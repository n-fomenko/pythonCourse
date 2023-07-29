import requests
from collections import Counter
import copy
from datetime import datetime, timedelta
from decimal import Decimal
import csv


class MovieData:

    def __init__(self, num_pages):
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMTI3NGFmYTRlNTUyMjRjYzRlN2Q0NmNlMTNkOTZjOSIsInN1YiI6IjVkNmZhMWZmNzdjMDFmMDAxMDU5NzQ4OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lbpgyXlOXwrbY0mUmP-zQpNAMCw_h-oaudAJB6Cn5c8"
        }
        self.num_pages = str(num_pages)
        self.movie_data = None
        self.sorted_movie_data = None
        # self.genres

    def get_movie_data(self):
        url1 = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&sort_by=popularity.desc&page={self.num_pages}"
        response = requests.get(url1, headers=self.headers)
        if response.status_code == 200:
            self.movie_data = response.json()['results']
        else:
            print("Error fetching movie data.")

    def get_unique_genres(self):
        url2 = f"https://api.themoviedb.org/3/genre/movie/list?language=en"
        response_g = requests.get(url2, headers=self.headers)
        if response_g.status_code == 200:
            genre_data = response_g.json()
            genres = {}
            for genre in genre_data['genres']:
                genre_id = genre['id']
                genre_name = genre['name']
                genres[genre_name] = genre_id
            return genres
        else:
            print("Error fetching genre data.")

    def get_all_data(self):
        return self.movie_data

    def get_specific_indices(self):
        return self.movie_data[3:19:4]

    def most_popular_title(self):
        movie = max(self.movie_data, key=lambda x: x[
            'popularity'])
        return movie['title']

    def find_key_words(self, key_words):
        titles = []
        for movie in self.movie_data:
            for key_word in key_words:
                if key_word in movie['overview']:
                    titles.append(movie['title'])
                return titles

    def delete_by_genre(self, genre_id):
        self.movie_data = list(filter(lambda x: genre_id not in x['genre_ids'], self.movie_data))

    def get_popular_genre(self):
        count = [x['genre_ids'] for x in self.movie_data]
        flat_count = [item for sublist in count for item in sublist]
        count_genres = Counter(flat_count)
        most_common_g = count_genres.most_common(2)
        return most_common_g

    def copy_with_replacement(self):
        updated_data = []
        for movie in self.movie_data:
            updated_movie = copy.deepcopy(movie)
            updated_movie['genre_ids'][0] = 22
            updated_data.append(updated_movie)
        return self.movie_data, updated_data

    def sorted_data(self):
        shortened_data = []

        for movie in self.movie_data:
            title = movie['title']
            pop_d = Decimal(movie['popularity'])
            popularity = pop_d.quantize(Decimal('0.0'))
            score = round(movie['vote_average'])
            release_date_str = movie['release_date']
            release_date = datetime.strptime(release_date_str, "%Y-%m-%d")
            last_day_in_cinema = release_date + timedelta(weeks=9, days=14)

            movie_shortened = {
                'Title': title,
                'Popularity': popularity,
                'Score': score,
                'Last_day_in_cinema': last_day_in_cinema.strftime("%Y-%m-%d")
            }
            shortened_data.append(movie_shortened)

        sorted_movie_data = sorted(shortened_data, key=lambda x: (x['Score'], x['Popularity']), reverse=True)
        self.sorted_movie_data = sorted_movie_data
        return self.sorted_movie_data

    def write_to_csv(self):
        my_file = open('demo_file.csv', 'w', newline='')
        writer = csv.writer(my_file)
        writer.writerow(['Title', 'Popularity', 'Score', 'Last day in cinema'])
        for dictionary in self.sorted_movie_data:
            writer.writerow(dictionary.values())

        my_file.close()
        my_file = open('demo_file.csv', 'r')
        print("The content of the csv file is:")
        print(my_file.read())
        my_file.close()
