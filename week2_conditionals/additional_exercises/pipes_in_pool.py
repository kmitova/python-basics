v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_for_h = p1 * h
p2_for_h = p2 * h
p1_plus_p2_for_h = p1_for_h + p2_for_h
percent_full = (p1_plus_p2_for_h / v) * 100

p1_contribution = (p1_for_h / p1_plus_p2_for_h) * 100
p2_contribution = (p2_for_h / p1_plus_p2_for_h) * 100

if p1_plus_p2_for_h <= v:
    print(f"The pool is {percent_full}% full."
          f" Pipe 1: {p1_contribution:.2f}%."
          f" Pipe 2: {p2_contribution:.2f}%.")
else:
    print(f"For {h:.2f} hours "
          f"the pool overflows with {p1_plus_p2_for_h - v:.2f} liters.")




