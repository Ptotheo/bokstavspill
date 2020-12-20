from playsound import playsound



playsound('D:/koding/bokstavspill/soundfile/a.wav')
def letter_a():
    letter_a = input("Hvilken bokstav er dette")
	if letter_a == "a":
        print("Tipp Topp Tommel Opp!"), playsound('D:/koding/bokstavspill/soundfile/rett.wav')
    else:
        print("prøv igjen"), playsound('D:/koding/bokstavspill/soundfile/feil.wav')


letter_a()