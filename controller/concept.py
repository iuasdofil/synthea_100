import logging

from flask import Blueprint, request, jsonify, Response

from models import Session, Concept

concept = Blueprint('concept', __name__)


def parse_concept_params(args: dict):
    keyword = args.get('keyword')
    last_id = args.get('last_id', default=0, type=int)
    limit = args.get('limit', default=20, type=int)

    if keyword is not None:
        keyword = keyword.lower()

    return keyword, last_id, limit


@concept.route('', methods=['GET'])
def concept_keyword_pagination():
    session = Session()
    try:
        keyword, last_id, limit = parse_concept_params(request.args)

        query = session.query(Concept).select_from(Concept)
        if keyword is not None:
            query = query.filter(Concept.c.concept_name.ilike(f'%{keyword}%'))
        rows = query.filter(Concept.c.concept_id > last_id).order_by(Concept.c.concept_id).limit(limit).all()

        return jsonify([row._asdict() for row in rows])
    except Exception as e:
        logging.exception(e)
        return Response(mimetype='application/json', status=400)
    finally:
        session.close()
