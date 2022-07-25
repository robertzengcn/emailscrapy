import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
import tldextract
import logging
from emailscrapy.emailscrapy.items import EmailscrapyItem
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dns.resolver import query

logger = logging.getLogger(__name__)



class EmailSpider(CrawlSpider):
    name = 'email_spider'
    # allowed_domains = ['clever-lichterman-044f16.netlify.com']
    # start_urls = [f'{url}']
    allowed_domains = []
    rules = (
        Rule(LinkExtractor(deny=('product','item','login','category')),callback='parse_page'),
    )

    def __init__(self, url='', **kwargs):
        self.start_urls = [f"{url}"]
        self.initurl = f"{url}"
        logger.info(self.start_urls)
        ext = tldextract.extract(url)
        # logger.info("the domain is {}".format(ext))
        self.allowed_domains.append(ext.registered_domain)
        logger.info(self.allowed_domains)
        self.email_list = []
        super().__init__(**kwargs)

    # sending requests
    # def start_requests(self):
    #     yield SeleniumRequest(
    #             url=self.initurl,
    #             callback=self.parse_page,
    #             wait_until=EC.presence_of_element_located(
    #                 (By.TAG_NAME, "html")),
    #             dont_filter=True
    #         )
    def parse_start_url(self, response):
        logger.info("open selenium request")
        yield SeleniumRequest(
            url=self.initurl,
            callback=self.parse_page,
            wait_time=15,
            wait_until=EC.presence_of_element_located(
                (By.TAG_NAME, "html")),
            dont_filter=True
        )

    # parse the page

    def parse_page(self, response):
        logger.info("start parse...")
        EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.finditer(EMAIL_REGEX, str(response.text))
        for email in emails:
            domain =email.group().rsplit('@', 1)[-1]
            res=False
            try:
                res=bool(query(domain, 'MX'))
            except:
                continue
            if res:
                item = EmailscrapyItem()
                item['url'] = response.url
                item['email'] = email.group()
                item['description'] = response.css('title::text').get()
                logger.info(item)
                return item
            
        # for email in set(self.email_list):
        #     yield{
        #         "emails": email
        #     }

        # self.email_list.clear()
