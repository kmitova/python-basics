movie_name = input()
salon_type = input()
tickets_purchased = int(input())
earnings = 0

if movie_name == "A Star Is Born":
    if salon_type == "normal":
        earnings = tickets_purchased * 7.5
    elif salon_type == "luxury":
        earnings = tickets_purchased * 10.5
    elif salon_type == "ultra luxury":
        earnings = tickets_purchased * 13.5
elif movie_name == "Bohemian Rhapsody":
    if salon_type == "normal":
        earnings = tickets_purchased * 7.35
    elif salon_type == "luxury":
        earnings = tickets_purchased * 9.45
    elif salon_type == "ultra luxury":
        earnings = tickets_purchased * 12.75
elif movie_name == "Green Book":
    if salon_type == "normal":
        earnings = tickets_purchased * 8.15
    elif salon_type == "luxury":
        earnings = tickets_purchased * 10.25
    elif salon_type == "ultra luxury":
        earnings = tickets_purchased * 13.25
elif movie_name == "The Favourite":
    if salon_type == "normal":
        earnings = tickets_purchased * 8.75
    elif salon_type == "luxury":
        earnings = tickets_purchased * 11.55
    elif salon_type == "ultra luxury":
        earnings = tickets_purchased * 13.95

print(f"{movie_name} -> {earnings:.2f} lv.")
