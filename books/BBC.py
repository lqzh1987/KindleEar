#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return BBC

class BBC(BaseFeedBook):
    title                 = 'BBC'
    description           = ''
    language              = 'zh-Hans'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_BBC.gif"
    coverfile             = "cv_BBC.jpg"
    deliver_days          = ['']
    deliver_times = [8,11,18]
    remove_classes = ['ec-messages',]
    feeds = [
	    (u'BBC��������ҳ', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'BBC����������', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Fworld%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'BBC�����ڲƾ�', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Fbusiness%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'BBC���Ƽ�����', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Fscience%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
        (u'BBC��ͼ��', 'http://lqzh.esy.es/makefulltextfeed.php?url=feeds.bbci.co.uk%2Fzhongwen%2Fsimp%2Ftopics%2Fpicture_gallery%2Frss.xml&max=50&links=preserve&exc=&submit=Create+Feed'),
                               ]
    
    #������������վ��û���ṩRSSǰ��ץȡ��ʽ�������Ѿ�����Ҫ�ˣ���Ϊֱ����RSSԴ��
    """
    feeds = [
            ('Index', 'http://www.economist.com/printedition'),
           ]
    
    def ParseFeedUrls(self):
        #return list like [(section,title,url,desc),..]
        mainurl = 'http://www.economist.com/printedition'
        urls = []
        urladded = set()
        opener = URLOpener(self.host, timeout=30)
        result = opener.open(mainurl)
        if result.status_code != 200:
            self.log.warn('fetch rss failed:%s'%mainurl)
            return []
            
        content = result.content.decode(self.feed_encoding)
        soup = BeautifulSoup(content, "lxml")
        
        #GAE��ȡ�������ƶ�����ҳ����PC��ȡ������ҳ��Щ��һ��
        for section in soup.find_all('section', attrs={'id':lambda x: x and 'section' in x}):
            h4 = section.find('h4')
            if h4 is None:
                self.log.warn('h4 is empty')
                continue
            sectitle = string_of_tag(h4).strip()
            if not sectitle:
                self.log.warn('h4 string is empty')
                continue
            #self.log.info('Found section: %s' % section_title)
            articles = []
            subsection = ''
            for node in section.find_all('article'):
                subsec = node.find('h5')
                if subsec:
                    subsection = string_of_tag(subsec)
                prefix = (subsection + ': ') if subsection else ''
                a = node.find('a', attrs={"href":True}, recursive=False)
                if a:
                    url = a['href']
                    if url.startswith(r'/'):
                        url = 'http://www.economist.com' + url
                    url += '/print'
                    title = string_of_tag(a)
                    if title:
                        title = prefix + title
                        #self.log.info('\tFound article:%s' % title)
                        if url not in urladded:
                            urls.append((sectitle,title,url,None))
                            urladded.add(url)
                            
        #��Щ�˻�ȡ������PC����ҳ�����ˣ��ٷ���һ��PC����ҳ��  
        if len(urls) == 0:
            for section in soup.find_all('div', attrs={'id':lambda x: x and 'section' in x}):
                h4 = section.find('h4')
                if h4 is None:
                    self.log.warn('h4 is empty')
                    continue
                sectitle = string_of_tag(h4).strip()
                if not sectitle:
                    self.log.warn('h4 string is empty')
                    continue
                
                articles = []
                subsection = ''
                for node in section.find_all('div', attrs={'class':'article'}):
                    subsec = node.previous_sibling
                    if subsec and subsec.name == 'h5':
                        subsection = string_of_tag(subsec)
                    prefix = (subsection + ': ') if subsection else ''
                    a = node.find('a', attrs={'class':'node-link',"href":True}, recursive=False)
                    if a:
                        url = a['href']
                        if url.startswith(r'/'):
                            url = 'http://www.economist.com' + url
                        url += '/print'
                        title = string_of_tag(a)
                        if title:
                            title = prefix + title
                            #self.log.info('\tFound article:%s' % title)
                            if url not in urladded:
                                urls.append((sectitle,title,url,None))
                                urladded.add(url)
                                
        if len(urls) == 0:
            self.log.warn('len of urls is zero.')
        return urls
        """