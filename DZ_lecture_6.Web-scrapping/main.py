import json

import bs4
import requests

HOST = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/111.0.0.0 Safari/537.36'}
KEYWORDS = ['Django', 'Flask']


def requests_response(host, headers, attrs, name_=None):
    response = requests.get(host, headers=headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, 'html.parser')
    results = soup.find_all(name_, attrs=attrs)
    return results


def get_vacancy_info(vacancys):
    list_vacancys_info = []
    for vacancy in vacancys:
        name = vacancy.find(class_="serp-item__title").text
        link = vacancy.find(class_="serp-item__title")['href']
        salary_fork = vacancy.find('span', class_="bloko-header-section-3")
        if salary_fork is None:
            salary_fork = 'Не указана'
        else:
            salary_fork = salary_fork.text
        company_name = \
            vacancy.find('a', class_="bloko-link bloko-link_kind-tertiary").text
        town = vacancy.find('div', {
            'data-qa': 'vacancy-serp__vacancy-address'}).text.split(',')[0]
        descriptions = requests_response(
            link, HEADERS, {'data-qa': 'vacancy-description'}, 'div'
        )
        for word in KEYWORDS:
            if word in descriptions[0].text and 'USD' in salary_fork:
                list_vacancys_info.append({
                    'Вакансия': name,
                    'Ссылка на описание': link,
                    'Зарплата': salary_fork.replace('\u202f', ' '),
                    'Компания': company_name.replace('\xa0', ' '),
                    'Город': town
                })
    return list_vacancys_info


if __name__ == '__main__':
    list_vacancys = requests_response(
        HOST, HEADERS, {'class': "vacancy-serp-item-body__main-info"}
    )
    vacancy_info = get_vacancy_info(list_vacancys)
    with open('vacancy.json', 'w', encoding='utf-8') as f:
        json.dump(vacancy_info, f, ensure_ascii=False, indent=4)
        print(f'Список из {len(vacancy_info)} вакансий(и) сохранен в файл: '
              f'vacancy.json')
