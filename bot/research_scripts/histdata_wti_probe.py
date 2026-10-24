"""Read-only probe of the public HistData WTI/USD M1 download pages (r49 Fase 2b C3).

Fetches HTML pages only and prints the public file_down form fields. It submits no form
and downloads no archive. Pass the page suffixes to probe, e.g. 2024 2024/1.
"""
import sys

import requests
from html.parser import HTMLParser

BASE = 'https://www.histdata.com'


class DownloadForm(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.fields = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'form':
            self.active = a.get('id') == 'file_down'
        if self.active and tag == 'input' and a.get('name'):
            self.fields[a['name']] = a.get('value', '')

    def handle_endtag(self, tag):
        if tag == 'form':
            self.active = False


def main():
    for suffix in sys.argv[1:] or ['2024']:
        s = requests.Session()
        s.headers.update({'User-Agent': 'Mozilla/5.0'})
        page = f'{BASE}/download-free-forex-historical-data/?/ascii/1-minute-bar-quotes/wtiusd/{suffix}'
        r = s.get(page, timeout=(10, 45))
        f = DownloadForm()
        f.feed(r.text)
        low = r.text.lower()
        print(suffix, r.status_code, 'form:', f.fields, '| no-data hint:',
              [h for h in ('no data', 'not available', 'coming soon', 'too many') if h in low])


if __name__ == '__main__':
    main()
