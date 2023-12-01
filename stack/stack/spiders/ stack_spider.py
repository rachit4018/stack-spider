from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem
class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//*[@id="questions"]')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                '//*[@id="questions"]/div[1]/div[2]/h3/a/text()').extract()[0]
            item['url'] = question.xpath(
                '//*[@id="questions"]/div[1]/div[2]/h3/a/@href').extract()[0]
            yield item