"""Parse ranks from Melon Music Chart."""
import requests
from bs4 import BeautifulSoup


def realtime():
    """Get latest real-time ranks."""
    # Get HTML document.
    url = "https://www.melon.com/chart/index.htm"
    headers = {
        "User-Agent": "mochart/0.0.1",
    }
    resp = requests.get(url, headers=headers)

    # Parse HTML.
    html_doc = resp.text
    soup = BeautifulSoup(html_doc, "html.parser")
    table = soup.table

    # These are in order.
    titles = [link.text for link in table.select("div.ellipsis.rank01 > span > a")]
    artists = [link.text for link in table.select("div.ellipsis.rank02 > span > a")]
    albums = [link.text for link in table.select("div.ellipsis.rank02 > a")]

    return [
        {"title": title, "artist": artist, "album": album}
        for title, artist, album in zip(titles, artists, albums)
    ]
