from fundus.publishers.base_objects import Publisher, PublisherGroup
from fundus.publishers.cz.seznamzpravy import SeznamZpravyParser
from fundus.publishers.cz.denik import DenikParser
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
    
    Denik = Publisher(
        name="Denik",
        domain="https://www.denik.cz/",
        parser=DenikParser,
        sources=[
            RSSFeed("https://www.denik.cz/rss/zpravy.html"),
            RSSFeed("https://www.denik.cz/rss/podnikani.html"),
            RSSFeed("https://www.denik.cz/rss/sport.html"),
            RSSFeed("https://www.denik.cz/rss/nazory.html"),
            RSSFeed("https://www.denik.cz/rss/magazin.html"),
            Sitemap("https://www.denik.cz/sitemap.xml"),
            NewsMap("https://www.denik.cz/sitemaps/news.html"),
        ],
    )
