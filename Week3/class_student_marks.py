import tkinter as tk

root = tk.Tk()
root.title("Student Marks Display")
root.geometry("500x500")
subjects = ["science", "socials", "maths"]
marks = {}
input_frame = tk.Frame(root)
input_frame.grid(row=1, column=0)

for subject in subjects:
    marks[subject] = tk.IntVar(value=0)

for i, subject in enumerate(subjects):
    tk.Label(input_frame, text=f"marks of {subject}").grid(row=i + 1, column=0)
    tk.Entry(input_frame, textvariable=marks[subject]).grid(row=i + 1, column=1)

def gradeFinding(marks):
    if marks >= 90:
        return "A"
    elif marks < 90 and marks >= 80:
        return "B"
    elif marks < 80 and marks >= 60:
        return "C"
    elif marks < 60 and marks >= 50:
        return "D"
    else:
        return "E"
    
def generate_report():
    total_marks = 0
    result_text = ""

    for subject in subjects:
        total_marks += float(marks[subject].get())
        result_text += f"marks of {subject}({gradeFinding(marks[subject].get())}) = {marks[subject].get()}\n"
    
    result_text += f"total marks = {total_marks}"
    result_label.config(text=result_text)

tk.Button(input_frame, text="Generate Report", command=generate_report).grid(row=len(subjects) + 1, column=0)
result_label = tk.Label(input_frame, text="Result")
result_label.grid(row=len(subjects) + 2, column=0)

root.mainloop()