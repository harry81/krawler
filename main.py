from naver_search import Naver

if __name__ == '__main__':
    naver = Naver(userDisplay=50)
    rst = naver.search()

    for ele in rst:
        print(ele['title'])
