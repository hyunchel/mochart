"""Parse ranks from Melon Music Chart."""
from mochart import utils


BASE_URL = "https://www.melon.com/chart"
SELECTOR = "tr"


def parser(rows):
    """Parse texts accordingly from Melon table."""

    def remove_dups(rows):
        return rows[len(rows) // 2:]

    def parse(selector):
        return map(
            (
                lambda row:
                    utils.group_multiples(
                        remove_dups(
                            row.select(selector)))
            ),
            rows[1:]
        )

    return [{
        "title": t[0],
        "artist": t[1],
        "album": t[2]
    } for t in zip(
        parse("div.ellipsis.rank01 a"),
        parse("div.ellipsis.rank02 a"),
        parse("div.ellipsis.rank03 a"),
    )]


def realtime():
    """Get latest real-time ranks.

    NOTE: According to Melon's public announcement,
          "real-time" work will pause for 6 hours every day from 1AM - 7AM.
          Reference:
          https://www.melon.com/customer/announce/infomAnnounce.htm?seq=668
    """
    url = f"{BASE_URL}/index.htm"
    return utils.get_ranks(url, SELECTOR, parser)


def trend(day_time=None):
    """Get latest trending ranks.

    NOTE: Historical value refreshes daily.
    """
    base_url = f"{BASE_URL}/rise/index.htm"
    local_dt = utils.localize_time(day_time, "Asia/Seoul")
    url = utils.append_date_string(
        base_url, local_dt, date_key="dayTime", date_format="%Y%m%d%H")
    return utils.get_ranks(url, SELECTOR, parser)


def day():
    """Get latest daily ranks."""
    url = f"{BASE_URL}/day/index.htm"
    return utils.get_ranks(url, SELECTOR, parser)


def week():
    """Get latest weekly ranks."""
    url = f"{BASE_URL}/week/index.htm"
    return utils.get_ranks(url, SELECTOR, parser)


def month():
    """Get latest monthly ranks."""
    url = f"{BASE_URL}/month/index.htm"
    return utils.get_ranks(url, SELECTOR, parser)
