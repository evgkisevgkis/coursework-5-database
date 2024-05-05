import psycopg2


def create_database(params, db_name) -> None:
    """Создание новой базы данных."""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    conn.close()


def get_vacancies(companies: list) -> list[dict]:
    """Получение вакансий через HH API"""
    pass


def insert_data(data: list[dict]):
    """Вставка данных о вакансиях в базу данных"""
    pass


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
