### --- OOP Email Simulator --- ###
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Declare the class variable, with default value, for emails. 

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
inbox_list = []  # List to store email objects


# --- Functions --- #
# Used to populate inbox with emails created
def populate_inbox():
    inbox_list.append(Email("MaryWroth@poetry.com","Song", 
'''Love a child is ever crying;
Please him, and he straight is flying;
Give him, he the more is craving,
Never satisfied with having …'''))
    inbox_list.append(Email("AnneBradstreet@poetry.com",
"To My Dear and Loving Husband", 
'''If ever two were one, then surely we.
If ever man were loved by wife, then thee;
If ever wife was happy in a man,
Compare with me ye women if you can …'''))
    inbox_list.append(Email("AndrewMarvell@poetry.com",
"To His Coy Mistress", 
'''Had we but world enough, and time,
This coyness, lady, were no crime.
We would sit down, and think which way
To walk, and pass our long love’s day …'''))

# Used to list emails
def list_emails():
    print("INBOX!")
    for i, email in enumerate (inbox_list):
        print(f"{i + 1}. {email.subject_line}")

# Used to display selected email and its content
def read_email(index):
    if (index - 1) <= len(inbox_list):
        email = inbox_list[index - 1]
        print(f'''/nFrom: {email.email_address}\n,
Subject: {email.subject_line}\nContent:{email.email_content}\n''')
        email.mark_as_read()
    else:
        print("Invalid email selected.")



populate_inbox()

while True:
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')

    if user_choice == "1":
        list_emails()
        try:
            index = int(input("Enter the number of the email you want to read: "))
            read_email(index)
        except ValueError as error:
            print(error)
        

    elif user_choice == "2":
        print("\nUnread Emails:")
        unread_emails = [email for email in inbox_list if not email.has_been_read]
        if unread_emails != "":
            for i, email in enumerate(unread_emails):
                print(f"{i}.{email.email_address} \n{email.subject_line}")
        else:
            print("No unread emails.")

    elif user_choice == "3":
        print("Goodbye!")
        break

    else:
        print("Incorrect option:")
