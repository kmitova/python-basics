season = input()
group = input()
students_number = int(input())
nights_number = int(input())
night_price = 0
sport = ""

if season == "Winter":
    if group == "boys" or group == "girls":
        night_price = 9.6
    if group == "mixed":
        night_price = 10
elif season == "Spring":
    if group == "boys" or group == "girls":
        night_price = 7.2
    if group == "mixed":
        night_price = 9.5
elif season == "Summer":
    if group == "boys" or group == "girls":
        night_price = 15
    if group == "mixed":
        night_price = 20

total_price = night_price * students_number * nights_number

if students_number >= 50:
    total_price = total_price - total_price * 0.5
elif 20 <= students_number < 50:
    total_price = total_price - total_price * 0.15
elif 10 <= students_number < 20:
    total_price = total_price - total_price * 0.05

if season == "Winter" and group == "girls":
    sport = "Gymnastics"
elif season == "Spring" and group == "girls":
    sport = "Athletics"
elif season == "Summer" and group == "girls":
    sport = "Volleyball"
elif season == "Winter" and group == "boys":
    sport = "Judo"
elif season == "Spring" and group == "boys":
    sport = "Tennis"
elif season == "Summer" and group == "boys":
    sport = "Football"
elif season == "Winter" and group == "mixed":
    sport = "Ski"
elif season == "Spring" and group == "mixed":
    sport = "Cycling"
elif season == "Summer" and group == "mixed":
    sport = "Swimming"

print(f"{sport} {total_price:.2f} lv.")


