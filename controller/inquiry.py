from flask import Blueprint, jsonify, request, Response

from models import Session, Person, Concept, Death
from sqlalchemy.orm import aliased
import logging


inquiry = Blueprint('inquiry', __name__)


def parse_person_params(args: dict):
    gender = args.get('gender')
    race = args.get('race')
    last_id = args.get('last_id', default=0, type=int)
    limit = args.get('limit', default=20, type=int)
    return gender, race, last_id, limit


@inquiry.route('/person', methods=['GET'])
def person():
    session = Session()
    try:
        gender, race, last_id, limit = parse_person_params(request.args)
        gender_concept, race_concept = aliased(Concept, name='gender_concept'), aliased(Concept, name='race_concept')

        query = session.query(Person, gender_concept.c.concept_name.label('gender_code'),
                              race_concept.c.concept_name.label('race_code'))\
            .select_from(Person)\
            .join(gender_concept, Person.c.gender_concept_id == gender_concept.c.concept_id)\
            .join(race_concept, Person.c.race_concept_id == race_concept.c.concept_id)

        if gender is not None:
            query = query.filter(gender_concept.c.concept_name.ilike(f'%{gender}%'))

        if race is not None:
            query = query.filter(race_concept.c.concept_name.ilike(f'%{race}%'))

        rows = query.filter(Person.c.person_id > last_id).order_by(Person.c.person_id).limit(limit).all()
        return jsonify([row._asdict() for row in rows])
    except Exception as e:
        logging.exception(e)
        return Response(mimetype='application/json', status=400)
    finally:
        session.close()
