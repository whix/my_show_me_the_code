from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


url = 'http://www.ruanyifeng.com/blog/2015/07/monad.html'
def extract(url):
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.links

if __name__ == '__main__':
    print extract(url)
