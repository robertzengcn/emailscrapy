import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from emailscrapy.commandline import get_command_line
import random
import string
from emailscrapy.emailscrapy.spiders.emailspider import EmailSpider
import validators

class WrongConfigurationError(Exception):
    pass

# process = CrawlerProcess(get_project_settings())
# process.crawl('EmailSpider')
# process.start()


def main(return_results=False, parse_cmd_line=True, config_from_dict=None):
    if parse_cmd_line:
        cmd_line_args = get_command_line()
        url = cmd_line_args.get('url')
        if (url is None):
            raise WrongConfigurationError('the url is empty')
        # check url valid
        valid=validators.url(url)
        if valid!=True:
           raise WrongConfigurationError('you not input the correct url')     
        outfile = cmd_line_args.get('output_filename')
        
        if(outfile is None or len(outfile) < 1):
            outfile = ''.join(random.choices(
                string.ascii_lowercase, k=32))+".json"

        SETTINGS = {
            "FEEDS": {
                outfile: {"format": "json"},
            }
        }
        process = CrawlerProcess(SETTINGS)
        process.crawl(EmailSpider, url=url)
        process.start()
