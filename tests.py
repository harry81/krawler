import unittest
from water import naver, hani


class TestStringMethods(unittest.TestCase):

    def test_cafe_25756108(self):
        naver.cafe(clubid='25756108')

    def test_cafe_10050146(self):
        res = naver.cafe(clubid='10050146')
        print(res)


class TestHani(unittest.TestCase):

    def test_get_hrefs(self):
        hrefs = hani.get_hrefs()
        self.assertIsInstance(hrefs[0], str)

    def test_extract(self):
        hrefs = hani.get_hrefs()

        print(len(hrefs))

        for href in hrefs[:40]:
            article = hani.extract(href)
            print(article['title'], article['register'], article['url'])

        self.assertIsInstance(article['title'], str)


if __name__ == '__main__':
    unittest.main()
