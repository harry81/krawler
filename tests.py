import unittest
from water import naver


class TestStringMethods(unittest.TestCase):

    def test_cafe_25756108(self):
        naver.cafe(clubid='25756108')

    def test_cafe_10050146(self):
        res = naver.cafe(clubid='10050146')
        print(res)


if __name__ == '__main__':
    unittest.main()
