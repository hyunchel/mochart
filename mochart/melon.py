"""Parse ranks from Melon Music Chart."""
from mochart import utils


SELECTORS = {
    "title": "div.ellipsis.rank01 > span > a",
    "artist": "div.ellipsis.rank02 > span > a",
    "album": "div.ellipsis.rank03 > a",
}


def realtime():
    """Get latest real-time ranks.
    
    NOTE: According to Melon's public announcement,
          "real-time" work will pause for 6 hours every day from 1AM - 7AM.
          Reference: https://www.melon.com/customer/announce/infomAnnounce.htm?seq=668
    """
    # Do not need any day time.
    url = "https://www.melon.com/chart/index.htm"
    return utils.get_ranks(url, SELECTORS)


def trend(day_time=None):
    """Get latest trending ranks.
    
    NOTE: Historical value refreshes daily.
    """
    url = "https://www.melon.com/chart/rise/index.htm"
    return utils.get_ranks(url, SELECTORS)


def day():
    """Get latest daily ranks."""
    url = "https://www.melon.com/chart/day/index.htm"
    return utils.get_ranks(url, SELECTORS)


def week():
    """Get latest weekly ranks."""
    url = "https://www.melon.com/chart/week/index.htm"
    return utils.get_ranks(url, SELECTORS)


def month():
    """Get latest monthly ranks."""
    url = "https://www.melon.com/chart/month/index.htm"
    return utils.get_ranks(url, SELECTORS)
