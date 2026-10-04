import os

def Encrypt(file_name, key):
    file = open(file_name, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open("CC-" + file_name, "wb")
    file.write(data)
    file.close()

def Decrypt(file_name, key):
    file = open(file_name, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(file_name, "wb")
    file.write(data)
    file.close()

choice = 1
while(choice != 4):
    print("1.Create a file\n2.Encrypt an existing file\n3.Decrypt an Existing File\n4.Quit")
    choice = int(input("Enter a choice: "))

    if(choice == 1):
        save_path = os.getcwd()
        file_name = input("Enter filename with .txt extension: ")
        filepath = os.path.join(save_path, file_name)
        text = input("Enter data to be saved: ")
        f1 = open(filepath, "w")
        f1.write(text)
        f1.close()

    if(choice == 2):
        key = int(input("Enter a key between 1-255: "))
        file_name = input("\nEnter filename with extension: ")
        Encrypt(file_name, key)
        print("File Encrypted!\nThe Encrypted filename is: ")
        print("CC-" + file_name)
        os.remove(file_name)
        continue

    if(choice == 3):
        key = int(input("Enter the key given for encryption: "))
        file_name = input("\nEnter encrypted filename with extension: ")
        Decrypt(file_name, key)
        print("File Decrypted!\nThe Decrypted filename is: ")
        print(file_name)
        continue