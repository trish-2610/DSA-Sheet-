s = "madAm ji"
vowel_count = 0
consonant_count = 0 

vowels = ["a","e","i","o","u"]
for char in s.lower():
    if char in vowels:
        vowel_count += 1
    elif char == " ":
        pass
    else:
        consonant_count += 1
print("Vowel Count = ",vowel_count)
print("Consonant Count = ",consonant_count)
