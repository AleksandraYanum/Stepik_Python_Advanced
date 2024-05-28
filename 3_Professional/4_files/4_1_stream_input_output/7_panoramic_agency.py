import sys


DIVIDER = '/'
LINE_IDX = 0
CATEGORY_IDX = 1
RELIABILITY_IDX = -1
LINE_IDX = 0


def main():

    news = [list(map(str.strip, line.split(DIVIDER))) for line in sys.stdin]

    needed_category = news.pop()[0]
    category_news = [one_news_info for one_news_info in news if one_news_info[CATEGORY_IDX] == needed_category]

    for news in sorted(category_news, key=lambda x: (float(x[RELIABILITY_IDX]), x[LINE_IDX])):
        print(news[LINE_IDX])


main()