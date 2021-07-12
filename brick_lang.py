"""This program takes a sentence and converts it to the brick language""" 

sentence = input("Пожалуйста, введите предложение:\n")

vowel_letters = ['а','о', 'е', 'ы', 'и', 'у']
mod_sentence = ""

for v_letter in vowel_letters:
  mod_sentence = sentence.replace(v_letter, v_letter + "к" + v_letter)
  sentence = mod_sentence

print(sentence)