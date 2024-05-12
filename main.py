from config import config
from utils import create_database, get_vacancies, insert_data, dbmanager_interaction, DBManager
import psycopg2


def main():
    """Запуск функционала и взаимодействие с пользователем"""
    db_name = 'hh_vacancies'
    params = config()
    companies = ['Платформа Больших Данных',
                 'ООО Центр пространственных исследований',
                 'ООО Автомакон',
                 'ИТЕРАНЕТ',
                 'evrone.ru',
                 'Aston',
                 'рунити',
                 'Тинькофф',
                 'ООО Перфект Системс',
                 'ООО Итон',
                 'Outlines Technologies',
                 'ООО Онли',
                 'ООО Смартекс',
                 'Центр технологий моделирования']

    if input('Желаете ли создать новую базу данных?(1=да) ') == '1':
        print('Хорошо')
        create_database(params, db_name)
        print('База данных создана')
        data = get_vacancies(companies)
        print('Данные получены')
        with psycopg2.connect(dbname=db_name, **params) as conn:
            with conn.cursor() as cur:
                insert_data(cur, data)
        print('Полученные данные вставлены в базу данных')
    dbman = DBManager(db_name, params)
    while True:
        dbmanager_interaction(dbman)
        if input('Введите 0 для выхода ') == '0':
            break


if __name__ == '__main__':
    main()
