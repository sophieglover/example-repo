student_no = int(input("How many students are registering?"))

id_no_list = []

for i in range (1, student_no + 1): 
    id_no = input("Enter a student ID number:")
    id_no_list.append(id_no)

with open("reg_form.txt", "w") as f:
    f.write("\n...\n".join(id_no_list))