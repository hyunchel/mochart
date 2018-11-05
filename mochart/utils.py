"""Utility functions shared by all providers."""
from collections import OrderedDict
from datetime import datetime

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


def append_day_time(url, day_time):
    """Add date string to the URL."""
    if day_time is None:
        day_time = datetime.now()
    seoul_dt = localize_time(day_time)
    dt_str = seoul_dt.strftime('%Y%m%d%H')
    return f"{url}?dayTime={dt_str}"
