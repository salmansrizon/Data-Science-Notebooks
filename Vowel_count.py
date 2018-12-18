Vowel 
import sys

def vowel_count(S):
    # initiating vowels in an array
    vowels = ['a','e','i','o','u']
    # matching user inputs to array list
    for vowel in vowels:
        counter = 0
        for char in S:
            if char == vowel:
                # Incrementation of this processes
                counter += 1
        yield(vowel, counter)


while True:

    user_imput = input("\nPress (e) to Exit\nor Enter string: ").strip().lower()
    # Input Checking 
    if not user_imput == "e":
        print("Results: ")
        for vow, counter in vowel_count(user_imput):
            print(" " + vow + "> occurred" + str(counter) + "times.")
        else:
            print ("Thanks")
            sys.exit()