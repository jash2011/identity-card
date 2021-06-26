from tkinter import *

root = Tk()

root.title("Identity card")
root.geometry("300x400")

root.configure(bg="white")
canvas=Canvas(root,width=500,height=600)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 500, 255, fill="#1463B0")
canvas.create_rectangle(0, 345, 500, 400, fill="#1463B0")

label_heading = canvas.create_text(150,100, font=('Times', '24', 'bold italic') ,text="Identity Card")
label_name_tag = canvas.create_text(91,216, font=('Times', '16', 'bold') ,text="Name : Jash Gupta")
label_grade_tag = canvas.create_text(91,276, font=('Times', '16', 'bold') ,text="Grade : 5")
label_subjects_tag = canvas.create_text(101,311, font=('Times', '16', 'bold') ,text="phone number : 91+*************")

label_name = Label(root)
label_grade = Label(root)
label_subjects = Label(root)

def myCardDetails():
    name = "Jash Gupta"
    print(type(name))   
    grade = 10
    print(type(grade))
    subjects = ["Math","Programming"]
    print(type(subjects))
    
    label_name['text'] = name
    label_grade['text'] = grade
    label_subjects['text'] = subjects
    
    
button1 = Button(root, text = "Show my ID Card", command=myCardDetails)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=label_grade)
label_subjects_window = canvas.create_window(155, 252, anchor=CENTER, window=label_subjects)
canvas.pack()

root.mainloop()