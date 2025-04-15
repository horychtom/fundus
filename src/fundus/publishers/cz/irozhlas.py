import datetime
import re
from typing import List, Optional

from lxml.etree import XPath

from fundus.parser import (
    ArticleBody,
    BaseParser,
    Image,
    ParserProxy,
    attribute,
)
from fundus.parser.utility import (
    extract_article_body_with_selector,
    generic_author_parsing,
    generic_date_parsing,
    image_extraction,
)


class iRozhlasParser(ParserProxy):
    class V1(BaseParser):
        _paragraph_selector = XPath(
            "//article//div[@class='b-detail']/p[not(contains(@class, 'meta'))]"
        )
        _summary_selector = XPath("//header/*[self::p or self::ul][contains(@class, 'text-lg')]")
        # TODO: interview articles have p > strong as sort of headlines, add them
        _subheadline_selector = XPath("//article//div[@class='b-detail']//h2")

        @attribute
        def body(self) -> Optional[ArticleBody]:
            return extract_article_body_with_selector(
                self.precomputed.doc,
                summary_selector=self._summary_selector,
                subheadline_selector=self._subheadline_selector,
                paragraph_selector=self._paragraph_selector,
            )

        @attribute
        def publishing_date(self) -> Optional[datetime.datetime]:
            return generic_date_parsing(
                self.precomputed.ld.bf_search("datePublished")
            )

        @attribute
        def title(self) -> Optional[str]:
            return self.precomputed.ld.bf_search("headline")

        @attribute
        def authors(self) -> List[str]:
            return (
                generic_author_parsing(
                    self.precomputed.ld.bf_search("author")
                ),
            )

        @attribute
        def images(self) -> List[Image]:
            # TODO width extraction doesnt work
            return image_extraction(
                doc=self.precomputed.doc,
                paragraph_selector=self._paragraph_selector,
                author_selector=re.compile(r"Foto: (?P<credits>.+)"),
                relative_urls=True,
            )
