from cryptography.fernet import Fernet
import uuid

fernet = ""

def decryptfile():
    location = input("Please provide the file location to decrypt: ")
    try:
        with open(location, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(location, 'wb') as dec_file:
            dec_file.write(decrypted)
        print("File decrypted successfully")
        print("=============================================")
    except:
        print("Failed to decrypt the file. Please verify the file location or the privatekey provided.")
    menu()

def encryptfile():
    location = input("Please provide the file location to encrypt: ")
    try:
        with open(location, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(location, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        print("File encrypted successfully");
        print("=============================================")
    except:
        print("Failed to detect or encrypt the file provided -> " + location)
    menu()
        
def menu():
    print("0 - Exit");
    print("1 - Encrypt File")
    print("2 - Decrypt File")
    
    user_option = input("Your option: ")
    if(user_option == "0"):
        return
    
    switcher = {
        "1": encryptfile,
        "2": decryptfile
    }
    try:
        switcher.get(user_option, "Invalid option")()
    except:
        print("Invalid option provided")            

def readprivatekey():
    location = input("Please provide your key location: ")
    global fernet
    try:
        with open(location, 'rb') as filekey:
	        key = filekey.read()
        fernet = Fernet(key)
        print("Private key read successfully.");
        menu()
    except:
        print("failed to read the private key provided.")
        print("========================================")
        initialize()

def initialize():
    print("Please provide your option:\n")
    print("1 - Generate key")
    print("2 - Encrypt/Decrypt File")
    user_option_input = input("Your option: ")
    switcher = {
        "1" : generatenewkey,
        "2" : readprivatekey
    }
    try:
        switcher.get(user_option_input,"invalid option provided")()
    except:
        print("invalid option provided")

def generatenewkey():
    key = Fernet.generate_key()
    file_name = str(uuid.uuid4())
    with open(file_name +'_private.key', 'wb') as filekey:
        filekey.write(key)
        
initialize()