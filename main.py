from config import config
from utils import create_database, get_vacancies, insert_data, dbmanager_interaction


def main():
    db_name = 'hh_vacancies'
    params = config()
    companies = []

    create_database(params, db_name)

    data = get_vacancies(companies)
    insert_data(data)

    dbmanager_interaction()
