def calculate_calories () :
    calories_list = [20, 50, 30]
    total_calories = 0

    while True :
        print('''please select your diet
        1. rice
        2. dal
        3. chapati''')

        ch = int(input())
        if ch == 0 :
            break
        total_calories += calories_list[ch - 1]

    print("total calories consumed :",total_calories)

