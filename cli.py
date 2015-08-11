import click
from googlemovieshowtimes import GoogleMovieShowtimes

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('location', default='', nargs=-1, required=False)
def main(location):
    """A command line tool to get the info on all the latest movies.
       ex: flix New
       """
    ## locations with more than one word, ie. new york
    if (len(location) > 0):
        string = ""
        for arg in location:
            string += arg + "+"
        string = string[:-1]
    else:
        string = ""

    parser = GoogleMovieShowtimes(string,"","")
    database = parser.parse()
    
    data = database['theater']
    theater = data[0]
    theater_name = theater['name']
    click.echo("")
    click.echo('{0}:'.format(theater_name))

    movies = theater['movies']

    for titles in movies:
        movie_name = titles['name']
        click.echo("")
        click.echo('{0}'.format(movie_name))
        movie_times = ""
        for movie_info in titles['times']:
            if len(movie_info) < 2:
                continue
            movie_times += str(movie_info) +  " | "
        click.echo('{0}'.format(movie_times[:-2]))
    
## if __name__ == '__main__':
##     main()




    
