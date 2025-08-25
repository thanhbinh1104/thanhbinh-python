import random

money = 100
win_count = 0
lose_count = 0

while money >= 5:
    print("Computer thinks a number from 1 to 100")
    comp_number = random.randint(1, 100)

    level = int(input('Choose level [1,2,3]? '))
    # 1: easy, 2: medium, 3: hard
    times = 10 if level == 1 else 5 if level == 2 else 3
    is_win = False
    money -= 5

    for time in range(times):
        your_num = int(input("Enter your guessing number #" + str(time + 1) + ": "))
        if your_num == comp_number:
            is_win = True
        else:
            if your_num < comp_number:
                print('too low!')
            else:
                print('too high!')
    if is_win and time + 1 >= times:
            print("You are Genius!!!!")
            win_count += 1
    if time + 1 >= times:
            print('-----------------------')
            print('Game over')
            lose_count += 1
    print('---------------------------')
    print(f"Wins: {win_count} | Losses: {lose_count}")
    print(f"Money left: ${money}")

    if money < 5:
        print("You don't have enough money to continue. Game ended.")
        break

    cont = input("Dare you to play [y/n]: ")
    if cont == 'n' or cont == 'N':
        break
print(f"Total Wins: {win_count}")
print(f"Total Losses: {lose_count}")
print(f"Final Money: {money}")