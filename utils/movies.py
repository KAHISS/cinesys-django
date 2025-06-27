from faker import Faker
import random

faker = Faker('pt_BR')


def gerar_filme_aleatorio():

    filme = {
        "movie_id": random.randint(1000, 9999),
        "title": faker.catch_phrase(),
        "user": faker.name(),
        "rating": random.uniform(0, 10),
        "comment": faker.sentence(),
        "category": faker.word(),
        "created_at": faker.date_time_this_year(),
        "updated_at": faker.date_time_this_year(),
        "is_published": faker.boolean(),
        "poster_url": f"https://picsum.photos/seed/{random.randint(1000, 9999)}/300/450",
        "likes": random.randint(0, 1000),
    }

    return filme
