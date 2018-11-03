"""Parse ranks from Melon Music Chart."""
from mochart.utils import get_ranks


def realtime():
    """Get latest real-time ranks."""
    url = "https://www.melon.com/chart/index.htm"
    selectors = {
        "title": "div.ellipsis.rank01 > span > a",
        "artist": "div.ellipsis.rank02 > span > a",
        "album": "div.ellipsis.rank03 > a",
    }
    return get_ranks(url, selectors)


def trend():
    """Get latest trending ranks."""
    url = "https://www.melon.com/chart/rise/index.htm"
    selectors = {
        "title": "div.ellipsis.rank01 > span > a",
        "artist": "div.ellipsis.rank02 > span > a",
        "album": "div.ellipsis.rank03 > a",
    }
    return get_ranks(url, selectors)



def day():
    """Get latest daily ranks."""
    url = "https://www.melon.com/chart/day/index.htm"
    selectors = {
        "title": "div.ellipsis.rank01 > span > a",
        "artist": "div.ellipsis.rank02 > span > a",
        "album": "div.ellipsis.rank03 > a",
    }
    return get_ranks(url, selectors)



def week():
    """Get latest weekly ranks."""
    url = "https://www.melon.com/chart/week/index.htm"
    selectors = {
        "title": "div.ellipsis.rank01 > span > a",
        "artist": "div.ellipsis.rank02 > span > a",
        "album": "div.ellipsis.rank03 > a",
    }
    return get_ranks(url, selectors)


def month():
    """Get latest monthly ranks."""
    url = "https://www.melon.com/chart/month/index.htm"
    selectors = {
        "title": "div.ellipsis.rank01 > span > a",
        "artist": "div.ellipsis.rank02 > span > a",
        "album": "div.ellipsis.rank03 > a",
    }
    return get_ranks(url, selectors)
