import json
import os
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def find_companies(company_name: str) -> {}:
    # set up WebDriver and query website
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://www.marketwatch.com/search?q=' + company_name + '&ts=0&tab=All%20News'
    driver.get(url)
    html = driver.page_source
    driver.close()

    # scrape website
    result = {'Search': company_name}
    soup = BeautifulSoup(html, 'lxml')
    categories = soup.find_all('div', {'class': 'ticker__set'})
    for category in categories:  # either 'Symbols' or 'Private Company'
        loading = category.find('div', {'class': 'loading', 'style': 'display: none;'})
        if loading is None:
            continue
        c = category.find('span', {'class': 'header__text'})
        # scrape public companies
        if c.getText().strip('\n') == 'Symbols':
            symbols = []
            table_rows = category.find_all('td')
            for table_row in table_rows:
                company_result = {}
                symbol = table_row.find('span', {'class': 'symbol j-symbol'})
                if symbol is not None:
                    company_result['Symbol'] = symbol.getText().strip('\n')
                name = table_row.find('small', {'class': 'company j-company'})
                if name is not None:
                    company_result['Name'] = name.getText().strip('\n')
                links = table_row.find_all('a', href=True)
                for link in links:
                    company_result['Link'] = 'https://www.marketwatch.com' + link['href']
                if bool(company_result):
                    print(f'Found public company for \"{company_name}\"')
                    symbols.append(company_result)
            result['Public Companies'] = symbols
        # scrape private companies
        elif c.getText().strip('\n') == 'Private Companies':
            symbols = []
            table_rows = category.find_all('td')
            for table_row in table_rows:
                company_result = {}
                name = table_row.find('span', {'class': 'symbol j-symbol'})
                if name is not None:
                    company_result['name'] = name.getText().strip('\n')
                links = table_row.find_all('a', href=True)
                for link in links:
                    company_result['Link'] = 'https://www.marketwatch.com' + link['href']
                if bool(company_result):
                    print(f'Found private company for \"{company_name}\"')
                    symbols.append(company_result)
            result['Private Companies'] = symbols
    return result


if __name__ == '__main__':
    results = []
    for company in sys.argv[1:]:
        results.append(find_companies(company))
    with open(f'{os.getcwd()}/companies.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=True, indent=3)
    print(f'\nFind the results in \"{os.getcwd()}/companies.json\"')
