import random


def random_book_chapter(bible):
    random_book = random.choice(list(bible))
    random_chapter = random.choice(list(bible[random_book]))
    return random_book, random_chapter