import requests
from bs4 import BeautifulSoup
from pack.headers import headers


def get_ip():
    url = 'https://2ip.ru'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    ip = soup.find('div', class_='ip').text.strip()
    country = soup.find('div', class_='value-country').text.split("  ")[0].strip()

    return ip, country


def get_status_website(url):
    response = requests.get(url=url, headers=headers).status_code
    return response


if __name__ == "__main__":
    get_ip()
    get_status_website('https://2ip.ru')


