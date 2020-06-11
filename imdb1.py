import scrapy

class imdb(scrapy.Spider):
    name = 'imdb_movies'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        SET_SELECTOR = 'tr'
        for movies in response.css(SET_SELECTOR):

            NAME_SELECTOR = '.titleColumn a ::text '
            year_selector = 'span ::text'
            rating_selector = 'strong ::text'

            yield {
                'name': movies.css(NAME_SELECTOR) .extract_first(),
                'release': movies.css(year_selector).extract_first(),
                'rating' : movies.css(rating_selector) .extract_first() ,
            }
            
