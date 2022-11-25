is_male=True

is_tall=False

if is_male and is_tall:
    print("It is male or tall ")
elif is_male and not (is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("You are Tall female")
else:
        print("You are neither male or toll")
        