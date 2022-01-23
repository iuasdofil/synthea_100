# Synthea

--------------------
## API 설명

--------------------
### person
#### GET /person/type_count<br>
조건에 일치하는 환자 수를 반환해줍니다.

filter 조건<br><br>
gender: 성별조건에 일치하는 환자 수를 반환해줍니다.<br>
gender의 값은 F(Female), M(Male)을 가질 수 있습니다.<br>
example)<br>
GET /person/type_count?gender=F<br>
GET /person/type_count?gender=M<br>

race: 인종 조건에 일치하는 환자 수를 반환해줍니다.<br>
race의 값은 other, native, black, white, asian을 가질 수 있습니다.<br>
example)<br> 
GET /person/type_count?race=other<br>
GET /person/type_count?race=white<br>

ethnicity: 민족 조건에 일치하는 환자 수를 반환해줍니다.<br>
ethnicity의 값은 nonhispanic, hispanic을 가질 수 있습니다.<br>
example)<br>
GET /person/type_count?ethnicity=nonhispanic<br>
GET /person/type_count?ethnicity=hispanic<br>

death: 사망한 환자 수를 반환해줍니다.<br>
death의 값은 T 값을 가질 수 있습니다.<br>
example)<br>
GET /person/type_count?death=T


success response<br>
```json
{"count": 1000}
```


invalid parameter error<br>
status code: 400

#### GET /person/visit_count
조건에 일치하는 방문자 수를 반환해줍니다.

filter 조건<br><br>

visit: 방문유형(입원/외래/응급)별 방문자 수<br>
visit의 값은 'Inpatient Visit', 'Outpatient Visit', 'Emergency Room Visit'을 가질 수 있습니다.
example)<br>
GET /person/visit_count?visit=Inpatient%20Visit
GET /person/visit_count?visit=Outpatient%20Visit
GET /person/visit_count?visit=Emergency%20Room%20Visit

gender: 성별별 방문자 수<br>
gender의 값은 F(Female), M(Male)을 가질 수 있습니다.<br>
GET /person/visit_count?gender=F
GET /person/visit_count?gender=M

race: 인종별 방문자 수<br>
race의 값은 other, native, black, white, asian을 가질 수 있습니다.<br>
GET /person/visit_count?race=other
GET /person/visit_count?race=native
GET /person/visit_count?race=white

ethnicity: 민족별 방문자 수<br>
ethnicity의 값은 nonhispanic, hispanic을 가질 수 있습니다.<br>
GET /person/visit_count?ethnicity=nonhispanic
GET /person/visit_count?ethnicity=hispanic

age_group: 연령별 방문자 수<br>
age_group은 10세 단위별 정수 값을 가질 수 있습니다.
GET /person/visit_count?age_group=10
GET /person/visit_count?age_group=30

success response<br>
```json
{"count": 41810}
```

invalid parameter error<br>
status code: 400


---------------
### concept
#### GET /concept
concept 정보를 조회할 수 있는 API 입니다.

조건에 일치하는 concept 정보를 반환해줍니다.<br>
keyword 필터를 사용하면 키워드 검색 가능합니다.<br>
keyword는 검색할 값을 입력할 수 있습니다. 대소문자 가리지 않고 단어가 keyword 값이 포함된 concept 정보를 반환해줍니다.

pagination parameter
last_id, limit을 통해서 pagination 조회가 가능합니다. 
last_id: 마지막 concept_id 값을 주면 last_id보다 큰 concept_id만 반환됩니다.
limit: 조회할 데이터의 개수입니다.

GET /concept
GET /concept?keyword=gender
GET /concept?keyword=gender&last_id=20&limit=30

success response
```json
[
    {
        "concept_class_id": "Domain",
        "concept_code": "OMOP generated",
        "concept_id": 2,
        "concept_name": "Gender",
        "domain_id": "Metadata",
        "invalid_reason": null,
        "standard_concept": null,
        "valid_end_date": "Thu, 31 Dec 2099 00:00:00 GMT",
        "valid_start_date": "Thu, 01 Jan 1970 00:00:00 GMT",
        "vocabulary_id": "Domain"
    },
    {
        "concept_class_id": "Main Heading",
        "concept_code": "D000068116",
        "concept_id": 28512,
        "concept_name": "Gender Dysphoria",
        "domain_id": "Condition",
        "invalid_reason": null,
        "standard_concept": null,
        "valid_end_date": "Thu, 31 Dec 2099 00:00:00 GMT",
        "valid_start_date": "Mon, 09 May 2016 00:00:00 GMT",
        "vocabulary_id": "MeSH"
    }
]
```

invalid parameter error<br>
status code: 400

### inquiry
#### GET /inquiry/person
환자 정보를 조회할 수 있는 API 입니다.

filter 조건
gender: 성별조건에 일치하는 환자 수를 반환해줍니다.<br>
gender의 값은 F(Female), M(Male)을 가질 수 있습니다.<br>
GET /inquiry/person?gender=F<br>
GET /inquiry/person?gender=M<br>

race: 인종 조건에 일치하는 환자 수를 반환해줍니다.<br>
race의 값은 other, native, black, white, asian을 가질 수 있습니다.<br>
example)<br> 
GET /inquiry/person?race=other<br>
GET /inquiry/person?race=white<br>

pagination parameter
last_id, limit을 통해서 pagination 조회가 가능합니다. 
last_id: 마지막 concept_id 값을 주면 last_id보다 큰 concept_id만 반환됩니다.
limit: 조회할 데이터의 개수입니다.


```json
[
    {
        "birth_datetime": "Mon, 20 Mar 1967 00:00:00 GMT",
        "care_site_id": null,
        "day_of_birth": 20,
        "ethnicity_concept_id": 0,
        "ethnicity_source_concept_id": 0,
        "ethnicity_source_value": "nonhispanic",
        "gender_code": "FEMALE",
        "gender_concept_id": 8532,
        "gender_source_concept_id": 0,
        "gender_source_value": "F",
        "location_id": null,
        "month_of_birth": 3,
        "person_id": 2955,
        "person_source_value": "57d587ce-fa2f-4661-bf80-5abdce3f190f",
        "provider_id": null,
        "race_code": "White",
        "race_concept_id": 8527,
        "race_source_concept_id": 0,
        "race_source_value": "white",
        "year_of_birth": 1967
    },
    {
        "birth_datetime": "Tue, 27 Mar 2018 00:00:00 GMT",
        "care_site_id": null,
        "day_of_birth": 27,
        "ethnicity_concept_id": 0,
        "ethnicity_source_concept_id": 0,
        "ethnicity_source_value": "nonhispanic",
        "gender_code": "FEMALE",
        "gender_concept_id": 8532,
        "gender_source_concept_id": 0,
        "gender_source_value": "F",
        "location_id": null,
        "month_of_birth": 3,
        "person_id": 4915,
        "person_source_value": "3c2a1f2f-54c4-4c20-a905-b32b94277829",
        "provider_id": null,
        "race_code": "White",
        "race_concept_id": 8527,
        "race_source_concept_id": 0,
        "race_source_value": "white",
        "year_of_birth": 2018
    }
]
```

invalid parameter error<br>
status code: 400
