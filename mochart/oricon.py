from mochart import utils


def parser(rows):
    """Parse texts accordingly from Oricon table."""
    ranks = []
    for row in rows:
        rank = {}
        rank["title"] = utils.group_multiples(row.select(".title"))
        rank["artist"] = utils.group_multiples(row.select(".name"))
        ranks.append(rank)

    return ranks


def day(day_time=None):
    base_url = "https://www.oricon.co.jp/rank/js/d"
    local_dt = utils.localize_time(day_time, "Asia/Tokyo")
    url = utils.append_date_string(
        base_url, local_dt, date_format="%Y-%m-%d", trailing_slash=True)
    return utils.get_ranks(url, "section.box-rank-entry", parser)


def week(day_time=None):
    base_url = "https://www.oricon.co.jp/rank/js/w"
    local_dt = utils.localize_time(day_time, "Asia/Tokyo")
    beg, _ = utils.get_week_dates(local_dt)
    url = utils.append_date_string(
        base_url, local_dt, date_format="%Y-%m-%d", trailing_slash=True)
    return utils.get_ranks(url, "section.box-rank-entry", parser)


def month(day_time=None):
    base_url = "https://www.oricon.co.jp/rank/js/m"
    local_dt = utils.localize_time(day_time, "Asia/Tokyo")
    beg, _ = utils.get_week_dates(local_dt)
    url = utils.append_date_string(
        base_url, local_dt, date_format="%Y-%m", trailing_slash=True)
    return utils.get_ranks(url, "section.box-rank-entry", parser)


def year(day_time=None):
    base_url = "https://www.oricon.co.jp/rank/js/y"
    local_dt = utils.localize_time(day_time, "Asia/Tokyo")
    beg, _ = utils.get_week_dates(local_dt)
    url = utils.append_date_string(
        base_url, local_dt, date_format="%Y", trailing_slash=True)
    return utils.get_ranks(url, "section.box-rank-entry", parser)
