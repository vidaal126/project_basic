from faker import Faker
import pymysql
from decouple import config


db = pymysql.connect(
    host=config('DB_LOCALHOST'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    database=config('DB_DATABASE'),
)
cursor = db.cursor()

fake = Faker()


def insert_plataforma_livros(num_registros):
    for _ in range(num_registros):
        nome_livro = fake.sentence(nb_words=3),
        decricao = fake.paragraph(),
        n_paginas = fake.random_int(min=50, max=500)

        cursor.execute("INSERT INTO plataforma_livros (nome_livro, decricao, n_paginas) VALUES (%s, %s, %s)", (nome_livro, decricao, n_paginas))  # noqa E501
        db.commit()


insert_plataforma_livros(5000)

db.close()
