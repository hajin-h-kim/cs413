import csv
from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt

# The hashed password string that was stolen
hashed_password_string = "tbarron:$6$hZ.FAR/z/0NW4Uj6$7q9WOkYn7EmB9Xb0sPmdnLCWINwVrqnf9usF1/sUN7lpkNQOWewvmz.VxKmTAVcCdaP7ZdQjhY3.wJRo.vjkU.:19981:0:99999:7:::"
# Extract the salt and the hashed password
parts = hashed_password_string.split('$')
algorithm = parts[1]  # '1' indicates MD5
salt = parts[2]       # '93y/T91X'
hashed_password = parts[3].split(':')[0]  # 'eNX43vhuNMe2cTQmawJbm.'

# Full salt for passlib
full_salt = f"${algorithm}${salt}$"

def check_hash(input_string, hashed_password, full_salt):
    # Hash the input string with the full salt using passlib
    hashed_value = sha512_crypt.using(salt=salt).hash(input_string)
    
    # Compare the hashed value with the hashed password
    return hashed_value.split('$')[-1] == hashed_password

def check_passwords_from_file(file_path, hashed_password, full_salt):
    with open(file_path, newline='') as csvfile:
        password_reader = csv.reader(csvfile)
        for row in password_reader:
            password = row[0]
            if check_hash(password, hashed_password, full_salt):
                print(f"The password '{password}' matches the hashed value!")
                return password
        print("No matching password found.")
        return None

# Path to the passwords.csv file
file_path = 'passwords2.csv'

# Check passwords from the file
found_password = check_passwords_from_file(file_path, hashed_password, full_salt)

if found_password:
    print(f"Password for tbarron is: {found_password}")
else:
    print("Failed to crack the password.")
