import click
from googlemovieshowtimes import GoogleMovieShowtimes

@click.command()
@click.argument('zipcode', default='', required=False)
def main(zipcode):
    """A command line tool to get the info on all the latest movies."""
    parser = GoogleMovieShowtimes(zipcode,"","")
    database = parser.parse()
    ##click.echo(database)
    ## #click.echo(parser.makeNice())
    
    data = database['theater']
    theater = data[1]
    movies = theater['movies']
    name = theater['name']
    click.echo('{0}'.format(name))

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
    
if __name__ == '__main__':
    main()




    
