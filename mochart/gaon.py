from mochart import utils


def parser(rows):
    """Parse texts accordingly from Gaon table."""
    values = []
    titles = map(
        lambda t: t[1].text,
        filter(lambda x: x[0] % 2 == 0, enumerate(rows))
    )
    artists = map(
        lambda t: t[1].text.split("|")[0],
        filter(lambda x: x[0] % 2 != 0, enumerate(rows))
    )
    albums = map(
        lambda t: t[1].text.split("|")[1],
        filter(lambda x: x[0] % 2 != 0, enumerate(rows))
    )
    return [
        {"title": title, "artist": artist, "album": album}
        for title, artist, album in zip(titles, artists, albums)
    ]


def week(day_time=None):
    base_url = "http://www.gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=week"
    weeks = utils.get_weeks(day_time)
    years = utils.get_years(day_time)
    url = f"{base_url}&targetTime={weeks}&hitYear={years}"
    return utils.get_ranks(url, "td.subject [title]", parser)


def month(day_time=None):
    base_url = "http://www.gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=month"
    months = utils.get_months(day_time)
    years = utils.get_years(day_time)
    url = f"{base_url}&targetTime={months}&hitYear={years}"
    return utils.get_ranks(url, "td.subject [title]", parser)


def year(day_time=None):
    base_url = "http://www.gaonchart.co.kr/main/section/chart/online.gaon?nationGbn=T&serviceGbn=ALL&termGbn=year"
    years = utils.get_years(day_time)
    url = f"{base_url}&targetTime={years}&hitYear={years}"
    return utils.get_ranks(url, "td.subject [title]", parser)
