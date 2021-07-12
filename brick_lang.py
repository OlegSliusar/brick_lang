"""This program takes a sentence and converts it to the brick language""" 

sentence = input("Пожалуйста, введите предложение:\n")

vowel_letters = ['а', 'А', 'о', 'О', 'е', 'Е', 'ы', 'Ы', 'и', 'И', 'у', 'У']
mod_sentence = ""

for v_letter in vowel_letters:
  mod_sentence = sentence.replace(v_letter, v_letter + "к" + v_letter.lower())
  sentence = mod_sentence

print("На кирпичном языке это будет: \n" + sentence)