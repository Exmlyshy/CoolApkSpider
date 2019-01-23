# -*- coding: utf-8 -*-

# Scrapy settings for coolapkuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'coolapkuser'

SPIDER_MODULES = ['coolapkuser.spiders']
NEWSPIDER_MODULE = 'coolapkuser.spiders'

MONGO_URI = 'localhost'
MONGO_DB = 'coolapk'
MONGO_TABLE = 'user'

REDIS_URI = 'localhost'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'coolapkuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; PRO 6 Plus Build/LMY48Z) (#Build; Meizu; PRO 6 Plus; Meizu-user 5.1.1 20171130.276299 release-keys; 5.1.1) +CoolMarket/8.9',
    'x-requested-with': 'XMLHttpRequest',
    'x-sdk-int': '22',
    'x-sdk-locale': 'zh-CN',
    'x-app-id': 'com.coolapk.market',
    'x-app-token': '',
    'x-app-version': '8.9',
    'x-app-code': '1812182',
    'x-api-version': '8',
    'x-app-device': 'MXdsBFI2AyTSBFI7UnepVWTgsTd6lWZNByOwAjOwAjOwAjOwAjOwAjOyADI7ATN3YTOyQDN1IDMwAjN0AyO1ETMwUzMxUzMyUDO5YDOgsTNxgDOzETOxQTN0ATN0AzN',
    'accept-encoding': 'gzip',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'coolapkuser.middlewares.CoolapkuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'coolapkuser.middlewares.CloseMiddlerWare': 542,
    'coolapkuser.middlewares.TokenMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'coolapkuser.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
