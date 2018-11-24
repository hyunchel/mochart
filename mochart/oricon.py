from mochart import utils


BASE_URL = "https://www.oricon.co.jp/rank/js"
SELECTOR = "section.box-rank-entry"
TIMEZONE = "Asia/Tokyo"


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
    base_url = f"{BASE_URL}/d"
    local_dt = utils.localize_time(day_time, TIMEZONE)
    url = utils.append_date_string(
        base_url, local_dt, date_format="%Y-%m-%d", trailing_slash=True)
    return utils.get_ranks(url, SELECTOR, parser)


def week(day_time=None):
    base_url = f"{BASE_URL}/w"
    local_dt = utils.localize_time(day_time, TIMEZONE)
    beg, _ = utils.get_week_dates(local_dt)
    url = utils.append_date_string(
        base_url, local_dt, date_format="%Y-%m-%d", trailing_slash=True)
    return utils.get_ranks(url, SELECTOR, parser)


def month(day_time=None):
    base_url = f"{BASE_URL}/m"
    local_dt = utils.localize_time(day_time, TIMEZONE)
    beg, _ = utils.get_week_dates(local_dt)
    url = utils.append_date_string(
        base_url, local_dt, date_format="%Y-%m", trailing_slash=True)
    return utils.get_ranks(url, SELECTOR, parser)


def year(day_time=None):
    base_url = f"{BASE_URL}/y"
    local_dt = utils.localize_time(day_time, TIMEZONE)
    beg, _ = utils.get_week_dates(local_dt)
    url = utils.append_date_string(
        base_url, local_dt, date_format="%Y", trailing_slash=True)
    return utils.get_ranks(url, SELECTOR, parser)
