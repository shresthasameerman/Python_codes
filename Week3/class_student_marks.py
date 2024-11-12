import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Student Marks Display")
root.geometry("500x500")
subjects = ["science", "socials", "maths"]
marks = {}

input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0)

for subject in subjects:
    tk.Label(input_frame, text=f"Enter marks of {subject}:").grid(row=subjects.index(subject), column=0)
    entry = tk.Entry(input_frame)
    entry.grid(row=subjects.index(subject), column=1)
    marks[subject] = entry

def gradeFinding(marks):
    total_marks = 0
    for subject in marks:
        total_marks += int(marks[subject].get())
    
    if total_marks >= 90:
        return "A"
    elif total_marks >= 80:
        return "B"
    elif total_marks >= 60:
        return "C"
    else:
        return "D"

def generate_report():
    total_marks = 0
    for subject in marks:
        total_marks += int(marks[subject].get())
    
    average_marks = total_marks / len(marks)
    percentage = (total_marks / (100 * len(marks))) * 100  # Assuming each subject is out of 100
    grade = gradeFinding(marks)
    
    # Prepare data for plotting
    subject_names = list(marks.keys())
    subject_marks = [int(marks[subject].get()) for subject in subject_names]

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.bar(subject_names, subject_marks, color='blue')
    plt.title('Marks Distribution')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.ylim(0, 100)  # Assuming marks are out of 100
    plt.grid(axis='y')
    plt.show()

    # Display the result
    result_label = tk.Label(root, text=f"Total Marks: {total_marks}, Average: {average_marks:.2f}, Percentage: {percentage:.2f}%, Grade: {grade}")
    result_label.grid(row=1, column=0)

tk.Button(root, text="Generate Report", command=generate_report).grid(row=2, column=0)

root.mainloop()