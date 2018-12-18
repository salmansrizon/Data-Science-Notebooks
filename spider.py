import scrapy
from scrapy import Request


class MultipleQuotesSpider(scrapy.Spider):
    name = "multiple-quotes"
    allowed_domains = ["pickaboo.com"]
    start_urls = ['https://www.pickaboo.com/mobile-tablet.html/']

    def parse(self, response):
        product_title = response.css('h2.product-name.newname>a::text').extract()
        if response.css('.regular-price'):
            Current_price = response.css('span::attr(content)').extract()
        else:
            return 0

        # li_tag = response.xpath("//li[contains(concat(' ', @class, ' '), ' old-price ')]")
        # if li_tag: 
        #     old_price = response.css('div.price-box>p.old-price>span.price::text').extract()
        #     pass
        # else:
        #     return None
             



        for item in zip(product_title,Current_price):

            info = {
                'Product Name' : item[0],
                'Current Price' : item[1],
                # 'Old Price': item[2]
            }

            yield info

        next_page_url = response.css('a.next::attr(href)').extract_first()
        yield scrapy.Request(url = next_page_url, callback=self.parse)