import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
import tldextract
import logging

logger = logging.getLogger(__name__)

class EmailSpider(CrawlSpider):
    name = 'email_crawl_spider'
    # allowed_domains = ['clever-lichterman-044f16.netlify.com']
    # start_urls = [f'{url}']

    rules = (   
        Rule(LinkExtractor(allow=('products', )), callback='parse_page'),
    )

    def __init__(self,url='',**kwargs):
        self.start_urls= [f"{url}"]
        ext =tldextract.extract(url)
        self.allowed_domains.append(ext.domain)
        self.email_list = []
        super().__init__(**kwargs)

    # parse the page 
    def parse_page(self, response):
        EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.finditer(EMAIL_REGEX, str(response.text))
        for email in emails:
            self.email_list.append(email.group())

        for email in set(self.email_list):
            yield{
                "emails": email
            }
 
        self.email_list.clear()