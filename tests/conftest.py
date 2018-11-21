import os

import pytest


def get_html_fixture(provider):
    filename = f"{provider}.html"
    with open(os.path.join(os.path.dirname(__file__), "fixtures", filename), "r") as f:
        return f.read()


@pytest.fixture
def melon_realtime():
    return get_html_fixture("melon_realtime")


@pytest.fixture
def mnet_realtime():
    return get_html_fixture("mnet_realtime")


@pytest.fixture
def gaon_realtime():
    return get_html_fixture("gaon_week")


@pytest.fixture
def naver_realtime():
    return get_html_fixture("naver_day")


@pytest.fixture
def oricon_realtime():
    return get_html_fixture("oricon_day")
