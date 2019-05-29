import unittest
from water import naver


class TestStringMethods(unittest.TestCase):

    def test_simple(self):
        self.assertEqual('foo'.upper(), 'FOO')
        from naver_api.naver_search import Naver
        naver = Naver()

        rows = naver.search()
        row = rows[0]
        for row in rows:
            print(row)

    def test_search(self):
        naver.search(category='book', query='영등포')

    def test_cafe(self):
        naver.cafe(clubid='25756108')


if __name__ == '__main__':
    unittest.main()
