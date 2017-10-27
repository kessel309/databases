import os
import json
import pytest
import sqlite3
import responses

from .config import (
    TESTING_DATABASE_PATH, DATABASE_SCHEMA_PATH, TESTING_GISTS_PATHS,
    POPULATED_DATABASE_PATH)


@pytest.fixture()
def clean_gists_database():
    db = sqlite3.connect(TESTING_DATABASE_PATH)
    with open(DATABASE_SCHEMA_PATH, 'r') as fp:
        db.executescript(fp.read())
    yield db
    db.close()
    os.remove(TESTING_DATABASE_PATH)


@pytest.fixture()
def populated_gists_database():
    db = sqlite3.connect(POPULATED_DATABASE_PATH)
    yield db
    db.close()


@pytest.fixture()
def mocked_requests():
    # /gists
    gists = []
    for testing_gist_path in TESTING_GISTS_PATHS:
        with open(testing_gist_path, 'r') as fp:
            gist = json.load(fp)
            gists.append(gist)

    responses.add(
        responses.GET, 'https://api.github.com/users/gvanrossum/gists',
        json=gists, status=200)

    # 404 request
    responses.add(
        responses.GET, 'https://api.github.com/users/rmotr-doesnt-exist/gists',
        status=404)
