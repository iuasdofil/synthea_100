import datetime
import logging

from flask import Blueprint, jsonify, request, Response
from sqlalchemy import func

from models import Session, Person, Death, VisitOccurrence

person = Blueprint('person', __name__)

visit_concept_type = {'Inpatient Visit': 9201, 'Outpatient Visit': 9202, 'Emergency Room Visit': 9203}


def parse_person_type(args: dict):
    gender = args.get('gender')
    race = args.get('race')
    ethnicity = args.get('ethnicity')
    death = args.get('death')

    if gender not in [None, 'F', 'M']:
        raise ValueError('Invalid gender value')

    if race not in [None, 'other', 'native', 'black', 'white', 'asian']:
        raise ValueError('Invalid race value')

    if ethnicity not in [None, 'nonhispanic', 'hispanic']:
        raise ValueError('Invalid ethnicity value')

    if death not in [None, 'T']:
        raise ValueError('Invalid death value')

    return gender, race, ethnicity, death


@person.route('/type_count', methods=['GET'])
def get_count_person():
    session = Session()
    try:
        gender, race, ethnicity, death = parse_person_type(request.args)
        query = session.query(func.count(Person.c.person_id)).select_from(Person)
        if gender is not None:
            query = query.filter(Person.c.gender_source_value == gender)

        if race is not None:
            query = query.filter(Person.c.race_source_value == race)

        if ethnicity is not None:
            query = query.filter(Person.c.ethnicity_source_value == ethnicity)

        if death is not None:
            query = query.join(Death)
        count = query.scalar()

        return jsonify({'count': count})
    except ValueError as ve:
        logging.exception(ve)
        return Response(mimetype='application/json', status=400)
    except Exception as e:
        logging.exception(e)
    finally:
        session.close()


def parse_visit_type(args: dict):
    visit = args.get('visit')
    gender = args.get('gender')
    race = args.get('race')
    ethnicity = args.get('ethnicity')
    age_group = args.get('age_group')

    if visit not in [None, 'Inpatient Visit', 'Outpatient Visit', 'Emergency Room Visit']:
        raise ValueError('Invalid visit value')
    if visit is not None:
        visit = visit_concept_type[visit]

    if gender not in [None, 'F', 'M']:
        raise ValueError('Invalid gender value')

    if race not in [None, 'other', 'native', 'black', 'white', 'asian']:
        raise ValueError('Invalid race value')

    if ethnicity not in [None, 'nonhispanic', 'hispanic']:
        raise ValueError('Invalid ethnicity value')

    if age_group is not None:
        try:
            age_group = int(age_group)
            if age_group % 10 != 0:
                raise ValueError('Invalid age_group value\nage_group is need divisible by 10')
        except ValueError:
            raise ValueError('Invalid age_group value\nage_group is require int type')

    return visit, gender, race, ethnicity, age_group


@person.route('/visit_count', methods=['GET'])
def get_visit():
    current_year = datetime.date.today().year
    session = Session()
    try:
        visit, gender, race, ethnicity, age_group = parse_visit_type(request.args)
        query = session.query(func.count(VisitOccurrence.c.visit_occurrence_id)).select_from(VisitOccurrence)
        if visit is not None:
            query = query.filter(VisitOccurrence.c.visit_concept_id == visit)

        if gender or race or ethnicity or age_group is not None:
            query = query.join(Person)

        if gender is not None:
            query = query.filter(Person.c.gender_source_value == gender)

        if race is not None:
            query = query.filter(Person.c.race_source_value == race)

        if ethnicity is not None:
            query = query.filter(Person.c.ethnicity_source_value == ethnicity)

        if age_group is not None:
            query = query.filter((current_year - age_group - 9) <= Person.c.year_of_birth)\
                .filter(Person.c.year_of_birth <= (current_year - age_group))

        count = query.scalar()
        return jsonify({'count': count})
    except ValueError as ve:
        logging.exception(ve)
        return Response(mimetype='application/json', status=400)
    except Exception as e:
        logging.exception(e)
    finally:
        session.close()
