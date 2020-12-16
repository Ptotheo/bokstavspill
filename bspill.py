from playsound import playsound


playsound('a.wav')
def letter_a():
    letter_a = input("Hvilken bokstav er dette")

    if letter_a == "a":
        print("Tipp Topp Tommel Opp!")
    else:
        print("prøv igjen")


letter_a()