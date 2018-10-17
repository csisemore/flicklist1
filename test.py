import random

def main():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    print(movie)
def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies = ['John Wick', 'John Wick Chapter 2', 'The Equalizer','The Equalizer 2', '31', 'House of 1000 Corpses', """The Devil's Rejects""", 'Deadpool', 'Deadpool 2']
    # TODO: randomly choose one of the movies, and return it
    movie = movies[random.randrange(0,len(movies))]
    return movie


if __name__ == "__main__":
    main()