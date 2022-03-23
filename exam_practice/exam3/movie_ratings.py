from sys import maxsize
number_of_movies = int(input())
lowest_rating = 10
highest_rating = -maxsize
total_ratings = 0
highest_rated = ""
lowest_rated = ""
for movie in range(number_of_movies):
    name = input()
    rating = float(input())
    if rating >= highest_rating:
        highest_rating = rating
        total_ratings += rating
        highest_rated = name
    else:
        if rating < lowest_rating:
            lowest_rating = rating
            lowest_rated = name
        total_ratings += rating

average_rating = total_ratings / number_of_movies
print(f"{highest_rated} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rated} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
