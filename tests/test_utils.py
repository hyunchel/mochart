"""Unit tests for utility functions."""
from datetime import datetime

from mochart import utils


def test_none_day_time():
    """Assert None value for day_time parameter."""
    url = "some URL string"
    day_time = None
    assert "dayTime" in utils.append_day_time(url, day_time)


def test_day_time_present():
    """Assert a value for day_time parameter."""
    url = "some URL string"
    day_time = datetime.now()
    date_str = day_time.strftime("%Y%m%d%H")
    assert date_str in utils.append_day_time(url, day_time)
