import sys

pairs = int(input())
value_of_pair = 0
difference = -sys.maxsize
is_different = False
for pair in range(pairs):
    number_one = int(input())
    number_two = int(input())
    sum_of_pairs = number_one + number_two
    if pair == 0:
        value_of_pair = sum_of_pairs
    else:
        if value_of_pair != sum_of_pairs:
            difference = abs(sum_of_pairs - value_of_pair)
            is_different = True
            value_of_pair = sum_of_pairs
if is_different:
    print(f"No, maxdiff={difference}")
else:
    print(f"Yes, value={value_of_pair}")