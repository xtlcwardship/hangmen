letters=[]
import os
word=[]
place=0
strikes=0
smoc=0
leters=int(input("how many letters in the word: "))
for i in range (leters):
    wordd=(input("what is the word letter by letter: "))
    word.append(wordd)
 
for i in range (leters):
    letters.append("_")
print(letters)
guess="b"
os.system(‘CLS’)
while guess != "done" and strikes != 6:
    guess=(input("what letter are you guessing done when the entire word was guessed say done "))
    place=-1
    pla=-1
    smoc=0
    for i in range (leters):
        place+=1
        if word[place] == guess:
            letters[place]=guess
            print(letters)
    
    for i in range (leters):
        pla+=1
        if word[pla] != guess:
            smoc+=1
            if smoc == leters:
                strikes+=1
                if strikes == 1:
                    print(" o")
                elif strikes == 2:
                    print(" o")
                    print(" l")
                elif strikes == 3:
                    print(" o")
                    print("-l")
                elif strikes == 4:
                    print(" o")
                    print("-l-")
                elif strikes == 5:
                    print(" o")
                    print("-l-")
                    print("/")
                elif strikes == 6:
                    print(" o")
                    print("-l-")
                    print(" ^")
 
print("the correct answer was " + str(word))
