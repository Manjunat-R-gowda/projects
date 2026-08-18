import random
from hungmanword import word
from hungmanart import stages,logo

chosen=random.choice(word)
print(chosen)
lives=6
print(logo)




place_holder=" "
mean=len(chosen)
for position in range(mean):
    place_holder+="_"
print(place_holder)
correctword=[]

game=False
while not game:
    print(f"**********************{lives} lifes left***************************")
    guess=input("enter a guess letter:-").lower()
    print(guess)
    if guess in correctword:
        print(f"you are guessed correct word{guess}")
    display=" "

    for letter in chosen:

        if letter==guess:
            display+=letter
            correctword.append(guess)
        elif letter in correctword:
            display+=letter
        else:
            display+="_"

    print(display)
    if guess not in chosen:
        lives-=1
        print(f"you guess{guess}")
        if lives==0:
            game=True
            print(f"*************************correct word is{chosen},game lose***************************")
    if "_" not in display:
        game=True
        print("******************************you win************************************ ")
    print(stages[lives])
