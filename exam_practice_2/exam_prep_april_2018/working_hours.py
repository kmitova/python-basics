hours_needed = int(input())
workers = int(input())
working_days = int(input())

hours = working_days * workers * 8

if hours >= hours_needed:
    print(f"{hours - hours_needed} hours left")
else:
    overtime = hours_needed - hours
    penalty = overtime * working_days
    print(f"{overtime} overtime")
    print(f"Penalties: {penalty}")
