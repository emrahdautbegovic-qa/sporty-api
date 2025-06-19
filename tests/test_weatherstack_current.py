import requests
import pytest
import os
import jsonschema
from helpers.file_helper import read_json


SCHEMA_PATH = os.path.join(os.path.dirname(__file__), '..', 'jsonschemas', 'current_weather_schema.json')
SCHEMA_PATH = os.path.abspath(SCHEMA_PATH)
BASE_URL = 'https://api.weatherstack.com'
ENDPOINT = 'current'
LOCATIONS=['New Delhi']


@pytest.mark.parametrize("city", LOCATIONS)
def test_current_weather_200(access_key, logger, city):
    response = requests.get(f'{BASE_URL}/{ENDPOINT}?query={city}&access_key={access_key}')
    logger.info(f'Response status code: {response.status_code}')

    assert response.status_code == 200

    data = response.json()
    logger.info(data)

    assert 'location' in data
    assert data['location']['name'] == city

    schema = read_json(SCHEMA_PATH)
    jsonschema.validate(instance=data, schema=schema)


@pytest.mark.parametrize("city", LOCATIONS)
def test_missing_access_key(logger, city):
    response = requests.get(f'{BASE_URL}/{ENDPOINT}?query={city}')
    logger.info(f'Response status code: {response.status_code}')

    assert response.status_code == 200

    data = response.json()
    logger.info(data)

    assert 'success' in data
    assert data['success'] == False
    assert data['error']['type'] == 'missing_access_key'


@pytest.mark.parametrize("city", LOCATIONS)
def test_units_s(access_key, logger, city):
    response = requests.get(f'{BASE_URL}/{ENDPOINT}?query={city}&units=s&access_key={access_key}')
    logger.info(f'Response status code: {response.status_code}')

    assert response.status_code == 200

    data = response.json()
    logger.info(data)

    assert 'location' in data
    assert data['location']['name'] == city
    assert data['current']['temperature'] > 200


def test_missing_query(logger, access_key):
    response = requests.get(f'{BASE_URL}/{ENDPOINT}?access_key={access_key}')
    logger.info(f'Response status code: {response.status_code}')

    assert response.status_code == 200

    data = response.json()
    logger.info(data)

    assert 'success' in data
    assert data['success'] == False
    assert data['error']['type'] == 'missing_query'