from itertools import combinations
import requests
from collections import Counter
import copy
from datetime import datetime, timedelta
from decimal import Decimal
import csv


class MovieData:
    HEADERS = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMTI3NGFmYTRlNTUyMjRjYzRlN2Q0NmNlMTNkOTZjOSIsIn'
                         'N1YiI6IjVkNmZhMWZmNzdjMDFmMDAxMDU5NzQ4OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.'
                         'lbpgyXlOXwrbY0mUmP-zQpNAMCw_h-oaudAJB6Cn5c8'
    }

    BASE_URL = 'https://api.themoviedb.org/3/'

    def __init__(self, num_pages):
        self.num_pages = num_pages
        self.movie_data = None
        self.sorted_movie_data = None

    def fetch_data(self, url):
        response = requests.get(url, headers=self.HEADERS)
        if response.status_code == 200:
            return response.json()
        print('Error fetching movie data.')
        return None

    def get_movie_data(self):
        for i in range(1, self.num_pages):
            url = f'{self.BASE_URL}discover/movie?include_adult=false&include_video=false' \
                  f'&sort_by=popularity.desc&page={i}'

            movie_data = self.fetch_data(url)
            if movie_data is not None:
                self.movie_data = movie_data['results']

    def get_unique_genres(self):
        url = f'{self.BASE_URL}genre/movie/list?language=en'
        genre_data = self.fetch_data(url)

        if genre_data is not None:
            return {genre['name']: genre['id'] for genre in genre_data['genres']}

    def get_all_data(self):
        return self.movie_data

    def get_specific_indices(self):
        return self.movie_data[3:19:4]

    def most_popular_title(self):
        return max(self.movie_data, key=lambda x: x['popularity'])['title']

    def find_key_words(self, keywords):
        return [movie['title'] for movie in self.movie_data for keyword in keywords if keyword in movie['overview']]

    def delete_by_genre(self, genre_id):
        self.movie_data = list(filter(lambda x: genre_id not in x['genre_ids'], self.movie_data))

    def get_popular_genre(self):
        return Counter([genre for movie in self.movie_data for genre in movie['genre_ids']]).most_common(2)

    def get_common_movies(self):
        return [(movie_1['original_title'], movie_2['original_title'])
                for movie_1, movie_2 in combinations(self.movie_data, 2)
                if set(movie_1['genre_ids']).intersection(movie_2['genre_ids'])]

    @staticmethod
    def change_genre_id(movie):
        movie['genre_ids'][0] = 22
        return movie

    def copy_with_replacement(self):
        return self.movie_data, list(map(self.change_genre_id, copy.deepcopy(self.movie_data)))

    @staticmethod
    def sort(movie):
        date_format = '%Y-%m-%d'
        last_day_in_cinema = datetime.strptime(movie['release_date'], date_format) + timedelta(weeks=9, days=14)

        movie_shortened = {
            'Title': movie['title'],
            'Popularity': Decimal(movie['popularity']).quantize(Decimal('0.0')),
            'Score': round(movie['vote_average']),
            'Last_day_in_cinema': last_day_in_cinema.strftime(date_format)
        }
        return movie_shortened

    def get_sorted_data(self):
        shortened_data = list(map(self.sort, self.movie_data))
        self.sorted_movie_data = sorted(shortened_data, key=lambda x: (x['Score'], x['Popularity']), reverse=True)
        return self.sorted_movie_data

    def write_to_csv(self):
        with open('demo_file.csv', 'w', newline='') as my_file:
            headers = ['Title', 'Popularity', 'Score', 'Last day in cinema']
            writer = csv.DictWriter(my_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.sorted_movie_data)
