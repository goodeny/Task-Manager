from tkinter import *

class Task:
    def __init__(self):
        self.id = 0
        self.title = ''
        self.stats = 0

        self.gray = '#2b303e'
        self.blue = '#181731'
        self.green = '#0C280F'
        
        self.task_bg = PhotoImage(file='./components/task_bg.png')
        self.task_bg2 = PhotoImage(file='./components/task_bg2.png')
        self.btn_delete = PhotoImage(file='./components/btn_delete.png')
        self.btn_uncheck = PhotoImage(file='./components/btn_update.png')
        self.btn_check = PhotoImage(file='./components/btn_check.png')

    def create_task(self, title, window, bg_img, bg_img_color, color):         
        #background
        self.task_frame = Label(window, image=bg_img, bg=bg_img_color)
        self.task_frame.pack(pady=10)
        #delete button
        self.button_delete_frame = Button(self.task_frame, image=self.btn_delete, bg=color, bd=0, activebackground=color, command=self.destroy)
        self.button_delete_frame.place(x=610,y=25)
        #uncheck stats
        self.button_uncheck_frame = Button(self.task_frame, image=self.btn_uncheck, bg=color, bd=0, activebackground=color, command=self.uncheck)
        self.button_uncheck_frame.place(x=570,y=25)
        #check stats
        self.button_check_frame = Button(self.task_frame, image=self.btn_check, bg=color, bd=0, activebackground=color, command=self.check)
        self.button_check_frame.place(x=530,y=25)
        #task title
        self.title_label = Label(self.task_frame, text=title, fg='white', bg=color, font='17')
        self.title_label.place(x=200, y=27)

    def destroy(self):
        self.task_frame.destroy()
        print(self.id, self.title, self.stats)
        self.delete(self.id)

    def check(self):
        from sql import update_task_stats
        self.stats = 1
        self.task_frame.config(image=self.task_bg2)
        self.button_delete_frame.config(bg=self.green, activebackground=self.green)
        self.button_uncheck_frame.config(bg=self.green, activebackground=self.green)
        self.button_check_frame.config(bg=self.green, activebackground=self.green)
        self.title_label.config(bg=self.green)
        print(self.id, self.title, self.stats)
        update_task_stats(self.id, 1)

    def uncheck(self):
        from sql import update_task_stats
        self.stats = 0
        self.task_frame.config(image=self.task_bg)
        self.button_delete_frame.config(bg=self.blue, activebackground=self.blue)
        self.button_uncheck_frame.config(bg=self.blue, activebackground=self.blue)
        self.button_check_frame.config(bg=self.blue, activebackground=self.blue)
        self.title_label.config(bg=self.blue)
        print(self.id, self.title, self.stats)
        update_task_stats(self.id, 0)

    def insert(self, title):
        from sql import insert_task
        insert_task(title, self.stats)

    def delete(self, task_id):
        from sql import delete_task
        delete_task(task_id)

    def getAllTasks(self):
        from sql import get_all_tasks
        return get_all_tasks()

class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Task Manager")
        self.window.geometry("750x750")
        #self.window.resizable(0,0)
        self.window.configure(bg="#2B303E")
        self.window.minsize(width=750, height=750)
        #Default color
        self.blue = '#181731'
        self.gray = '#2B303E'
        self.green = '#0C280F'

        self.task_bg = PhotoImage(file='./components/task_bg.png')
        self.task_bg2 = PhotoImage(file='./components/task_bg2.png')

        self.create_header_content()
        self.create_content()
       
    def create_header_content(self):
        self.header_content = Frame(self.window, height=6, bg=self.gray)
        self.header_content.pack(fill=X)

        self.box_components = Label(self.header_content, width=50, height=5, bg=self.gray)
        self.box_components.pack()

        self.box_label_left = Label(self.box_components, text='Task', fg='white', bg=self.gray)
        self.box_label_left.place(x=0, y=35)

        self.box_bottom_center_img = PhotoImage(file='./components/center_button.png')
        self.box_bottom_center = Button(self.box_components, image=self.box_bottom_center_img, border=0, background=self.gray, activebackground=self.gray, cursor='hand2', command=self.create_input_content)
        self.box_bottom_center.place(x=150, y=20)

        self.box_label_right = Label(self.box_components, text='Manager', fg='white', bg=self.gray)
        self.box_label_right.place(x=299, y=35)

    def create_input_content(self):
        self.box_bottom_center.config(state=DISABLED)

        self.input_label_image = PhotoImage(file='./components/input_bg.png')
        self.input_label = Label(self.window, bg=self.gray, image=self.input_label_image)
        self.input_label.pack()

        self.input_entry = Entry(self.input_label, bg='white', font='Arial 12', bd=0)
        self.input_entry.place(x=54, y=87, width=560, height=40)

        self.input_button_confirm_image = PhotoImage(file='./components/input_confirm.png')
        self.input_button_confirm = Button(self.input_label, image=self.input_button_confirm_image, activebackground='#181731', bd=0, bg='#181731', command=self.confirm_input)
        self.input_button_confirm.place(x=200, y=155)

        self.input_button_cancel_image = PhotoImage(file='./components/input_cancel.png')
        self.input_button_cancel = Button(self.input_label, image=self.input_button_cancel_image, activebackground='#181731', bd=0, bg='#181731', command=self.hidde_input)
        self.input_button_cancel.place(x=350, y=155)

    def hidde_input(self):
        self.input_label.pack_forget()
        self.box_bottom_center.config(state=NORMAL)

    def confirm_input(self):
        self.tasks = Task()
        self.tasks.insert(self.input_entry.get())
        self.tasks.create_task(self.input_entry.get(), self.main_frame, self.task_bg, self.gray, self.blue)
        self.input_label.pack_forget()
        self.box_bottom_center.config(state=NORMAL)
        self.main_content.destroy()
        self.create_content()
        
    def create_content(self):
        
        self.main_content = Frame(self.window, bg=self.gray)
        self.main_content.pack(fill=Y, expand=1)

        self.canvas = Canvas(self.main_content, bg=self.gray, highlightbackground=self.gray, width=700)
        self.canvas.pack(side=LEFT, fill=Y, expand=1)

        self.scrollbar = Scrollbar(self.main_content, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        self.main_frame = Frame(self.canvas, bg=self.gray)
        self.canvas.create_window((0,0), window=self.main_frame, anchor="nw")
        self.t = Task()

        for task in self.t.getAllTasks():
            task_obj = Task()
            task_obj.id = task[0]
            task_obj.title = task[1]
            task_obj.stats = task[2]

            if task_obj.stats == 0:
                task_obj.create_task(task_obj.title, self.main_frame, self.task_bg, self.gray, self.blue)
            else:
                task_obj.create_task(task_obj.title, self.main_frame, self.task_bg2, self.gray, self.green)
                
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
if __name__ == "__main__":
    app = App()
    app.window.mainloop()
