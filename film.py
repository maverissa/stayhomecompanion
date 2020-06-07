import imdb
import random
import emoji
import telebot


bot = telebot.TeleBot('1116307628:AAGco0iC37MG0Yy_J3p7esHABjEpedxu7u0')
rating_button = ['7-8', '9-10']
rating_msg = 'Choose the rating:'
year_button = ['80s', '90s', '00s', '10s', 'new 2019-2020']
year_msg = emoji.emojize('Choose the year of the film and I will try to'
                         ' find it as quickly as possible:sparkles:',
                         use_aliases=True)
film_menu = [emoji.emojize('5 movies from top :bomb:', use_aliases=True),
             emoji.emojize('Actor :dancer:', use_aliases=True),
             emoji.emojize('Rating :fire:', use_aliases=True),
             emoji.emojize('Released year :calendar:', use_aliases=True)]
film_menu_msg = 'By what criteria do you want to choose a film?'


# Selection of random 5 movies from the top
def top5():
    movies_db = imdb.IMDb()
    top250 = movies_db.get_top250_movies()
    top5_from_top250 = []
    message = ''
    i = 0
    while i < 5:
        top5_from_top250.append(random.choice(top250))
        i += 1
    for movie in top5_from_top250:
        message += movie['title'] + '\n'
    return message


# Selection of a random movie by actor
def film_by_actor(name_of_actor):
    try:
        movies_db = imdb.IMDb()
        people = movies_db.search_person(name_of_actor)
        # в скобках вставить вводимое значение боту
        id = people[0].personID
        person = movies_db.get_person(id)
        bio = movies_db.get_person_biography(id)
        name = person['name']
        other_films = bio['titlesRefs']
        all_films = []
        for key in other_films:
            all_films.append(key)
        return f'{name}\nName of the film: {random.choice(all_films)}'
    except IndexError:
        return 'I cannot find this actor. Sorry((('


# Rating 7-8 and 9-10
def rating(call):
    movies_db = imdb.IMDb()
    movies = movies_db.get_top250_movies()
    desired_rating = []
    if call.data == rating_button[0]:
        for movie in movies:
            if 7 <= int(movie['rating']) <= 8:
                desired_rating.append(movie)
    elif call.data == rating_button[1]:
        for movie in movies:
            if 9 <= int(movie['rating']) <= 10:
                desired_rating.append(movie)
    film = random.choice(desired_rating)
    id = film.getID()
    info = movies_db.get_movie(id)
    plot = info['plot summary']
    normal_plot = editing_plot(plot)
    film_name = random.choice(desired_rating)['title']
    year = film['year']
    bot.send_message(call.message.chat.id,
                     f'{film_name}\nReleased year: {year}\nPlot: '
                     f'{normal_plot}')


# Film by the year
def by_year(call):
    movies_db = imdb.IMDb()
    movies = movies_db.get_top250_movies()
    desired_year = []
    if call.data == year_button[0]:
        for movie in movies:
            if 1980 <= int(movie['year']) < 1990:
                desired_year.append(movie)
    elif call.data == year_button[1]:
        for movie in movies:
            if 1990 <= int(movie['year']) < 2000:
                desired_year.append(movie)
    elif call.data == year_button[2]:
        for movie in movies:
            if 2000 <= int(movie['year']) < 2010:
                desired_year.append(movie)
    elif call.data == year_button[3]:
        for movie in movies:
            if 2010 <= int(movie['year']) <= 2020:
                desired_year.append(movie)
    elif call.data == year_button[4]:
        for movie in movies:
            if 2019 <= int(movie['year']) <= 2020:
                desired_year.append(movie)
    film = random.choice(desired_year)
    id = film.getID()
    info = movies_db.get_movie(id)
    plot = info['plot summary']
    normal_plot = editing_plot(plot)
    film_name = random.choice(desired_year)['title']
    year = film['year']
    actors = ', '.join(map(str, casting))
    bot.send_message(call.message.chat.id,
                     f'{film_name}\nReleased year: {year}\nActors: '
                     f'{actors}\nPlot: {normal_plot}')


def film_subscription(person):
    movies_db = imdb.IMDb()
    movies = movies_db.get_top250_movies()
    desired_year = []
    for movie in movies:
        if int(movie['year']) == 2019:
            desired_year.append(movie)
    desired_film = random.choice(desired_year)
    id = desired_film.getID()
    info = movies_db.get_movie(id)
    plot = info['plot summary']
    normal_plot = editing_plot(plot)
    film_name = random.choice(desired_year)['title']
    year = desired_film['year']
    directors = info['directors']
    directstr = ' '.join(map(str, directors))
    bot.send_message(person,
                     f'{film_name}\nReleased year: {year}\nDirector: '
                     f'{directstr}\nPlot: {normal_plot}')


def editing_plot(plot):
    plot1 = []
    for i in plot[0]:
        if i == ':':
            break
        else:
            plot1.append(i)
    plot1 = [''.join(plot1)]
    return plot1[0]
