from lxml import html
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from datetime import datetime
import requests


class Naver(object):

    def __init__(self, clubid=10050146, userDisplay=50):
        query_dict = {
            "search.clubid": 10050146,
            "search.boardtype": "L",
            "search.specialmenutype": "",
            "search.questionTab": "A",
            "search.totalCount": 401,
            "search.page": 1,
            "userDisplay": userDisplay
        }

        qs = urlencode(query_dict)
        self.url = "http://cafe.naver.com/ArticleList.nhn?%s" % qs

    def search(self):
        rst = []
        page = requests.get(self.url)
        tree = html.fromstring(page.content.decode('cp949', 'ignore'))

        now = datetime.now()

        for tr in tree.xpath('//form[@name="ArticleList"]/table/tr'):
            td = tr.xpath('td')
            if len(td) < 2:
                continue

            article_time = td[3].xpath('text()')[0].replace('\r\n', '').strip().split(':')
            ele = dict(
                id=td[0].xpath('span//text()')[0],
                title=td[1].xpath('span/span/a/text()')[0],
                username=td[2].xpath('div//td/a/span/text()')[0],
                created_at=now.replace(
                    hour=int(article_time[0]),
                    minute=int(article_time[1])).strftime("%Y-%m-%d %H:%M:%S")
            )
            rst.append(ele)

        return rst
