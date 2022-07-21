# import scrapy
from scrapy.crawler import CrawlerProcess
# from emailscrapy.emailscrapy.spiders import EmailSpider
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl('EmailSpider')
process.start()
