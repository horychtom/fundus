from fundus.publishers.base_objects import Publisher, PublisherGroup
from fundus.publishers.cz.seznamzpravy import SeznamZpravyParser
from fundus.publishers.cz.irozhlas import iRozhlasParser
from fundus.scraping.url import NewsMap, RSSFeed, Sitemap


class CZ(metaclass=PublisherGroup):
    SeznamZpravy = Publisher(
        name="SeznamZpravy",
        domain="https://seznamzpravy.cz/",
        parser=SeznamZpravyParser,
        sources=[
            RSSFeed("https://www.seznamzpravy.cz/rss"),
            Sitemap("https://www.seznamzpravy.cz/sitemaps/sitemap_articles.xml"),
            NewsMap("https://www.seznamzpravy.cz/sitemaps/sitemap_news.xml"),
        ],
    )
    iRozhlas = Publisher(
        name="iRozhlas",
        domain="https://www.irozhlas.cz/",
        parser=iRozhlasParser,
        sources=[
            RSSFeed("https://www.irozhlas.cz/rss/irozhlas"),
            Sitemap("https://www.irozhlas.cz/sites/default/files/irozhlas_feeds/sitemaps/sitemap-index.xml"),
            NewsMap("https://www.irozhlas.cz/sites/default/files/irozhlas_feeds/sitemaps/news.xml"),
        ],
    )
    
