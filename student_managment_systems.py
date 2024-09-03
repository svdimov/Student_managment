import tkinter as tk
from tkinter import messagebox
import json
import os

# Dictionary to store student records
students = {}


def load_data():
    if os.path.exists('students.json'):
        with open('students.json', 'r') as file:
            return json.load(file)
    return {}


def save_data():
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=4)


def add_student(name, age, grade, subjects):
    students[name] = {
        'age': age,
        'grade': grade,
        'subjects': subjects
    }
    save_data()
    messagebox.showinfo("Success", f"Student {name} added successfully.")


def update_student(name, age, grade, subjects):
    if name in students:
        if age:
            students[name]['age'] = int(age)
        if grade:
            students[name]['grade'] = float(grade)
        if subjects:
            students[name]['subjects'] = subjects.split(',')
        save_data()
        messagebox.showinfo("Success", f"Student {name} updated successfully.")
    else:
        messagebox.showerror("Error", f"Student {name} not found.")


def delete_student(name):
    if name in students:
        del students[name]
        save_data()
        messagebox.showinfo("Success", f"Student {name} deleted successfully.")
    else:
        messagebox.showerror("Error", f"Student {name} not found.")


def search_student(name):
    if name in students:
        record = students[name]
        messagebox.showinfo("Student Record", f"Name: {name}\nAge: {record['age']}\nGrade: {record['grade']}\nSubjects: {', '.join(record['subjects'])}")
    else:
        messagebox.showerror("Error", f"Student {name} not found.")


def list_all_students():
    if students:
        records = "\n".join([f"Name: {name}, Age: {details['age']}, Grade: {details['grade']}, Subjects: {', '.join(details['subjects'])}" for name, details in students.items()])
        messagebox.showinfo("All Students", records)
    else:
        messagebox.showinfo("No Records", "No student records found.")


def add_student_window():
    window = tk.Toplevel(root)
    window.title("Add Student")
    window.geometry("400x300")
    window.configure(bg='lightgreen')

    tk.Label(window, text="Name", bg='lightgreen').grid(row=0, column=0, pady=5)
    tk.Label(window, text="Age", bg='lightgreen').grid(row=1, column=0, pady=5)
    tk.Label(window, text="Grade", bg='lightgreen').grid(row=2, column=0, pady=5)
    tk.Label(window, text="Subjects", bg='lightgreen').grid(row=3, column=0, pady=5)

    name_entry = tk.Entry(window)
    age_entry = tk.Entry(window)
    grade_entry = tk.Entry(window)
    subjects_entry = tk.Entry(window)

    name_entry.grid(row=0, column=1, pady=5)
    age_entry.grid(row=1, column=1, pady=5)
    grade_entry.grid(row=2, column=1, pady=5)
    subjects_entry.grid(row=3, column=1, pady=5)

    def on_add():
        name = name_entry.get()
        age = int(age_entry.get())
        grade = float(grade_entry.get())
        subjects = subjects_entry.get().split(',')
        add_student(name, age, grade, subjects)
        window.destroy()

    tk.Button(window, text="Add", command=on_add, bg='green', width=17, height=2).grid(row=4, column=1, pady=10)


def update_student_window():
    window = tk.Toplevel(root)
    window.title("Update Student")
    window.geometry("400x300")
    window.configure(bg='lightyellow')

    tk.Label(window, text="Name", bg='lightyellow').grid(row=0, column=0, pady=5)
    tk.Label(window, text="New Age", bg='lightyellow').grid(row=1, column=0, pady=5)
    tk.Label(window, text="New Grade", bg='lightyellow').grid(row=2, column=0, pady=5)
    tk.Label(window, text="New Subjects", bg='lightyellow').grid(row=3, column=0, pady=5)

    name_entry = tk.Entry(window)
    age_entry = tk.Entry(window)
    grade_entry = tk.Entry(window)
    subjects_entry = tk.Entry(window)

    name_entry.grid(row=0, column=1, pady=5)
    age_entry.grid(row=1, column=1, pady=5)
    grade_entry.grid(row=2, column=1, pady=5)
    subjects_entry.grid(row=3, column=1, pady=5)

    def on_update():
        name = name_entry.get()
        age = age_entry.get()
        grade = grade_entry.get()
        subjects = subjects_entry.get()
        update_student(name, age, grade, subjects)
        window.destroy()

    tk.Button(window, text="Update", command=on_update, bg='yellow', width=17, height=2).grid(row=4, column=1, pady=10)


def delete_student_window():
    window = tk.Toplevel(root)
    window.title("Delete Student")
    window.geometry("400x300")
    window.configure(bg='lightcoral')

    tk.Label(window, text="Name", bg='lightcoral').grid(row=0, column=0, pady=5)

    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1, pady=5)

    def on_delete():
        name = name_entry.get()
        delete_student(name)
        window.destroy()

    tk.Button(window, text="Delete", command=on_delete, bg='red', width=17, height=2).grid(row=1, column=1, pady=10)


def search_student_window():
    window = tk.Toplevel(root)
    window.title("Search Student")
    window.geometry("400x300")
    window.configure(bg='lightblue')

    tk.Label(window, text="Name", bg='lightblue').grid(row=0, column=0, pady=5)

    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1, pady=5)

    def on_search():
        name = name_entry.get()
        search_student(name)
        window.destroy()

    tk.Button(window, text="Search", command=on_search, bg='blue', width=17, height=2).grid(row=1, column=1, pady=10)


# Create the main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("300x400")

tk.Button(root, text="Add Student", command=add_student_window, bg='green', width=20, height=2).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student_window, bg='yellow', width=20, height=2).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student_window, bg='red', width=20, height=2).pack(pady=5)
tk.Button(root, text="Search Student", command=search_student_window, bg='blue', width=20, height=2).pack(pady=5)
tk.Button(root, text="List All Students", command=list_all_students, width=20, height=2).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=20, height=2).pack(pady=5)

# Load student data from the JSON file
students = load_data()

# Run the application
root.mainloop()
