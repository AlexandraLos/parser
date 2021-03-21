from pars import Parser


def main():
    vacancy_title = str(input('Введите название вакансии: '))
    words_in = str(input('Введите ключевые слова через пробел: ')).split(' ')
    jobs = Parser(vacancy_title)
    info = jobs.vacancies_pars(words_in)
    # print(info[0])
    # print(info[1])

    for i in info[0]:
        for j in i:
            print(f'На странице №{int(j[0]) + 1} найдено {i[j]} ключевых слов')
    for i in info[1]:
        for j in i:
            words = i[j]
            for w in words:
                if int(words[w]) == 0 or w == 'all_vacancies':
                    continue
                else:
                    all_vacancies = int(words['all_vacancies'])
                    d = round((int(words[w]) / all_vacancies), 3)
                    print(f'В среднем на странице №{int(j[0]) + 1} слово "{w}" встречается {d} раз')


if __name__ == '__main__':
    main()
