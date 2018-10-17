from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    ###content = <hr>

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    movie = get_random_movie()
    content += "<h1>Tommorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    return content
    ###return contentT

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies = ['John Wick', 'John Wick Chapter 2', 'The Equalizer','The Equalizer 2', '31', 'House of 1000 Corpses', """The Devil's Rejects""", 'Deadpool', 'Deadpool 2']
    # TODO: randomly choose one of the movies, and return it
    movie = movies[random.randrange(0,len(movies))]
    return movie



app.run()
