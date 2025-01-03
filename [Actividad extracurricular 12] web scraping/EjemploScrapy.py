
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'Quote': quote.css('span.text::text').get(),
                'Author': quote.css('small.author::text').get()
            }
