number_of_players = int(input())
total_baked = 0
money_raised = 0
for player in range(number_of_players):
    name_of_player = input()
    baked_cookies = 0
    baked_waffles = 0
    baked_cakes = 0
    while True:
        bake_type = input()
        if bake_type == "Stop baking!":
            break
        baked = int(input())
        if bake_type == "cookies":
            baked_cookies = baked_cookies + baked
            money_raised = money_raised + baked * 1.5
        elif bake_type == "cakes":
            baked_cakes = baked_cakes + baked
            money_raised = money_raised + baked * 7.8
        elif bake_type == "waffles":
            baked_waffles = baked_waffles + baked
            money_raised = money_raised + baked * 2.3
        total_baked = total_baked + baked
    print(f"{name_of_player} baked {baked_cookies} cookies, {baked_cakes} cakes and {baked_waffles} waffles.")

print(f"All bakery sold: {total_baked}")
print(f"Total sum for charity: {money_raised:.2f} lv.")
