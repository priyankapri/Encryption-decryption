'''
Programmer: Priyanka P
PittUserID = prp37
Project2 : Lab4-5-6
Date: July,7th 2021
Aim: Develop a function to encrypt and decrypt text files
'''
# Lab3
def menu():
    attempts =1
    option = str(input("VIGENERE CIPHER \n \n Select Operation: \n 1) to encrypt text \n 2) to decrypt text \n 9) Quit  \n \n"))
    while option !="1" and option !="2"  and option !="9":
        print ("Invalid choice! Please try again. \n")
        option = str(input("VIGENERE CIPHER \n \n Select Operation: \n 1) to encrypt text \n 2) to decrypt text \n 9) Quit  \n \n"))
        attempts +=1
    if option =="1":
        print("ENCRYPTING TEXT ......")
        encrypt_vigenere()
        print ("DONE!")
        attempts +=1
    elif option =="2":
        print("DECRYPTING TEXT ......")
        decrypt_vigenere()
        print ("DONE!")
    else: #option =="9":
        exit()
    #else:
        #print("Invalid Option. Try again.")

 # Lab 2
# The aim is to develop a function that can decrypt text using teh same key used for encryption
def decrypt_vigenere():
    source_file_name = input("Enter file with text:")
    destination_file_name = input("Enetr file with encrypted text:")
    user_key = input("Enter the text decryption key:")
    source_file = open(source_file_name,'r')
    file_content = source_file.readline()
    source_file.close()
    encrypted_text = file_content.strip()
    adj_key = adjusted_key(encrypted_text.lower(), user_key.lower())
    decrypted_message =""
    key_index = 0
    for i in range(len(encrypted_text)):
        if ord(encrypted_text[i]) >=97 and ord(encrypted_text[i]) <=122:
            decrypted_message = decrypted_message+chr(((ord(encrypted_text.lower()[i])-97) -(ord(adj_key.lower()[key_index]) - 97)) %26 +97)
            key_index +=1
        elif ord(encrypted_text[i]) >=65 and ord(encrypted_text[i]) <=90:
             decrypted_message = decrypted_message+chr(((ord(encrypted_text.upper()[i])-65) -(ord(adj_key.upper()[key_index]) - 65)) %26 +65)
             key_index +=1
        else:
            decrypted_message = decrypted_message+encrypted_text[i]

    destination_file = open(destination_file_name, 'w')
    destination_file.writelines(decrypted_message)
    destination_file.close()
    print(decrypted_message)

# Lab 1
# The aim is to develop a function that can encrypt text using a user specified key
def encrypt_vigenere():
    source_file_name = input("Enter file with text:")
    destination_file_name = input("Enter file with encrypted text:")
    key = input("Enter your key:") # user-specified key (Ask user for the key)
    source_file = open(source_file_name, 'r') # A file that is in your system at the same location of this code in reading mode
    file_content = source_file.readline() # read line by line the texts in the text file stored
    source_file.close()
    text = file_content.strip() # Omit whitespaces between the words
    adj_key = adjusted_key(text.lower(),key.lower()) # This is using adjusted_key function that is actually encrypting while repetting itself in your text
    encrypted_message =""
    key_index =0
    for i in range(len(text)):
        if ord(text[i]) >=97 and ord(text[i]) <=122:
            encrypted_message = encrypted_message+chr(((ord(text.lower()[i])-97) +(ord(adj_key.lower()[key_index]) - 97)) %26 +97) # if key is small w.r.t. text, we are shifting the key to move back to index 1 and repeat as needed for the text
            key_index +=1
        elif ord(text[i]) >=65 and ord(text[i]) <=90:
            encrypted_message = encrypted_message+chr(((ord(text.upper()[i])-65) +(ord(adj_key.upper()[key_index]) - 65)) %26 +65)
            key_index +=1
        else:
            encrypted_message = encrypted_message + text[i]

    destination_file=open(destination_file_name, 'w') # file where encrypted message will be written
    destination_file.writelines(encrypted_message)
    destination_file.close()
    print(encrypted_message)


def adjusted_key(text,key):
    result =''
    counter =0
    for c in text:
        if ord(c) >=97 and ord(c) <=122:
            result = result+key[counter % len(key)]
            counter +=1
    return result

'''
adjusted key function: repeating the key back to index position to match the given text
'''
def main():
    menu()

if __name__ == '__main__':
    main()
