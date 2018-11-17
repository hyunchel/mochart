"""Unit tests for utility functions."""
from datetime import datetime
from unittest.mock import MagicMock

import mochart.utils as utils


def test_get_html_document(monkeypatch):
    """Assert GET request is sent with URL and headers."""
    mock_requests = MagicMock()
    monkeypatch.setattr(utils, "requests", mock_requests)

    url = "some URL string"
    utils.get_html_document(url)

    assert url in mock_requests.get.call_args[0]
    assert "headers" in mock_requests.get.call_args[1]
