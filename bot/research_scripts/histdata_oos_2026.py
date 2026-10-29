"""Inspect the authorized 2026 HistData SPX archive without importing candles.

Use the existing research environment and downloader parser. Do not read credentials
or contact trading accounts. Probe only the public data pages and disclose coverage.
"""
import json
import sys
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import requests
import jesse.models
from jesse import helpers as jh
from histdata_download import BASE, DownloadForm


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_data(self, data):
        self.text.append(data)


def main():
    if sys.version_info < (3, 10):
        raise RuntimeError("Jesse requires Python >=3.10")
    jh.debug({"python": sys.version.split()[0], "authorization": "User approved 2026 downloader and import"})
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    page = BASE + "/download-free-forex-historical-data/?/ascii/1-minute-bar-quotes/spxusd/2026"
    response = session.get(page, timeout=(10, 45))
    response.raise_for_status()
    parsed = urlparse(response.url)
    if parsed.hostname != "www.histdata.com":
        raise ValueError("Unexpected provider redirect")
    form, links = DownloadForm(), Links()
    form.feed(response.text)
    links.feed(response.text)
    relevant = sorted({urljoin(response.url, href) for href in links.links
                       if "spxusd" in href.lower()})
    jh.debug(json.dumps({"page": response.url, "status": response.status_code,
                         "form_action": form.action,
                         "form_metadata": {k: form.fields.get(k) for k in ("fxpair", "timeframe", "platform", "date", "datemonth")},
                         "links_2026": relevant, "all_links": links.links[:100],
                         "visible_text": " ".join(" ".join(links.text).split())[-11000:], "text_length": len(response.text), "page_title": response.text[response.text.find("<title>"):response.text.find("</title>")+8]}))


if __name__ == "__main__":
    main()
