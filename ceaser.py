alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

#arra kell rájönnöm hogy hol van az adott betű az abc be a text[i] alapján és úgy eltolnom 
#valahogy úgy néz ki hogy text[i] = s -> alphabetben hol van .index és utána +shift 
#ha a total_shift indexExc-t dobna azt le kell kezelni

#ötlet 1
#zzz-> alp.index = 26 + shift = 2 -> exception de ha én azt mondom hogy amikor ez történik (am try catch de nem azzal fogom) nullázom az alphabet indexet de úgy, hogy:
#ha total_shift több mint 26 alp.index = 0 

def encrypt(text, shift, alphabet):
    chars = list(text)
    for i in range(len(text)):
        total_shift = shift + alphabet.index(chars[i])
        if total_shift > 25:   
            total_shift = shift - 1
            chars[i] = alphabet[total_shift]
        else:
            chars[i] = alphabet[total_shift]
    text = "".join(chars)
    print(f"Here is your encrypted text: {text}")    

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def decrypt(text, shift, alphabet):
    rev_alphabet = alphabet[::-1] 
    chars = list(text)
    for i in range(len(text)):
        total_shift = shift + rev_alphabet.index(chars[i])
        if total_shift > 25:   
            total_shift = shift - 1
            chars[i] = rev_alphabet[total_shift]
        else:
            chars[i] = rev_alphabet[total_shift]
    text = "".join(chars)
    print(f"Here is your deencrypted text: {text}")

def ceasar(direction):
    if direction == "encode":
        encrypt(text, shift, alphabet)
    elif direction == "decode":
        decrypt(text, shift, alphabet)
    else:
        print("Bad input!")
#decrypt(text, shift, alphabet)
#encrypt(text, shift, alphabet)

more = True

while(more):
    print("Welcome to the coder/decoder machine!")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(direction)

    choice = input("Do you wanna continue?(y/n): ")

    if choice == "n":
        more = False

