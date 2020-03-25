import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html,'lxml')

    links = soup.find('table', id='currencies-all').find_all('td',class_='currency-name')
 
def main():
    #https://coinmarketcap.com/all/views/all/
    
    all_links = []



if __name__ == '__main__':
    main()
