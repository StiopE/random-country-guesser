import random
rand_num = random.randint(1,196)
with open("all_countries.txt", 'r') as f:
    for i in range(rand_num):
        country = f.readline()
random_country = country.lower() 
random_country = random_country.strip() 
len_random_country = len(random_country) 
list_random_country = list(random_country) 
shadow_l = [] 
for i in range(len_random_country):
    shadow_l.append('*') 
for i in range(25, -1, -1): 
    random_letter = input("Enter a random letter: ").strip().lower()
    if random_letter == random_country:
        shadow_l = list_random_country
        break
    if random_letter in list_random_country: 
        print(f"{random_letter} is in my random country") 
        for i in range(len(list_random_country)): 
            if list_random_country[i] == random_letter: 
                shadow_l[i] = random_letter 
                list_random_country[i] = "_" 
        print(*shadow_l)
        print()
    else:
        print(f"{random_letter} is not in my random country")
        print(*shadow_l)
        print()
if '*' not in shadow_l:
    print(f"You have won the game!! The answer was {random_country}")
else:
    print("You have lost the game :( ")