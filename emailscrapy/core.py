# import scrapy
from scrapy.crawler import CrawlerProcess
from emailscrapy.emailscrapy.spiders import EmailSpider
from scrapy.utils.project import get_project_settings

# process = CrawlerProcess(get_project_settings())
# process.crawl('EmailSpider')
# process.start()
def main(return_results=False, parse_cmd_line=True, config_from_dict=None):
        if parse_cmd_line:
        cmd_line_args = get_command_line()