from pars import Parser


def main():
    name = str(input('Введите название вакансии: '))
    words_in = str(input('Введите ключевые слова через пробел: ')).split(' ')
    jobs = Parser(name)
    info = jobs.vacancies_pars(words_in)

    if info == 0:
        print(f'Ваканский по слову {name} не найдено')
    else:
        print(info[0])
        print(info[1])
        for i in info[0]:
            for j in i:
                print(f'На странице {int(j[0]) + 1} найдено {i[j]} ключевых слов')
        for i in info[1]:
            for j in i:
                words = i[j]
                for w in words:
                    if int(words[w]) == 0 or w == 'all_vacancies':
                        continue
                    else:
                        all_vac = int(words['all_vacancies'])
                        d = round((int(words[w])/all_vac), 3)
                        print(f'В среднем на странице №{int(j[0]) + 1} слово {w} встречается {d} раз')


if __name__ == '__main__':
    main()
