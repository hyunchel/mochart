"""Utility functions shared by all providers."""
from collections import OrderedDict
from datetime import datetime

import pytz
import requests
from bs4 import BeautifulSoup


def get_html_document(url):
    """Get HTML document of given URL."""
    headers = {
        "User-Agent": "mochart/0.0.1",
    }
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_html_document(html_doc, selectors):
    """Select items in HTML document."""
    soup = BeautifulSoup(html_doc, "html.parser")
    table = soup.table

    # These are in order.
    items = OrderedDict()
    for key, selector in selectors.items():
        items[key] = [link.text for link in table.select(selector)]

    keys = items.keys()
    return [
        {key: value for key, value in zip(keys, values)}
        for values in zip(*items.values())
    ]


def get_ranks(url, selectors):
    """Prase ranks from with URL and selectors."""
    return parse_html_document(
        get_html_document(url),
        selectors,
    )


def append_day_time(url, day_time):
    """Add date string to the URL."""
    if day_time is None:
        day_time = datetime.now()
    seoul = pytz.timezone("Asia/Seoul")
    seoul_dt = day_time.astimezone(seoul)
    dt_str = seoul_dt.strftime('%Y%m%d%H')
    return f"{url}?dayTime={dt_str}"
