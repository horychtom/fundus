import datetime
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


class DenikParser(ParserProxy):
    class V1(BaseParser):
        _paragraph_selector = XPath(
            "//main/div[contains(@class,'article-body')]/p[not(.//img)]")
        _summary_selector = XPath("//main//div/p[contains(@class, 'ac-perex')]")
        _subheadline_selector = XPath(
            "//main/div[contains(@class,'article-body')]/h2"
        )
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
                image_selector = XPath("//div/a/img"),
                # TODO add author selector
                #author_selector=re.compile(r"Foto: (?P<credits>.+)"),
                relative_urls=True,
            )