"""Utility functions shared by all providers."""
from datetime import datetime, timedelta

import pytz
import requests
from bs4 import BeautifulSoup


def get_html_document(url):
    """Get HTML document of given URL."""
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36", # noqa
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", # noqa
    }
    resp = requests.get(url, headers=headers)
    return resp.text


def apply_parser(html_doc, selector, parser):
    """Parse items in HTML document."""
    soup = BeautifulSoup(html_doc, "html.parser")
    return parser(soup.select(selector))


def get_ranks(url, selector, parser):
    """Prase ranks from with URL and selectors."""
    return apply_parser(
        get_html_document(url),
        selector,
        parser,
    )


def localize_time(day_time, timezone="UTC"):
    """Return local time, defaulting to UTC.

    >>> dt = datetime(2018, 11, 17)
    >>> local_dt = localize_time(dt)
    >>> local_dt.tzname()
    'UTC'
    >>> local_dt = localize_time(dt, "Asia/Seoul")
    >>> local_dt.tzname()
    'KST'
    """
    if day_time is None:
        day_time = datetime.now()
    local = pytz.timezone(timezone)
    return day_time.astimezone(local)


def append_date_string(url,
                       day_time,
                       date_key=None,
                       date_format="%Y-%m-%d",
                       trailing_slash=False):
    """Add date string to the URL.

    >>> url = "https://mochart.com"
    >>> dt = datetime(2018, 11, 17)
    >>> append_date_string(url, dt)
    'https://mochart.com/2018-11-17'
    """
    dt_str = day_time.strftime(date_format)
    slash = ""
    if trailing_slash:
        slash = "/"
    if date_key:
        return f"{url}?{date_key}={dt_str}{slash}"
    return f"{url}/{dt_str}{slash}"


def get_week_dates(day_time):
    """Return the beginning and end of the week which given time falls to.

    >>> dt = datetime(2018, 11, 17)
    >>> beg, end = get_week_dates(dt)
    >>> beg.strftime("%Y-%m-%d")
    '2018-11-12'
    >>> end.strftime("%Y-%m-%d")
    '2018-11-18'
    """
    beg = day_time - timedelta(days=day_time.weekday())
    end = beg + timedelta(days=6)
    return beg, end


def get_weeks_in(day_time, start_zero=False, start_sunday=False):
    """Return the number of weeks into given month.

    >>> dt = datetime(2018, 1, 1)
    >>> get_weeks_in(dt)
    1
    """
    current_week = int(get_weeks(day_time))
    beginning_week = int(get_weeks(datetime(day_time.year, day_time.month, 1)))
    addition = 0 if start_zero else 1
    return current_week - beginning_week + addition


def get_weeks(day_time, start_sunday=False):
    """Return the number of weeks into given month in string.

    >>> dt = datetime(2018, 1, 1)
    >>> get_weeks(dt)
    '01'
    """
    dt = localize_time(day_time)
    week_format = "%U" if start_sunday else "%W"
    return dt.strftime(week_format)


def get_months(day_time):
    """Return month in string.

    >>> dt = datetime(2018, 1, 1)
    >>> get_months(dt)
    '01'
    """
    dt = localize_time(day_time)
    return dt.strftime("%m")


def get_years(day_time):
    """Return year in string.

    >>> dt = datetime(2018, 1, 1)
    >>> get_years(dt)
    '2018'
    """
    dt = localize_time(day_time)
    return dt.strftime("%Y")


def group_multiples(links):
    """Join links by comma if more than one.

    >>> from collections import namedtuple
    >>> Link = namedtuple("Link", ["text"])
    >>> artists = [Link("IU"), Link("Sungha Jung")]
    >>> group_multiples(artists)
    'IU, Sungha Jung'
    """
    return ", ".join([link.text.strip() for link in links])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
