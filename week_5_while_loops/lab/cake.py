width = int(input())
length = int(input())
all_pieces = width * length
slices_left = 0
no_more_left = False

command = input()
while command != "STOP":
    slices_number = int(command)
    all_pieces = all_pieces - slices_number
    if all_pieces <= 0:
        no_more_left = True
        break
    command = input()
if no_more_left:
    print(f"No more cake left! You need {abs(all_pieces)} pieces more.")
else:
    print(f"{all_pieces} pieces are left.")

