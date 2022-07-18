##Project for scrapy email from web
Give a url, then the program will start a spider to scrawl the site, and grap email

Consider for the email locate at dynamic websites,the program will start a SeleniumRequest to open the url, but for the reason of efficiency, we will not use selenium to craw the whole dynamic web


##Installation
email scrapy is written in python3,You can also install it comfortably with pip
```
virtualenv --python python3 env
source env/bin/activate
```
## run spider
```
scrapy crawl email_spider -a url=https://www.example.com
```

you can save the result to json file by use follow command
```
scrapy crawl email_spider -a url=https://www.example.com -o email.json
```


