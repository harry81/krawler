import unittest
from water import naver
from water.krawler import Chosun, Hani, Frip, BR, KakaoBook, NaverBook


class TestBR(unittest.TestCase):

    def test_get_hrefs(self):
        br = BR()

    def test_parser(self):
        br = BR(limit=15)
        for idx, href in enumerate(br.hrefs):
            article = br.article(idx)
            print(article['title'])


class TestFrip(unittest.TestCase):

    def test_base(self):
        frip = Frip()
        res = frip.extract(perPage=100)

        for ele in [ele for ele in res['products'] if ele['rating'] > 4]:
            print("{title} {price} {rating}".format(**ele))


class TestStringMethods(unittest.TestCase):

    def test_cafe_25756108(self):
        naver.cafe(clubid='25756108')

    def test_cafe_10050146(self):
        res = naver.cafe(clubid='10050146')
        print(res)


class TestChosun(unittest.TestCase):

    def test_get_hrefs(self):
        chosun = Chosun()
        self.assertEqual(10, len(chosun.hrefs))

    def test_parser(self):
        chosun = Chosun()
        article = chosun.article()

        self.assertIsInstance(article['title'], str)


class TestHani(unittest.TestCase):

    def test_get_hrefs(self):
        hani = Hani()
        self.assertIn('html', hani.hrefs[0])

    def test_extract(self):
        hani = Hani()
        article = hani.article()
        self.assertIsInstance(article['title'], str)


class TestKakaoBook(unittest.TestCase):

    def test_get_hrefs(self):
        kakao = KakaoBook()
        res = kakao.search(query="용기")
        self.assertTrue(len(res.json()['documents']) > 10)


class TestNaverBook(unittest.TestCase):

    def test_search(self):
        naver = NaverBook()
        res = naver.search(query="노트북")
        self.assertTrue(len(res.json()['items']) > 5)

    def test_search_isbn(self):
        naver = NaverBook()
        res = naver.search(query="8975601994 9788975601996")
        self.assertTrue(len(res.json()['items']) == 1)


if __name__ == '__main__':
    unittest.main()
