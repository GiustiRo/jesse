"""Probe public HistData M1 download navigation; no account or credentials.

Only prints page titles, HTTP status, and public SPX/year links. It neither
imports data nor treats a download page as evidence of complete history.
"""
import re
from html.parser import HTMLParser
from urllib.parse import urljoin
import requests
import jesse.models  # Initialize store before standalone jh.debug logging.
from jesse import helpers as jh


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])


s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0'
url = 'https://www.histdata.com/download-free-forex-data/'
for stage in range(4):
    r = s.get(url, timeout=(10, 35))
    r.raise_for_status()
    p = Links()
    p.feed(r.text)
    title = re.search(r'<title>(.*?)</title>', r.text, re.S)
    jh.debug({'stage': stage, 'status': r.status_code, 'url': r.url,
              'title': title.group(1) if title else None})
    if stage == 0:
        candidates = [h for h in p.links if 'ascii' in h.lower() and '1-minute' in h.lower()]
    elif stage == 1:
        candidates = [h for h in p.links if 'spxusd' in h.lower()]
    elif stage == 2:
        candidates = [h for h in p.links if re.search(r'/202[0-5](?:/|$|[?])', h)]
        candidates = [h for h in candidates if '/spxusd/2020' in h.lower()]
    else:
        jh.debug({'download_links': p.links[:30]})
        jh.debug({'forms_and_inputs': re.findall(r'<(?:form|input)[^>]+>', r.text)})
        break
    if not candidates:
        jh.debug({'no_candidate_links': p.links[:20]})
        break
    url = urljoin(r.url, candidates[0])
