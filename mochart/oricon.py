from mochart import utils


def parser(rows):
    """Parse texts accordingly from Oricon table."""
    ranks = []

    def group_by_multiples(rows):
        return ", ".join([link.text for link in rows])

    for row in rows:
        rank = {}
        rank["title"] = group_by_multiples(row.select(".title"))
        rank["artist"] = group_by_multiples(row.select(".name"))
        ranks.append(rank)

    return ranks


def day(day_time=None):
    base_url = "https://www.oricon.co.jp/rank/js/d"
    url = utils.append_date_string(
        base_url, day_time, date_format="%Y-%m-%d", trailing_slash=True)
    return utils.get_ranks(url, "section.box-rank-entry", parser)


def week(day_time=None):
    base_url = "https://www.oricon.co.jp/rank/js/w"
    beg, _ = utils.get_week_dates(day_time)
    url = utils.append_date_string(
        base_url, day_time, date_format="%Y-%m-%d", trailing_slash=True)
    return utils.get_ranks(url, "section.box-rank-entry", parser)


def month(day_time=None):
    base_url = "https://www.oricon.co.jp/rank/js/m"
    beg, _ = utils.get_week_dates(day_time)
    url = utils.append_date_string(
        base_url, day_time, date_format="%Y-%m", trailing_slash=True)
    return utils.get_ranks(url, "section.box-rank-entry", parser)


def year(day_time=None):
    base_url = "https://www.oricon.co.jp/rank/js/y"
    beg, _ = utils.get_week_dates(day_time)
    url = utils.append_date_string(
        base_url, day_time, date_format="%Y", trailing_slash=True)
    return utils.get_ranks(url, "section.box-rank-entry", parser)
