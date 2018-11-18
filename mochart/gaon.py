from mochart import utils


def parser(rows):
    """Parse texts accordingly from Gaon table."""
    titles = map(lambda t: t[1].text,
                 filter(lambda x: x[0] % 2 == 0, enumerate(rows)))
    artists = map(lambda t: t[1].text.split("|")[0],
                  filter(lambda x: x[0] % 2 != 0, enumerate(rows)))
    albums = map(lambda t: t[1].text.split("|")[1],
                 filter(lambda x: x[0] % 2 != 0, enumerate(rows)))
    return [{
        "title": title,
        "artist": artist,
        "album": album
    } for title, artist, album in zip(titles, artists, albums)]


def week(day_time=None):
    base_url = "http://www.gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=week" # noqa
    local_dt = utils.localize_time(day_time, "Asia/Seoul")
    weeks = utils.get_weeks(local_dt)
    years = utils.get_years(local_dt)
    url = f"{base_url}&targetTime={weeks}&hitYear={years}"
    return utils.get_ranks(url, "td.subject [title]", parser)


def month(day_time=None):
    base_url = "http://www.gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=month" # noqa
    local_dt = utils.localize_time(day_time, "Asia/Seoul")
    months = utils.get_months(local_dt)
    years = utils.get_years(local_dt)
    url = f"{base_url}&targetTime={months}&hitYear={years}"
    return utils.get_ranks(url, "td.subject [title]", parser)


def year(day_time=None):
    base_url = "http://www.gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=year" # noqa
    local_dt = utils.localize_time(day_time, "Asia/Seoul")
    years = utils.get_years(local-dt)
    url = f"{base_url}&targetTime={years}&hitYear={years}"
    return utils.get_ranks(url, "td.subject [title]", parser)
