import tkinter as tk

class Application(tk.Frame):
    def __init__(self,course_data ,imgcreator,master=None):
        self.logs = []
        self.imgcreator = imgcreator
        self.course_data = course_data
        self.added_course = {}

        super().__init__(master)
        self.master.geometry('600x400')
        self.__create_widgets()
        

    def __create_widgets(self):

        self.name_label = tk.Label(self.master, text='@Created by Fazly Fardin Chowdhury')
        self.name_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.course_label = tk.Label(self.master, text = 'Course Initial:')
        self.course_label.grid(row=0,column=0,padx=10,pady=10)
        self.course_entry = tk.Entry()
        self.course_entry.grid(row=0,column=1,padx=10,pady=10)

        self.section_label = tk.Label(self.master, text='Section:')
        self.section_label.grid(row=1,column=0,padx=10,pady=10)
        self.section_entry = tk.Entry()
        self.section_entry.grid(row=1,column=1,padx=10,pady=10)

        self.add_button = tk.Button(text='add',command=self.__add_course)
        self.add_button.grid(row=2,column=1,padx=10,pady=10)

        self.log_box = tk.Text(self.master, height=10, width=50,state='disabled')
        self.log_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.clear_button = tk.Button(text='clear',command=self.__clear_data)
        self.clear_button.grid(row=3,column=3)

        self.create_img_button = tk.Button(text='Create',command=self.__create_image)
        self.create_img_button.grid(row=4,column=1)


    def __log(self,log_message):
        self.log_box.config(state='normal')
        self.logs.append(log_message)
        self.log_box.insert(tk.END, log_message)
        self.log_box.config(state='disabled')

    def __add_course(self):
        course_initial = self.course_entry.get().upper()
        section = self.section_entry.get().upper()
        course = f'{course_initial}.{section}'

        if course in self.course_data:            
            log_message = f'{course_initial}.{section} added to database\n'
            self.added_course[course] = self.course_data[course]

        else:
            log_message = f'could not find {course_initial}.{section}\n'

        self.__log(log_message)


        self.course_entry.delete(0,tk.END)
        self.section_entry.delete(0,tk.END)

    def __create_image(self):
        if len(self.added_course) == 0:
            self.__log('there are no course added to database.\n')
            return
        self.imgcreator.create_image(self.added_course)
        self.__log('semester_routine.png has been created.\n')


    def __clear_data(self):
        self.added_course.clear()
        self.log_box.config(state='normal')
        self.log_box.delete('1.0','end')
        self.log_box.config(state='disabled')
        self.__log('Cleared database.\n')


