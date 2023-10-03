


def encrypt_text(message,n):
    ans = ""
    # iterate over the given text
    for i in range(len(message)):
        ch = message[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # if there are numbers then ignore them
        elif (ch.isdigit()):
            ans+=ch
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans



def decrypt(message,n):
    
    #enter your encrypted message(string) below
    #encrypted_message = input("Enter the message i.e to be decrypted: ").strip()
    
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower="abcdefghijklmnopqrstuvwxyz"
    
    #enter the key value to decrypt
    #n = int(input("Enter the key to decrypt: "))
    ans = ""

    for ch in message:

        if ch in upper:
            position = upper.find(ch)
            new_pos = (position - n) % 26
            new_char = upper[new_pos]
            ans += new_char
        elif ch in lower:
            position = lower.find(ch)
            new_pos = (position - n) % 26
            new_char = lower[new_pos]
            ans += new_char
        else:
            ans += ch
    return ans

#decrypt()


message = input("Enter a message to encrypt/decrypt: ")
n = int(input("Enter a key: "))
cipher = input("Would you like to encrypt or decrypt? ")
while(cipher.lower() != "encrypt" and (cipher.lower() != "decrypt")):
    cipher = input("Please type either encrypt OR decrypt! ")
if cipher.lower() == "encrypt":
    encrypt_text(message, n)
    print("Cipher Text is: " + encrypt_text(message,n))
elif cipher.lower() == "decrypt":
    decrypt(message, n)
    print("Your decrypted message is:\n")
    print(decrypt(message,n))