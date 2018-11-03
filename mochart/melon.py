"""Parse ranks from Melon Music Chart."""
from mochart import utils


SELECTORS = {
    "title": "div.ellipsis.rank01 > span > a",
    "artist": "div.ellipsis.rank02 > span > a",
    "album": "div.ellipsis.rank03 > a",
}


def realtime(day_time=None):
    """Get latest real-time ranks."""
    # Do not need any day time.
    url = "https://www.melon.com/chart/index.htm"
    return utils.get_ranks(url, SELECTORS)


def trend(day_time=None):
    """Get latest trending ranks."""
    base_url = "https://www.melon.com/chart/rise/index.htm"
    url = utils.append_day_time(base_url, day_time)
    return utils.get_ranks(url, SELECTORS)


def day(day_time=None):
    """Get latest daily ranks."""
    base_url = "https://www.melon.com/chart/day/index.htm"
    url = utils.append_day_time(base_url, day_time)
    return utils.get_ranks(url, SELECTORS)


def week(day_time=None):
    """Get latest weekly ranks."""
    base_url = "https://www.melon.com/chart/week/index.htm"
    url = utils.append_day_time(base_url, day_time)
    return utils.get_ranks(url, SELECTORS)


def month(day_time=None):
    """Get latest monthly ranks."""
    base_url = "https://www.melon.com/chart/month/index.htm"
    url = utils.append_day_time(base_url, day_time)
    return utils.get_ranks(url, SELECTORS)
