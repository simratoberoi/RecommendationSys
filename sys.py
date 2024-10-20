users_data = {
    'user1': {'gender': 'male', 'age': 24, 'night_owl': True, 'food': 'veg'},
    'user2': {'gender': 'female', 'age': 22, 'night_owl': False, 'food': 'non-veg'},
    'user3': {'gender': 'male', 'age': 23, 'night_owl': True, 'food': 'veg'},
    'user4': {'gender': 'female', 'age': 24, 'night_owl': False, 'food': 'non-veg'},
}

def preferences():
    gender = input("What is your gender? (male/female/other): ").lower()
    age = int(input("What is your age?: "))
    night_owl = input("Are you a night owl? (yes/no): ").lower() == 'yes'
    food = input("What is your food preference? (veg/non-veg): ").lower()

    return {'gender': gender, 'age': age, 'night_owl': night_owl, 'food': food}

def score(user_pref, candidate_pref):
    score = 0
    if user_pref['gender'] == candidate_pref['gender']:
        score += 10
    age_diff = abs(user_pref['age'] - candidate_pref['age'])
    if age_diff <= 2:
        score += 10 - (age_diff * 5)
    if user_pref['night_owl'] == candidate_pref['night_owl']:
        score += 5
    if user_pref['food'] == candidate_pref['food']:
        score += 5
    return score

def recommend(user_pref, users_data):
    best_match = None
    best_score = -1
    for username, candidate_pref in users_data.items():
        score = score(user_pref, candidate_pref)
        print(f"Score for {username}: {score}")
        if score > best_score:
            best_score = score
            best_match = username

    return best_match, best_score

if __name__ == "__main__":
    print("Let's find the best roommate match for you!")
    user_pref = preferences()
    best_match, best_score = recommend(user_pref, users_data)

    print(f"\nYour best roommate match is {best_match} with a score of {best_score}!")
