from mochart import utils


BASE_URL = "http://www.mnet.com/chart/TOP100"
SELECTOR = "td.MMLItemTitle > div > div.MMLITitle_Box.info"
TIMEZONE = "Asia/Seoul"


def parser(rows):
    """Parse texts accordingly from Mnet table."""
    ranks = []
    for row in rows:
        rank = {}
        rank["title"] = utils.group_multiples(row.select("a.MMLI_Song"))
        rank["album"] = utils.group_multiples(row.select("a.MMLIInfo_Album"))
        # Requires a bit of tricks due to multiple artists.
        rank["artist"] = utils.group_multiples(row.select("a.MMLIInfo_Artist"))
        ranks.append(rank)
    return ranks


def realtime(day_time=None):
    local_dt = utils.localize_time(day_time, TIMEZONE)
    url = utils.append_date_string(BASE_URL, local_dt, date_format="%Y%m%d%H")
    return utils.get_ranks(
        url, SELECTOR, parser)


def day(day_time=None):
    local_dt = utils.localize_time(day_time, TIMEZONE)
    url = utils.append_date_string(BASE_URL, local_dt, date_format="%Y%m%d")
    return utils.get_ranks(
        url, SELECTOR, parser)


def week(day_time=None):
    local_dt = utils.localize_time(day_time, TIMEZONE)
    beg, end = utils.get_week_dates(local_dt)
    date_format = "%Y%m%d"
    url = f"{BASE_URL}/{beg.strftime(date_format)}-{end.strftime(date_format)}"
    return utils.get_ranks(
        url, SELECTOR, parser)


def month(day_time=None):
    local_dt = utils.localize_time(day_time, TIMEZONE)
    url = utils.append_date_string(BASE_URL, local_dt, date_format="%Y%m")
    return utils.get_ranks(
        url, SELECTOR, parser)


def year(day_time=None):
    local_dt = utils.localize_time(day_time, TIMEZONE)
    url = utils.append_date_string(BASE_URL, local_dt, date_format="%Y")
    return utils.get_ranks(
        url, SELECTOR, parser)
