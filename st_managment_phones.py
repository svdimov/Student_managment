from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
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


class StudentApp(App):

    def build(self):
        self.title = 'Student Management System'
        self.root = BoxLayout(orientation='vertical')

        self.root.add_widget(Button(text='Add Student', on_press=self.add_student_window))
        self.root.add_widget(Button(text='Update Student', on_press=self.update_student_window))
        self.root.add_widget(Button(text='Delete Student', on_press=self.delete_student_window))
        self.root.add_widget(Button(text='Search Student', on_press=self.search_student_window))
        self.root.add_widget(Button(text='List All Students', on_press=self.list_all_students))
        self.root.add_widget(Button(text='Exit', on_press=self.stop))

        return self.root

    def add_student_window(self, instance):
        content = BoxLayout(orientation='vertical')
        name_input = TextInput(hint_text='Name')
        age_input = TextInput(hint_text='Age', input_filter='int')
        grade_input = TextInput(hint_text='Grade', input_filter='float')
        subjects_input = TextInput(hint_text='Subjects (comma separated)')

        content.add_widget(name_input)
        content.add_widget(age_input)
        content.add_widget(grade_input)
        content.add_widget(subjects_input)
        add_button = Button(text='Add', on_press=lambda x: self.add_student(name_input.text, age_input.text, grade_input.text, subjects_input.text))
        content.add_widget(add_button)

        popup = Popup(title='Add Student', content=content, size_hint=(0.8, 0.8))
        popup.open()

    def update_student_window(self, instance):
        content = BoxLayout(orientation='vertical')
        name_input = TextInput(hint_text='Name')
        age_input = TextInput(hint_text='New Age (optional)', input_filter='int')
        grade_input = TextInput(hint_text='New Grade (optional)', input_filter='float')
        subjects_input = TextInput(hint_text='New Subjects (comma separated, optional)')

        content.add_widget(name_input)
        content.add_widget(age_input)
        content.add_widget(grade_input)
        content.add_widget(subjects_input)
        update_button = Button(text='Update', on_press=lambda x: self.update_student(name_input.text, age_input.text, grade_input.text, subjects_input.text))
        content.add_widget(update_button)

        popup = Popup(title='Update Student', content=content, size_hint=(0.8, 0.8))
        popup.open()

    def delete_student_window(self, instance):
        content = BoxLayout(orientation='vertical')
        name_input = TextInput(hint_text='Name')

        content.add_widget(name_input)
        delete_button = Button(text='Delete', on_press=lambda x: self.delete_student(name_input.text))
        content.add_widget(delete_button)

        popup = Popup(title='Delete Student', content=content, size_hint=(0.8, 0.4))
        popup.open()

    def search_student_window(self, instance):
        content = BoxLayout(orientation='vertical')
        name_input = TextInput(hint_text='Name')

        content.add_widget(name_input)
        search_button = Button(text='Search', on_press=lambda x: self.search_student(name_input.text))
        content.add_widget(search_button)

        popup = Popup(title='Search Student', content=content, size_hint=(0.8, 0.4))
        popup.open()

    def add_student(self, name, age, grade, subjects):
        students[name] = {
            'age': int(age),
            'grade': float(grade),
            'subjects': subjects.split(',')
        }
        save_data()
        Popup(title='Success', content=Label(text=f'Student {name} added successfully.'), size_hint=(0.8, 0.4)).open()

    def update_student(self, name, age, grade, subjects):
        if name in students:
            if age:
                students[name]['age'] = int(age)
            if grade:
                students[name]['grade'] = float(grade)
            if subjects:
                students[name]['subjects'] = subjects.split(',')
            save_data()
            Popup(title='Success', content=Label(text=f'Student {name} updated successfully.'), size_hint=(0.8, 0.4)).open()
        else:
            Popup(title='Error', content=Label(text=f'Student {name} not found.'), size_hint=(0.8, 0.4)).open()

    def delete_student(self, name):
        if name in students:
            del students[name]
            save_data()
            Popup(title='Success', content=Label(text=f'Student {name} deleted successfully.'), size_hint=(0.8, 0.4)).open()
        else:
            Popup(title='Error', content=Label(text=f'Student {name} not found.'), size_hint=(0.8, 0.4)).open()

    def search_student(self, name):
        if name in students:
            record = students[name]
            Popup(title='Student Record',
                  content=Label(text=f"Name: {name}\nAge: {record['age']}\nGrade: {record['grade']}\nSubjects: {', '.join(record['subjects'])}"),
                  size_hint=(0.8, 0.6)).open()
        else:
            Popup(title='Error', content=Label(text=f'Student {name} not found.'), size_hint=(0.8, 0.4)).open()

    def list_all_students(self, instance):
        if students:
            records = "\n".join([f"Name: {name}, Age: {details['age']}, Grade: {details['grade']}, Subjects: {', '.join(details['subjects'])}" for name, details in students.items()])
            Popup(title='All Students', content=Label(text=records), size_hint=(0.8, 0.8)).open()
        else:
            Popup(title='No Records', content=Label(text='No student records found.'), size_hint=(0.8, 0.4)).open()


if __name__ == '__main__':
    students = load_data()
    StudentApp().run()
