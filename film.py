import imdb
import random
# Выбор рандомных 5 кино из топа


def top5():
    moviesDB = imdb.IMDb()
    top250 = moviesDB.get_top250_movies()
    top5_from_top250 = []
    message = ''
    i = 0
    while i < 5:
        top5_from_top250.append(random.choice(top250))
        i += 1
    for movie in top5_from_top250:
        message += movie['title'] + '\n'
    return message


# Выбор рандомного фильма по актеру


def film_by_actor(name_of_actor):
    try:
        moviesDB = imdb.IMDb()
        people = moviesDB.search_person(name_of_actor)  # в скобках вставить вводимое значение боту
        id = people[0].personID
        person = moviesDB.get_person(id)
        bio = moviesDB.get_person_biography(id)
        name = person['name']
        other_films = bio['titlesRefs']
        all_films = []
        for key in other_films:
            all_films.append(key)
        return f'name: {name}\nname of the film: {random.choice(all_films)}'
    except IndexError:
        return 'I cannot find this actor. Sorry((('


# Рейтинг выше 7


def rating():
    moviesDB = imdb.IMDb()
    movies = moviesDB.get_top250_movies()
    rating_7_higher = []
    for movie in movies:
        if int(movie['rating']) > 7:
            rating_7_higher.append(movie)
    film = random.choice(rating_7_higher)
    film_name = random.choice(rating_7_higher)['title']
    year = film['year']
    return f'film: {film_name}\nreleased year: {year}'
