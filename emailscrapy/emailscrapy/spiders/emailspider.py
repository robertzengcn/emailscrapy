import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
import tldextract
import logging
from emailscrapy.items import EmailscrapyItem
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)
#scrapy crawl email_spider -a url=https://www.flipkart.com/toys-online-store
class EmailSpider(CrawlSpider):
    name = 'email_spider'
    # allowed_domains = ['clever-lichterman-044f16.netlify.com']
    # start_urls = [f'{url}']
    allowed_domains =[]
    rules = (   
        Rule(LinkExtractor(deny=('products'),), callback='parse'),
    )

    def __init__(self,url='',**kwargs):
        self.start_urls= [f"{url}"]
        logger.info(self.start_urls)
        ext =tldextract.extract(url)
        self.allowed_domains.append(ext.domain)
        logger.info(self.allowed_domains)
        self.email_list = []
        super().__init__(**kwargs)  

    # sending requests
    # def start_requests(self):
    #     yield SeleniumRequest(
    #             url=self.url,
    #             callback=self.parse_page,
    #             wait_until=EC.presence_of_element_located(
    #                 (By.TAG_NAME, "html")),
    #             dont_filter=True
    #         )     

    # parse the page 
    def parse(self, response):
        logger.info("start parse...")
        EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.finditer(EMAIL_REGEX, str(response.text))
        for email in emails:
            item = EmailscrapyItem()
            item['url']=response.url
            item['email']=email.group()
            item['title']=response.css('title::text').get()
            logger.info(item)
            return item
            

        # for email in set(self.email_list):
        #     yield{
        #         "emails": email
        #     }
 
        # self.email_list.clear()