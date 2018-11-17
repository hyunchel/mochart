"""Parse ranks from Melon Music Chart."""
from mochart import utils


def parser(rows):
    """Parse texts accordingly from Melon table."""
    def remove_dups(rows):
        return rows[len(rows) // 2:]
    def get_texts(rows):
        return map(lambda row: row.text, rows)
    def group_multiples(rows):
        return ", ".join(rows)
    def parse(selector):
        return map(
            (
                lambda row:
                    group_multiples(
                        get_texts(
                            remove_dups(
                                row.select(selector))))
            ),
            rows[1:]
        )
    return [
        {"title": t[0], "artist": t[1], "album": t[2]}
        for t in zip(
            parse("div.ellipsis.rank01 a"),
            parse("div.ellipsis.rank02 a"),
            parse("div.ellipsis.rank03 a"),
        )
    ]


def realtime():
    """Get latest real-time ranks.
    
    NOTE: According to Melon's public announcement,
          "real-time" work will pause for 6 hours every day from 1AM - 7AM.
          Reference: https://www.melon.com/customer/announce/infomAnnounce.htm?seq=668
    """
    # Do not need any day time.
    url = "https://www.melon.com/chart/index.htm"
    return utils.get_ranks(url, "tr", parser)


def trend(day_time=None):
    """Get latest trending ranks.
    
    NOTE: Historical value refreshes daily.
    """
    base_url = "https://www.melon.com/chart/rise/index.htm"
    url = utils.append_date_string(base_url, day_time, date_key="dayTime", date_format="%Y%m%d%H")
    return utils.get_ranks(url, "tr", parser)


def day():
    """Get latest daily ranks."""
    url = "https://www.melon.com/chart/day/index.htm"
    return utils.get_ranks(url, "tr", parser)


def week():
    """Get latest weekly ranks."""
    url = "https://www.melon.com/chart/week/index.htm"
    return utils.get_ranks(url, "tr", parser)


def month():
    """Get latest monthly ranks."""
    url = "https://www.melon.com/chart/month/index.htm"
    return utils.get_ranks(url, "tr", parser)
