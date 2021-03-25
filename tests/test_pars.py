from requests import get
from pars import Parser
from bs4 import BeautifulSoup


def test_connection(check_connect):
    response = get(check_connect[0], headers=check_connect[1])
    assert (response.status_code == 200)


def test_word():
    jobs = Parser('дробовик')
    info = jobs.vacancies_pars('')
    assert (info == 0)


def test_words_in():
    words_in = ['python', 'linux', 'flask']
    jobs = Parser('python')
    info = jobs.vacancies_pars(words_in)
    words_d = {'python': 58, 'linux': 16.8, 'flask': 4}
    check = True
    for i in info[1]:
        for j in i:
            words = i[j]
            for w in words:
                if int(words[w]) == 0 or w == 'all_vacancies':
                    continue
                else:
                    prev = words_d[w]
                    print(prev)
                    if prev - 1 < int(words[w]) / 5 < prev + 1:
                        pass
                    else:
                        check = False
    assert (check == True)


def test_soup(check_connect):
    response = get(check_connect[0], headers=check_connect[1])
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', {'class': 'vacancy-serp-item'})
    assert (results != [])


def test_soup_desc(check_connect):
    link = "https://rabota.by/vacancy/43048095?query=python"
    response = get(link, headers=check_connect[1])
    soup = BeautifulSoup(response.text, 'html.parser').find_all('div', {'class': 'vacancy-description'})
    description_vac = ""
    for s in soup:
        description_vac += s.get_text('\n').lower()
    assert (description_vac != "")
