from mochart import utils


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
    base_url = "http://www.mnet.com/chart/TOP100"
    url = utils.append_date_string(base_url, day_time, date_format="%Y%m%d%H")
    return utils.get_ranks(
        url, "td.MMLItemTitle > div > div.MMLITitle_Box.info", parser)


def day(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    url = utils.append_date_string(base_url, day_time, date_format="%Y%m%d")
    return utils.get_ranks(
        url, "td.MMLItemTitle > div > div.MMLITitle_Box.info", parser)


def week(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    beg, end = utils.get_week_dates(day_time)
    date_format = "%Y%m%d"
    url = f"{base_url}/{beg.strftime(date_format)}-{end.strftime(date_format)}"
    return utils.get_ranks(
        url, "td.MMLItemTitle > div > div.MMLITitle_Box.info", parser)


def month(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    url = utils.append_date_string(base_url, day_time, date_format="%Y%m")
    return utils.get_ranks(
        url, "td.MMLItemTitle > div > div.MMLITitle_Box.info", parser)


def year(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    url = utils.append_date_string(base_url, day_time, date_format="%Y")
    return utils.get_ranks(
        url, "td.MMLItemTitle > div > div.MMLITitle_Box.info", parser)
