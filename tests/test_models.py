import pytest

from gists_database.models import Gist
from tests.fixtures import clean_gists_database

GIST_DATA = (
    7,
    '18bdf248a679155f1381',
    'https://gist.github.com/18bdf248a679155f1381',
    'https://gist.github.com/18bdf248a679155f1381.git',
    'https://gist.github.com/18bdf248a679155f1381.git',
    'https://api.github.com/gists/18bdf248a679155f1381/commits',
    'https://api.github.com/gists/18bdf248a679155f1381/forks',
    1,
    '2014-05-03T20:26:08Z',
    '2017-02-17T18:06:12Z',
    1,
    'https://api.github.com/gists/18bdf248a679155f1381/comments'
)


def test_gist_model_create(clean_gists_database):
    model = Gist(GIST_DATA)
    assert model.github_id == '18bdf248a679155f1381'
    assert model.html_url == 'https://gist.github.com/18bdf248a679155f1381'
    assert model.created_at == '2014-05-03T20:26:08Z'


def test_gist_model_create_invalid_params(clean_gists_database):
    with pytest.raises(KeyError):
        Gist({'this-is': 'invalid'})


def test_gist_model_str(clean_gists_database):
    model = Gist(GIST_DATA)
    assert str(model) == 'Gist: 18bdf248a679155f1381'
