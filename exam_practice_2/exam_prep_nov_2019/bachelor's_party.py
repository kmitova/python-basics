money_for_singer = int(input())
catering = 0
total_catering = 0
total_guests = 0
while True:
    command = input()
    if command == "The restaurant is full":
        break
    number_of_people_in_a_group = int(command)
    total_guests = total_guests + number_of_people_in_a_group
    if number_of_people_in_a_group < 5:
        catering = number_of_people_in_a_group * 100
    elif number_of_people_in_a_group >= 5:
        catering = number_of_people_in_a_group * 70
    total_catering = total_catering + catering


difference = abs(total_catering - money_for_singer)

if total_catering >= money_for_singer:
    print(f"You have {total_guests} guests and {difference} leva left.")
else:
    print(f"You have {total_guests} guests and {total_catering} leva income, but no singer.")

