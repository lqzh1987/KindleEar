 #!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return BBC

class BBC(BaseFeedBook):
    title                 = u'BBC新闻'
    description           = u'BBC新闻。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_BBC.gif"
    coverfile             = "cv_BBC.jpg"
	deliver_times         = [8,11,18]
    oldest_article        = 1
    
    feeds = [
        (u'BBC：新闻主页', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'BBC：国际新闻', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Fworld%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'BBC：金融财经', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Fbusiness%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'BBC：科技健康', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Fscience%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'BBC：图集', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Ftopics%2Fpicture_gallery%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
            ]
      
