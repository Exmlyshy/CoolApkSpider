# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    uid = scrapy.Field()
    username = scrapy.Field()
    admintype = scrapy.Field()
    groupid = scrapy.Field()
    usergroupid = scrapy.Field()
    level = scrapy.Field()
    status = scrapy.Field()
    usernamestatus = scrapy.Field()
    avatarstatus = scrapy.Field()
    logintime = scrapy.Field()
    entityType = scrapy.Field()
    entityId = scrapy.Field()
    displayUsername = scrapy.Field()
    userAvatar = scrapy.Field()
    groupName = scrapy.Field()
    isBlackList = scrapy.Field()
    isIgnoreList = scrapy.Field()
    isLimitList = scrapy.Field()
    gender = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    bio = scrapy.Field()
    isDeveloper = scrapy.Field()
    verify_status = scrapy.Field()
    apkDevNum = scrapy.Field()
    feed = scrapy.Field()
    follow = scrapy.Field()
    fans = scrapy.Field()
    apkFollowNum = scrapy.Field()
    apkRatingNum = scrapy.Field()
    albumNum = scrapy.Field()
    albumFavNum = scrapy.Field()
    discoveryNum = scrapy.Field()
    replyNum = scrapy.Field()
