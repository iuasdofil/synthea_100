from sqlalchemy import Column, Integer, String, Date, ForeignKey, TIMESTAMP, BIGINT, Numeric, Text, Table, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import CONFIG

engine = create_engine(f'postgresql+psycopg2://{CONFIG["user"]}:{CONFIG["password"]}@{CONFIG["host"]}:{CONFIG["port"]}/'
                       f'{CONFIG["database"]}', pool_pre_ping=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()


Concept = Table(
    'concept',
    metadata,
    Column('concept_id', Integer, primary_key=True),
    Column('concept_name', String(255)),
    Column('domain_id', String(20)),
    Column('vocabulary_id', String(20)),
    Column('concept_class_id', String(20)),
    Column('standard_concept', String(1)),
    Column('concept_code', String(50)),
    Column('valid_start_date', Date),
    Column('valid_end_date', Date),
    Column('invalid_reason', String(1)),
)

Person = Table(
    'person',
    metadata,
    Column('person_id', Integer, primary_key=True),
    Column('gender_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('year_of_birth', Integer),
    Column('month_of_birth', Integer),
    Column('day_of_birth', Integer),
    Column('birth_datetime', TIMESTAMP),
    Column('race_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('ethnicity_concept_id', Integer),
    Column('location_id', BIGINT),
    Column('provider_id', BIGINT),
    Column('care_site_id', BIGINT),
    Column('person_source_value', String(50)),
    Column('gender_source_value', String(50)),
    Column('gender_source_concept_id', Integer),
    Column('race_source_value', String(50)),
    Column('race_source_concept_id', Integer),
    Column('ethnicity_source_value', String(50)),
    Column('ethnicity_source_concept_id', Integer)
)

VisitOccurrence = Table(
    'visit_occurrence',
    metadata,
    Column('visit_occurrence_id', BIGINT, primary_key=True),
    Column('person_id', BIGINT, ForeignKey('person.person_id')),
    Column('visit_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('visit_start_date', Date),
    Column('visit_start_datetime', TIMESTAMP),
    Column('visit_end_date', Date),
    Column('visit_end_datetime', TIMESTAMP),
    Column('visit_type_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('provider_id', BIGINT),
    Column('care_site_id', BIGINT),
    Column('visit_source_value', String(50)),
    Column('visit_source_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('admitted_from_concept_id', Integer),
    Column('admitted_from_source_value', String(50)),
    Column('discharge_to_source_value', String(50)),
    Column('discharge_to_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('preceding_visit_occurrence_id', BIGINT, ForeignKey('visit_occurrence.visit_occurrence_id'))
)

Death = Table(
    'death',
    metadata,
    Column('person_id', BIGINT, ForeignKey('person.person_id')),
    Column('death_date', Date),
    Column('death_datetime', TIMESTAMP),
    Column('death_type_concept_id', Integer),
    Column('cause_concept_id', BIGINT, ForeignKey('concept.concept_id')),
    Column('cause_source_value', Integer),
    Column('cause_source_concept_id', BIGINT, ForeignKey('concept.concept_id'))
)

DrugExposure = Table(
    'drug_exposure',
    metadata,
    Column('drug_exposure_id', BIGINT, nullable=False, primary_key=True),
    Column('person_id', BIGINT, ForeignKey('person.person_id')),
    Column('drug_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('drug_exposure_start_date', Date),
    Column('drug_exposure_start_datetime', TIMESTAMP),
    Column('drug_exposure_end_date', Date),
    Column('drug_exposure_end_datetime', TIMESTAMP),
    Column('verbatim_end_date', Date),
    Column('drug_type_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('stop_reason', String(20)),
    Column('refills', Integer),
    Column('quantity', Numeric),
    Column('days_supply', Integer),
    Column('sig', Text),
    Column('route_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('lot_number', String(50)),
    Column('provider_id', BIGINT),
    Column('visit_occurrence_id', BIGINT, ForeignKey('visit_occurrence.visit_occurrence_id')),
    Column('visit_detail_id', BIGINT),
    Column('drug_source_value', String(50)),
    Column('drug_source_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('route_source_value', String(50)),
    Column('dose_unit_source_value', String(50))
)

ConditionOccurrence = Table(
    'condition_occurrence',
    metadata,
    Column('condition_occurrence_id', BIGINT, nullable=False, primary_key=True),
    Column('person_id', BIGINT, ForeignKey('person.person_id')),
    Column('condition_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('condition_start_date', Date),
    Column('condition_start_datetime', TIMESTAMP),
    Column('condition_end_date', Date),
    Column('condition_end_datetime', TIMESTAMP),
    Column('condition_type_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('condition_status_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('stop_reason', String(20)),
    Column('provider_id', BIGINT),
    Column('visit_occurrence_id', BIGINT, ForeignKey('visit_occurrence.visit_occurrence_id')),
    Column('visit_detail_id', BIGINT),
    Column('condition_source_value', String(50)),
    Column('condition_source_concept_id', Integer, ForeignKey('concept.concept_id')),
    Column('condition_status_source_value', String(50))
)


DrugPair = Table(
    'drug_pair',
    metadata,
    Column('drug_concept_id1', Integer),
    Column('drug_concept_id2', Integer)
)


ClinicalNote = Table(
    'clinical_note',
    metadata,
    Column('note', Text)
)
