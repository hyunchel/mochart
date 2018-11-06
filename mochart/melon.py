"""Parse ranks from Melon Music Chart."""
from mochart import utils


SELECTORS = {
    "title": "div.ellipsis.rank01",
    "artist": "div.ellipsis.rank02",
    "album": "div.ellipsis.rank03",
}


def parser(table, selector):
    """Parse texts accordingly from Melon table."""
    values = []
    for row in table.select(selector):
        texts = [link.text for link in row.select("a")]
        texts = texts[len(texts) // 2:]
        values.append(", ".join(texts))
    return values


def realtime():
    """Get latest real-time ranks.
    
    NOTE: According to Melon's public announcement,
          "real-time" work will pause for 6 hours every day from 1AM - 7AM.
          Reference: https://www.melon.com/customer/announce/infomAnnounce.htm?seq=668
    """
    # Do not need any day time.
    url = "https://www.melon.com/chart/index.htm"
    return utils.get_ranks(url, SELECTORS, parser)


def trend(day_time=None):
    """Get latest trending ranks.
    
    NOTE: Historical value refreshes daily.
    """
    base_url = "https://www.melon.com/chart/rise/index.htm"
    url = utils.append_day_time(base_url, day_time)
    print(url)
    return utils.get_ranks(url, SELECTORS, parser)


def day():
    """Get latest daily ranks."""
    url = "https://www.melon.com/chart/day/index.htm"
    return utils.get_ranks(url, SELECTORS, parser)


def week():
    """Get latest weekly ranks."""
    url = "https://www.melon.com/chart/week/index.htm"
    return utils.get_ranks(url, SELECTORS, parser)


def month():
    """Get latest monthly ranks."""
    url = "https://www.melon.com/chart/month/index.htm"
    return utils.get_ranks(url, SELECTORS, parser)
