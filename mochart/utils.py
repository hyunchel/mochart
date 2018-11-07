"""Utility functions shared by all providers."""
from collections import OrderedDict
from datetime import datetime, timedelta

import pytz
import requests
from bs4 import BeautifulSoup


def get_html_document(url):
    """Get HTML document of given URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_html_document(html_doc, selectors, parser):
    """Select items in HTML document."""
    soup = BeautifulSoup(html_doc, "html.parser")
    table = soup.table

    # These are in order.
    items = OrderedDict()
    for key, selector in selectors.items():
        values = parser(table, selector)
        items[key] = values

    keys = items.keys()
    return [
        {key: value for key, value in zip(keys, values)}
        for values in zip(*items.values())
    ]


def get_ranks(url, selectors, parser):
    """Prase ranks from with URL and selectors."""
    return parse_html_document(
        get_html_document(url),
        selectors,
        parser,
    )


def localize_time(day_time):
    """Return Seoul time."""
    if day_time is None:
        day_time = datetime.now()
    seoul = pytz.timezone("Asia/Seoul")
    return day_time.astimezone(seoul)


def append_date_string(url, day_time, date_key=None, date_format=None):
    """Add date string to the URL."""
    seoul_dt = localize_time(day_time)
    dt_str = seoul_dt.strftime(date_format)
    if date_key:
        return f"{url}?{date_key}={dt_str}"
    return f"{url}/{dt_str}"


def get_week_dates(day_time):
    """Return the beginning and end of the week which given time falls to."""
    seoul_dt = localize_time(day_time)
    beg = seoul_dt - timedelta(days=seoul_dt.weekday())
    end = beg + timedelta(days=6)
    return beg, end


def get_weeks_in(day_time, start_zero=False, start_sunday=False):
    """Return the number of weeks into given month."""
    dt = localize_time(day_time)
    week_format = "%U" if start_sunday else "%W"
    addition = 0 if start_zero else 1
    current_week = int(dt.strftime(week_format))
    beginning_week = int(datetime(dt.year, dt.month, 1).strftime(week_format))
    return current_week - beginning_week + addition
