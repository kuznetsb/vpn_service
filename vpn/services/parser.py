from urllib.parse import urlparse

from bs4 import BeautifulSoup
from requests import Response

from vpn_service.settings import SITE_URL, DJANGO_PORT


class HTMLParser:
    def __init__(self, response: Response):
        self.origin_url = response.url
        self.text = response.text

    def change_routing(self):
        soup = BeautifulSoup(self.text, "html.parser")
        domain = urlparse(self.origin_url).netloc
        same_site_links = list(
            filter(
                lambda x: domain == urlparse(x["href"]).netloc,
                soup.findAll("a", href=True),
            )
        )
        for link in same_site_links:
            link["href"] = f"{SITE_URL}:{DJANGO_PORT}/vpn/{link['href']}"
        return soup
