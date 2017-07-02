from Alfred import Alfred
from Item import Item
from bs4 import BeautifulSoup
import requests

class Post:
    def __init__(self, tag):
        self._archive = tag.find('a', class_='archive-title')
        self.title = self._archive['title']
        self.href = self._archive['href']
        self.excerpt = tag.find('span', class_='excerpt').find('p').string


alf = Alfred()
if alf.get_arg_len() < 1:
    categories = ['blog', 'python', 'web', 'android', 'ios']
    [alf.add_item(Item(c, auto_complete=c, icon='mobileicon.png', valid=False)) for c in categories]
else:
    category = alf.get_arg(0)
    resp = requests.get('http://{}.jobbole.com/all-posts/'.format(category))
    soup = BeautifulSoup(resp.text, 'html.parser')
    tags = soup.find('div', id='archive').find_all('div', class_='post-meta')
    posts = [Post(tag) for tag in tags]
    [alf.add_item(Item(p.title, sub_title=p.excerpt, arg=p.href, icon='mobileicon.png')) for p in posts]
alf.show()