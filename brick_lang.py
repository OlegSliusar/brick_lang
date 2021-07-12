"""This program takes a sentence and converts it to the brick language"""

sentence = input("Пожалуйста, введите предложение:\n")

vowel_letters = ['а', 'А', 'о', 'О', 'е', 'Е', 'ы', 'Ы', 'и', 'И', 'у', 'У']
MOD_SENTENCE = ""

for v_letter in vowel_letters:
    MOD_SENTENCE = sentence.replace(v_letter, v_letter + "к" + v_letter.lower())
    sentence = MOD_SENTENCE

print("На кирпичном языке это будет: \n" + sentence)
