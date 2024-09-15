import csv

# Generate all possible 5-character passwords
passwords = []
uppercase = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
lowercase = [chr(x) for x in range(ord('a'), ord('z') + 1)]
numbers = [str(x) for x in range(10)]

for i in uppercase:
    for j in lowercase:
        for k in lowercase:
            for l in lowercase:
                for m in numbers:
                    passwords.append(i + j + k + l + m)

# Save passwords to a file named passwords.csv
with open('passwords2.csv', 'w', newline='') as csvfile:
    password_writer = csv.writer(csvfile)
    for password in passwords:
        password_writer.writerow([password])

print("Passwords have been saved to passwords2.csv")


# lower_upper_number = [x in range ('a':'z')] + uppercase + number
