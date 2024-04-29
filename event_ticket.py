"""
Create a programme where users apply for a free ticket for an event.
The user needs to input some personal information to receive the ticket.
Do input validation and exception handling for each user input submitted.

"""

LINE = "-" * 79
heading = "Application for a Free Ticket to our Event!"

print(f"{LINE}\n{heading}\n{LINE}")

# Enter first name
user_name = input("Enter your first name: ")
user_name = user_name.lower()
print(user_name)

# Enter surname
user_surname = input("Enter your surname: ")
user_surname = user_surname.lower()
print(user_surname)

# Enter email address
user_email = input("Enter your email address: ")
if "@" in user_email and "." in user_email:
    print(user_email)
else:
    print("Invalid email address entered")

# Enter mobile number
user_mob_num = input("Enter a UK mobile number (starting in 07 and without spaces): ")
if len(user_mob_num) == 11 and user_mob_num.isdigit():
    print(user_mob_num)
else:
    print("Please enter a UK mobile number: ")

# Enter age (applicant must be over 18)
user_age = input("Enter your age: ")
if user_age.isnumeric and user_age >= 18:
# Thank user for registering, their ticket will be emailed 24hrs before event.
    print("Thankyou for registering, your ticket will be emailed to you 24hrs before the event starts.")
else:
    print("Sorry you have to be 18 or over to attend this event.")
