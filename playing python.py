
import datetime

x = datetime.datetime.now()


while True:   
    print(x)

    print("Hello you!, ik ben python \n")
    c = input("Wie ben jij?\n")
    print(f"Hello {c}\n") 
    if (input("do you want to repeat:") == 'y'):
        continue
    else:
        break   

print("Hoe oud ben ik (a) 16 (b) 17 (c) 20 (d) 15")
answer1 = "a"
response1 = input("Your answer is: ")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")

print("Welke school zit ik op (a) horizon college hoorn (b) media college amsterdam (c) HMC (d) regio college")
answer1 = "b"
response1 = input("Your answer is: ")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")

print("Welke progameer taal ben ik bekend mee (a) HTML (b)Java script (c) python (d) c++")
answer1 = "c"
response1 = input("Your answer is: ")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is het goede antwoord je hebt alles goed gekozen je bent een legend ")