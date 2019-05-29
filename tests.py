import unittest


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
        from water import naver
        naver.search(category='book', query='영등포')


if __name__ == '__main__':
    unittest.main()
