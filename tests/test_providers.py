from datetime import datetime, timedelta
from unittest.mock import MagicMock

import pytest

from mochart import (melon, mnet, naver, gaon, oricon)


PROVIDERS = [melon, mnet, naver, gaon, oricon]


@pytest.mark.integration
def test_sanity_checks():
    """Assert some ranks are fetched."""
    two_days_ago = datetime.now() - timedelta(days=2)
    for provider in PROVIDERS:
        try:
            assert len(provider.day(two_days_ago)) > 5
        except TypeError:
            assert len(provider.day()) > 5
        except AttributeError:
            assert len(provider.week(two_days_ago)) > 5


def test_gaon_parser(monkeypatch, gaon_week):
    """Assert parser extracts some ranks."""
    mock_get_html_document = MagicMock(return_value=gaon_week)
    monkeypatch.setattr(gaon.utils, "get_html_document", mock_get_html_document)
    ranks = gaon.week()
    assert len(ranks) > 0


def test_melon_parser(monkeypatch, melon_realtime):
    """Assert parser extracts some ranks."""
    mock_get_html_document = MagicMock(return_value=melon_realtime)
    monkeypatch.setattr(melon.utils, "get_html_document", mock_get_html_document)
    ranks = melon.realtime()
    assert len(ranks) > 0


def test_mnet_parser(monkeypatch, mnet_realtime):
    """Assert parser extracts some ranks."""
    mock_get_html_document = MagicMock(return_value=mnet_realtime)
    monkeypatch.setattr(mnet.utils, "get_html_document", mock_get_html_document)
    ranks = mnet.realtime()
    assert len(ranks) > 0


def test_naver_parser(monkeypatch, naver_day):
    """Assert parser extracts some ranks."""
    mock_get_html_document = MagicMock(return_value=naver_day)
    monkeypatch.setattr(naver.utils, "get_html_document", mock_get_html_document)
    ranks = naver.day()
    assert len(ranks) > 0


def test_oricon_parser(monkeypatch, oricon_day):
    """Assert parser extracts some ranks."""
    mock_get_html_document = MagicMock(return_value=oricon_day)
    monkeypatch.setattr(oricon.utils, "get_html_document", mock_get_html_document)
    ranks = oricon.day()
    assert len(ranks) > 0
