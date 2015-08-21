from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# html = requests.get('http://www.xuebuyuan.com/2127057.html').content.decode('utf-8')
# print html
# lst = re.findall(r'', html)
url = 'http://www.xuebuyuan.com/2127057.html'
def extract(url):
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text

if __name__ == '__main__':
    print extract(url)
