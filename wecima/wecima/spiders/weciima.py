import scrapy
import time

class WeciimaSpider(scrapy.Spider):
    name = "weciima"
    # allowed_domains = ["weciimaa.online"]
    start_urls = ["https://weciimaa.online/download-series/?page_number=1/"]

    def parse(self, response):
        for item in response.css('div.Thumb--GridItem') :
            yield {
                "title":item.css('strong.hasyear::text').get(),
                "url":item.css('div.Thumb--GridItem a::attr(href)').get()

            }
            time.sleep(1)
        
        next_page = response.css('.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)