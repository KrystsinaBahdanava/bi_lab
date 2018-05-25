import csv

# read file
from pathlib import Path


def ratings_field(element):
    return element[2]


def sort_movies(movies_list):
    movies_list.sort(key=ratings_field, reverse=True)


all_movies = []
path = Path('IMDB-Movie-Data.csv')
if path.is_file():
    with open(path, 'r') as movies:
        reader = csv.DictReader(movies)
        for row in reader:
            all_movies.append([row["Title"], row["Year"], row["Rating"]])
else:
    print("EXCEPTION!")

sort_movies(all_movies)

print(all_movies)

# write top 250
with open('top250_movies.csv', 'w') as top250:
    writer = csv.writer(top250)
    for row in all_movies[:250]:
        writer.writerow([row[0]])


def avg_movies(movies_avg):
    result = {}
    for movie in movies_avg:
        res = result.get(movie[1], [0, 0.0])
        res[0] += 1
        res[1] += float(movie[2])
        result[movie[1]] = res
    return result


# write aggregations
aggregated_movies = {}
for k, v in avg_movies(all_movies).items():
    aggregated_movies[k] = v[1] / v[0]
with open('avg_ratings_movies.csv', 'w') as aggregated:
    writer = csv.writer(aggregated)
    for k, v in aggregated_movies.items():
        writer.writerow([k, v])

print(aggregated_movies)
