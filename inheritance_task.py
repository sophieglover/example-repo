class Course:
    
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Class attribute for head office location

    head_office = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def office_location(self):
        print("The location of the head office is", self.head_office)

class OOPCourse(Course):

    def __init__(self):
        self.description = "OOP Fundamentals"
        
        self.trainer = "Mr Anon A. Mouse"

        self.course_id = "12345"

    def trainer_details(self):
        print(f"The course is about {self.description} and it is run by trainer {self.trainer}")

    def show_course_ID(self):
        print(f"The course ID is #{self.course_id}") 

course_1 = OOPCourse()

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_ID()


