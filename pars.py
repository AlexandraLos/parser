from requests import get
from bs4 import BeautifulSoup


class Parser:
    URL = 'https://rabota.by/search/vacancy?clusters=true&text={}&area=1002'
    HEADERS = {'User-Agent': 'Mozilla/5.0'}

    def __init__(self, name_vac):
        self.name_vac = name_vac

    def get_info_vacancies(self, link):
        print(link)
        response = get(link, headers=self.HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser').find_all('div', {'class': 'vacancy-description'})
        description_vacancies = ""
        for s in soup:
            description_vacancies += s.get_text('\n').lower()
        return description_vacancies

    def get_current_vacancy(self, html, words_in):
        link = html.find('a').get('href')
        des_job = self.get_info_vacancies(link)
        k = 0
        w = {}
        for i in words_in:
            w[i] = 0
        for i in des_job.split(' '):
            word = i.replace('\n', '').strip().replace('.', '').replace(',', '').replace(':', '')
            if word in words_in:
                k += 1
            for h in w:
                if h == word:
                    w[h] += 1
        return k, w

    def vacancies_pars(self, words_in):
        jobs = []
        w = {}
        for i in words_in:
            w[i] = 0
        words = []
        for page in range(0, 5):
            print(f'Парсинг страницы №{page + 1}')
            g = self.URL.format(self.name_vac)
            response = get(f'{g}&page={page}', headers=self.HEADERS)
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', {'class': 'vacancy-serp-item'})
            count = 0
            all_words_page = {}
            for i in words_in:
                all_words_page[i] = 0
            for result in results:
                try:
                    job = self.get_current_vacancy(result, words_in)
                    count += job[0]
                    j = job[1]
                    for step_word in j:
                        for b in all_words_page:
                            if b == step_word:
                                all_words_page[b] += j[step_word]
                    all_words_page['all_vacancies'] = len(results)
                except Exception as e:
                    print(e)
            words.append({str(page): all_words_page})
            jobs.append({str(page): count})
        return jobs, words
