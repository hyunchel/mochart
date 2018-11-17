from mochart import utils

SELECTORS = {
    "title": "td.name > a._title > span",
    "artist": "td._artist > a",
}


def parser(rows):
    """Parse texts accordingly from Naver table."""

    def group_multiples(rows):
        return ", ".join([link.text.strip() for link in rows])

    ranks = []
    for row in rows[2:]:
        rank = {}
        rank["title"] = group_multiples(
            row.select("td.name > a._title > span"))
        rank["artist"] = group_multiples(row.select("td._artist > a"))
        ranks.append(rank)
    return ranks


def realtime(day_time=None):
    """Return realtime rankings."""
    url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1h"
    return utils.get_ranks(url, "tr", parser)


def day(day_time=None):
    """Return rankings for the day."""
    url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1d"
    return utils.get_ranks(url, "tr", parser)


def week(day_time=None):
    """Return rankings for given week."""
    url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=7d"

    if day_time is not None:
        base_url = "https://music.naver.com/listen/history/index.nhn?type=TOTAL"

        dt = utils.localize_time(day_time)
        year = dt.strftime("%Y")
        month = dt.strftime("%m")
        # 0 == all, so the first week is 1.
        week = utils.get_weeks_in(dt)

        url = f"{base_url}&year={year}&month={month}&week={week}"

    return utils.get_ranks(url, "tr", parser)


def month(day_time=None):
    """Return rankings for given month."""
    url = "https://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=28d"
    if day_time is not None:
        base_url = "https://music.naver.com/listen/history/index.nhn?type=TOTAL"

        dt = utils.localize_time(day_time)
        year = dt.strftime("%Y")
        month = dt.strftime("%m")
        # 0 == all, so the first week is 1.
        week = 0

        url = f"{base_url}&year={year}&month={month}&week={week}"

    return utils.get_ranks(url, "tr", parser)
