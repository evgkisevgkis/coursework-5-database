import psycopg2
import requests


def create_database(params, db_name) -> None:
    """Создание новой базы данных."""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    cur.close()
    conn.close()

    with psycopg2.connect(dbname=db_name, **params) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                    CREATE TABLE vacancies(
                    vacancy_id SERIAL PRIMARY KEY,
                    vacancy_name VARCHAR NOT NULL,
                    company_name VARCHAR(50) NOT NULL,
                    salary INT,
                    url VARCHAR,
                    city VARCHAR,
                    description TEXT
                    )
                    """)


def get_vacancies(companies: list) -> list[dict]:
    """Получение вакансий через HH API"""
    data = []
    companies = companies
    for company in companies:
        page = 0
        query_param = {'text': company,
                       'search_field': 'company_name',
                       'page': page,
                       'per_page': 100}
        req = requests.get('https://api.hh.ru/vacancies', query_param)
        pages_count = req.json().get('pages', 0)
        while page <= pages_count:
            req = requests.get('https://api.hh.ru/vacancies', query_param)
            vacancies = req.json()['items']
            for i in vacancies:
                data.append(i)
            page += 1
    return data


def insert_data(cur, data: list[dict]):
    """Вставка данных о вакансиях в базу данных"""
    for item in data:
        vacancy = {'name': item['name'],
                   'employer': item['employer']['name'],
                   'salary': 0 if item['salary'] is None else item.get('salary', {'from': 0})['from'],
                   'url': item['alternate_url'],
                   'city': None if item['address'] is None else item['address'].get('city'),
                   'description': item['snippet'].get('responsibility')}
        cur.execute(
            """
            INSERT INTO vacancies(vacancy_name, company_name, salary, url, city, description)
            VALUES (%s, %s, %s, %s, %s, %s)""",
            (vacancy['name'], vacancy['employer'], vacancy['salary'], vacancy['url'],
             vacancy['city'], vacancy['description'])
        )


class DBManager:
    """Класс для работы с данными в БД"""
    def get_companies_and_vacancies_count(self) -> list[tuple[str, int]]:
        """Получает список всех компаний и количество вакансий у каждой компании"""
        pass

    def get_all_vacancies(self) -> list[dict]:
        """Получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию"""
        pass

    def get_avg_salary(self) -> float:
        """Получает среднюю зарплату по вакансиям"""
        pass

    def get_vacancies_with_higher_salary(self) -> list[dict]:
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        pass

    def get_vacancies_with_keyword(self, keyword) -> list[dict]:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        pass


def dbmanager_interaction() -> None:
    """Взаимодействие пользователя с экзепляром класса для работы с данными"""
    pass
