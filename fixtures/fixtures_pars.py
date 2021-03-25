import pytest

@pytest.fixture()
def check_connect():
    URL = 'https://rabota.by/search/vacancy?clusters=true&text=python&area=1002'
    HEADERS = {'User-Agent': 'Mozilla/5.0'}
    return URL, HEADERS
