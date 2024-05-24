# ---------- Functions ----------

def input_validation(name_type):
    while True:
        user_input = input(f"Please enter your {name_type} here: ")
        user_input = user_input.lower()
        for char in user_input:
            if char in '.!@£$%^&*()_+=[{]};:"\\|?>,<0123456789/':
                print(f"ERROR: Invalid character used in input of {name_type}")
                break
            else:
                return user_input
            
# ---------- End of Functions ----------

# ---------- Introduction ----------

LINE = "-" * 79
heading = "Application for a Free Ticket to our Event!"

print(f"{LINE}\n{heading}\n{LINE}")

# ---------- End of Introduction ----------

# ---------- Main Code ----------

# Enter first name
user_first_name = input_validation("First Name")

# Enter last name
user_last_name = input_validation("Last Name")

# Enter email address

while True:
    user_email = input("Enter your email address: ")
    user_email = user_email.lower()
    if "@" in user_email and "." in user_email:
        break
    else:
        print("ERROR: Invalid email address entered")
        continue
            
# Enter mobile number
while True:
    user_mob_num = input("Enter a UK mobile number (starting in 07 and without spaces): ")
    if user_mob_num[0] == '0' and user_mob_num[1] == '7' and len(user_mob_num) == 11:
        break
    else:
        print("ERROR: Please enter a UK mobile number: ")
        continue

# Enter age (applicant must be over 18)
while True:
    user_age = input("Enter your age: ")
    if user_age.isdigit() and int(user_age):
        if int(user_age) >= 18:
            # Thank user for registering, their ticket will be emailed 24hrs before event.
            print("Thankyou for registering.\nYour ticket will be emailed to you 24hrs before the event starts.")
            break
        else:
            print("ERROR: Sorry you have to be 18 or over to attend this event.")
            continue
    else:
        print("ERROR: please enter your age in a numeric format")

# ---------- End of Main Code ----------

# ---------- Writing Data to File ----------

with open("event_applications.txt", 'a') as file_obj:
    file_obj.write(f"{user_first_name},{user_last_name},{user_email},{user_mob_num},{user_age},\n")

# ---------- End of Writing Data to File ----------

