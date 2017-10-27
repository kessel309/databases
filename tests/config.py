import os
from os.path import dirname as dot


BASE_TESTS_PATH = dot(__file__)
BASE_PROJECT_PATH = dot(dot(__file__))

TESTING_DATABASE_NAME = 'testing_gists_database.db'
TESTING_DATABASE_PATH = os.path.join(BASE_TESTS_PATH, TESTING_DATABASE_NAME)

POPULATED_DATABASE_NAME = 'populated_gists_database.db'
POPULATED_DATABASE_PATH = os.path.join(
    BASE_TESTS_PATH, POPULATED_DATABASE_NAME)



DATABASE_SCHEMA_PATH = os.path.join(BASE_PROJECT_PATH, 'schema.sql')

BASE_PATH = 'tests/gists_data'
TESTING_GISTS_NAMES = (
    '18bdf248a679155f1381.json',
    '1adb5bee99400ce615a5.json',
    '291bfcfe70d2f9582331.json',
    '4232a4cdad00bd92a7a64cf3e2795820.json',
    '86beaced733b7dbf2d034e56edb8d37e.json',
    'c669398c67386e9fb43e.json',
    'ef201fe313719305c4c7.json'
)

TESTING_GISTS_PATHS = [
    os.path.join(BASE_TESTS_PATH, 'gists_data/%s' % n)
    for n in TESTING_GISTS_NAMES]
