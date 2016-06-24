#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return lutou

class lutou(BaseFeedBook):
    title                 = u'路透社'
    description           = u'路透社新闻。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_lutou.gif"
    coverfile             = "cv_lutou.jpg"
	deliver_times         = [8,11,18]
    oldest_article        = 1
    
    feeds = [
        (u'路透：中国财经', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FchinaNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：深度分析', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FCNAnalysesNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：国际财经', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FCNIntlBizNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：时事要闻', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FCNTopGenNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：财经报道', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FcnBizNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：投资资讯', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FcnInvNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：公司新闻', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FcompanyNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：市场报道', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FcnMktNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：外汇', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FcurrenciesNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'路透：产业', 'http://lqzh.esy.es/makefulltextfeed.php?url=cn.reuters.com%2FrssFeed%2FindustryNews%2F&max=50&links=preserve&exc=&submit=Create+Feed'),
            ]
