movie_name = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())
    total_seats = free_seats
    sold_tickets = 0  # зануляване, защото започва продажба за нов филм, помни за зануляването!!!
    while free_seats > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        free_seats -= 1
        total_tickets += 1
        sold_tickets += 1
    print(f"{movie_name} - {sold_tickets / total_seats * 100:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100:.2f}% kids tickets.")
