from mochart import utils


SELECTORS = {
    "title": "td.MMLItemTitle > div > div.MMLITitle_Box.info > div.MMLITitleSong_Box > a.MMLI_Song",
    "artist": "td.MMLItemTitle > div > div.MMLITitle_Box.info > div.MMLITitle_Info",
    "album": "td.MMLItemTitle > div > div.MMLITitle_Box.info > div.MMLITitle_Info > a.MMLIInfo_Album",
}


def parser(table, selector):
    """Parse texts accordingly from Mnet table."""
    values = []
    for row in table.select(selector):

        if "MMLI_Song" in selector:
            values.append(row.text)
        elif "MMLIInfo_Album" in selector:
            values.append(row.text)
        else:
            # Requires a bit of tricks due to multiple artists.
            artists = ", ".join([link.text for link in row.select("a.MMLIInfo_Artist")])
            values.append(artists)
    return values


def realtime(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    url = utils.append_date_string(base_url, day_time, date_format="%Y%m%d%H")
    return utils.get_ranks(url, SELECTORS, parser)


def day(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    url = utils.append_date_string(base_url, day_time, date_format="%Y%m%d")
    return utils.get_ranks(url, SELECTORS, parser)


def week(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    beg, end = utils.get_week_dates(day_time)
    # Should this be added to "append_date_string"?
    date_format = "%Y%m%d"
    url = f"{base_url}/{beg.strftime(date_format)}-{end.strftime(date_format)}"
    return utils.get_ranks(url, SELECTORS, parser)


def month(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    url = utils.append_date_string(base_url, day_time, date_format="%Y%m")
    return utils.get_ranks(url, SELECTORS, parser)


def year(day_time=None):
    base_url = "http://www.mnet.com/chart/TOP100"
    url = utils.append_date_string(base_url, day_time, date_format="%Y")
    return utils.get_ranks(url, SELECTORS, parser)
