# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Initialise the instance variables for each email.

    has_been_read = False   # defaults to having not been read

    # Create the 'mark_as_read()' method to change the 'has_been_read'
    # instance variable for a specific object from False to True.

    def mark_as_read(self):
        self.has_been_read = True
       

# --- Functions --- #
# Build out the required functions for your program.

inbox = []


# Create 3 sample emails and add them to the inbox list.

def populate_inbox():
    email1 = Email("noreply@deliveroo.com", "Your Order is in the Kitchen!",
                   "Food will be delivered in 25 minutes.")
    
    email2 = Email("onion06@gmail.com", "I miss you :(",
                   "Looking forward to seeing you soon!")
    
    email3 = Email("hyperiondev@outlook.com", "Welcome to HyperionDev!",
                   "Good luck, contact us if you need any help.")

    inbox.extend([email1, email2, email3])    
    
    pass


# Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.

def list_emails():

    for index, email in enumerate(inbox):
        print(f"{index}  {email.subject_line}")
    
    pass


# Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True


def read_email(index):

    selected_email = inbox[index]

    print(f"\nEmail Address: {selected_email.email_address}")
    print(f"Subject Line: {selected_email.subject_line}")
    print(f"Content: {selected_email.email_content}")

    selected_email.mark_as_read()

    print(f"\nEmail from {selected_email.email_address} marked as read. \n")
    
    pass


# Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.

def view_unread_emails():

    for index, email in enumerate(inbox):
        if email.has_been_read == False:
            print(f"\n{index}  {email.subject_line}")
    
    pass


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.

populate_inbox() 

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:

        list_emails()
        
        index = int(input("Input the index of desired email:"))

        read_email(index)

    
    elif user_choice == 2:

        view_unread_emails()
        

    elif user_choice == 3:
        print("Goodbye!")
        break

    else:
        print("Oops - incorrect input.")











