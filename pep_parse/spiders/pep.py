import scrapy

from pep_parse.items import PepParseItem
from settings import URL_LIST


class PepSpider(scrapy.Spider):
    name = 'pep'

    start_urls = URL_LIST
    allowed_domains = URL_LIST

    def parse(self, response):
        pep_hrefs = response.css(
            'section[id=numerical-index] tr td:nth-child(2) a::attr(href)'
        ).getall()
        for link in pep_hrefs:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = (
            response.css('h1.page-title::text').get().split(' – ', 1)
        )
        pep_data = {
            'number': number.split()[1],
            'name': name,
            'status': response.css('dt:contains("Status") + dd::text').get(),
        }
        yield PepParseItem(pep_data)
