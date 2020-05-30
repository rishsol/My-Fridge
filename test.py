from bs4 import BeautifulSoup
import copy
from tkcalendar import DateEntry

with open('templates/new_item.html') as f:
    contents = f.read()

with open('templates/home.html') as g:
    homecontents =  g.read()

soup = BeautifulSoup(homecontents, 'lxml')

print(DateEntry())