from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.dr-chuck.com/page1.htm').read()
soup = BeautifulSoup(r)

print(soup.prettify()[0:1000])
