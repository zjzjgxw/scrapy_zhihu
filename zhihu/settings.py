# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'



COOKIES = 'd_c0="AFDAB_PzVwqPTiB94baqbnVkW66g-D4W8Nc=|1470481112"; _za=3400aa9b-6111-4fe2-bfc7-47197de14be1; _zap=8b5d048d-3bdd-4462-86f7-3ce1a6e4bcd6; aliyungf_tc=AQAAAGlNuDWF7wMAqYVP2piPMVXEybGL; _xsrf=f14b12caef75f0f99d66ab72fc4af559; s-q=%E8%A6%83%E8%B6%85; s-i=1; sid=cngifk3v; __utma=51854390.1141296138.1501078013.1501078013.1505231119.2; __utmc=51854390; __utmz=51854390.1505231119.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20130314=1^3=entry_date=20130314=1; q_c1=c03b3fdc1a154f1e8066f1faefe046e7|1508071459000|1486036952000; q_c1=c03b3fdc1a154f1e8066f1faefe046e7|1516548758000|1486036952000; _xsrf=f14b12caef75f0f99d66ab72fc4af559; l_cap_id="N2NhNWI4N2NkOGYzNGI4NTliN2FhZTcyYjgzY2U2Nzc=|1517149727|86a5925bea36a322d38d631130021cf5449e94df"; r_cap_id="N2EzNzA0MDQ0ZGQ3NGRlYWE3YTY5NThkNzI2MzM2ZDE=|1517149727|e67b21a946d2d307e163b7be12c9aadaa097932c"; cap_id="NzFhNWZlNGY0MzYxNDA0MWJlZDkxMjkyYjExMGFjNGE=|1517149727|ecc1c794a26fe4613b43a94f2b386f0a9c8e1b53"; capsion_ticket="2|1:0|10:1517747841|14:capsion_ticket|44:NDA3NTgzMzQ5ZTRmNGU0Nzk1MTI0MjY0MDVmYmFkZjc=|badbe4bb8d7bd0f86e025a9361c380e64d333dbe353aea3ffc46588a8fcaa39e"; z_c0="2|1:0|10:1517747848|4:z_c0|92:Mi4xUmVBSUFBQUFBQUFBVU1BSDhfTlhDaVlBQUFCZ0FsVk5oMHhrV3dCOHM3NWhhLTdaWDNoU1dIVzBwcUZqangyZldR|02e96caac61775a2d86100496f52a1e7f03d464dc95f801c58ee6817b3f08cc4"'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Connection': 'keep - alive',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihu.pipelines.ZhihuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
