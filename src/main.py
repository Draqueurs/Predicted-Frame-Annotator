from customtkinter import CTkCheckBox, set_widget_scaling, set_appearance_mode, filedialog, StringVar, IntVar, CTk, CTkOptionMenu, CTkSlider, CTkButton, CTkFrame, CTkFont, CTkScrollableFrame, CTkImage, CTkLabel, CTkToplevel
from CTkMenuBar import *
from utils import get_size
from PIL import Image
import os
import csv
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class CloseToplevelWindow(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f"360x162+{self.master.winfo_x() + (self.master.winfo_width()//2) - 180}+{self.master.winfo_y() + (self.master.winfo_height()//2) - 81}")
        self.title('Frame Annotator')
        self.resizable(False, False)

        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        warning_image = CTkImage(Image.open(resource_path('icons\warning.png')), size=(50,50))

        CTkLabel(self, text="Do you want to save the changes you\nmade to loaded file?", justify='left', font=CTkFont(size=15), image=warning_image, compound='left', anchor='w').grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        CTkLabel(self, text="Your changes will be lost if you don't save them.").grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        CTkButton(self, text='Save', command=self.save_button_event).grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        CTkButton(self, text='Don\'t Save', command=self.dont_save_button_event).grid(row=2, column=1, padx=5, pady=5, sticky='nsew')
        CTkButton(self, text='Cancel', command=self.cancel_button_event).grid(row=2, column=2, padx=5, pady=5, sticky='nsew')

    def save_button_event(self):
        self.master.save_button_event()
        if self.master.save:
            self.master.destroy()
        else:
            self.destroy()

    def dont_save_button_event(self):
        self.master.destroy()

    def cancel_button_event(self):
        self.destroy()


class ResetToplevelWindow(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f"360x162+{self.master.winfo_x() + (self.master.winfo_width()//2) - 180}+{self.master.winfo_y() + (self.master.winfo_height()//2) - 81}")
        self.title('Frame Annotator')
        self.resizable(False, False)

        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        warning_image = CTkImage(Image.open(resource_path('icons\warning.png')), size=(50,50))

        CTkLabel(self, text="Do you want to save the changes you\nmade to loaded file?", justify='left', font=CTkFont(size=15), image=warning_image, compound='left', anchor='w').grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        CTkLabel(self, text="Your changes will be lost if you don't save them.").grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        CTkButton(self, text='Save', command=self.save_button_event).grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        CTkButton(self, text='Don\'t Save', command=self.dont_save_button_event).grid(row=2, column=1, padx=5, pady=5, sticky='nsew')
        CTkButton(self, text='Cancel', command=self.cancel_button_event).grid(row=2, column=2, padx=5, pady=5, sticky='nsew')

    def save_button_event(self):
        self.master.save_button_event()
        self.master.reset()
        self.destroy()

    def dont_save_button_event(self):
        self.master.reset()
        self.destroy()

    def cancel_button_event(self):
        self.destroy()


class HetogramFrame(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DisplayFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((0,2,3,4,5,6), weight=0)



        CTkLabel(self, textvariable=self.master.display_label_label, font=CTkFont(weight='bold', size=20)).grid(row=0, column=0, columnspan=7, padx=5, pady=5, sticky='nsew')

        self.label = CTkLabel(self, text='')
        self.label.grid(row=1, column=0, columnspan=7, padx=5, pady=5, sticky='nsew')

        CTkLabel(self, textvariable=self.master.image_index_text_var, width=50, font=CTkFont(weight='bold')).grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        self.slider = CTkSlider(self, state='disabled', variable=self.master.image_index)
        self.slider.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        CTkLabel(self, textvariable=self.master.max_image_index_text_var, width=50, font=CTkFont(weight='bold')).grid(row=2, column=2, padx=5, pady=5, sticky='nsew')
        CTkButton(self, text='', width=28, height=28, image=CTkImage(light_image=Image.open(resource_path('icons\previous_light.png')), dark_image=Image.open(resource_path('icons\previous_dark.png')), size=(20,20)), command=self.master.previous).grid(row=2, column=3, padx=5, pady=5, sticky='nsew')
        CTkButton(self, text='', width=28, height=28, image=CTkImage(light_image=Image.open(resource_path('icons\\next_light.png')), dark_image=Image.open(resource_path('icons\\next_dark.png')), size=(20,20)), command=self.master.previous).grid(row=2, column=4, padx=5, pady=5, sticky='nsew')
        self.label_optionmenu = CTkOptionMenu(self, variable=self.master.label_var, font=CTkFont(weight='bold'), command=self.master.valid)
        self.label_optionmenu.grid(row=2, column=5, padx=5, pady=5, sticky='nsew')
        self.valid_button = CTkButton(self, text='Valid', font=CTkFont(weight='bold'), command=self.master.valid)
        self.valid_button.grid(row=2, column=6, padx=5, pady=5, sticky='nsew')
        
        self.label.bind('<Configure>', self.resize)

    def resize(self, event):
        if self.master.image:
            size=get_size(self.label.winfo_width(), self.label.winfo_height(), self.master.image.size[0], self.master.image.size[1])
            self.label.configure(image=CTkImage(self.master.image,
                                    size=size))


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title('Frame Annotator')
        self.minsize(self.winfo_screenwidth() // 2, self.winfo_screenheight() // 2)
         
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.image_index = IntVar(value=0)
        self.label_var = StringVar(value='none')
        self.image_index_text_var = StringVar(value=self.image_index.get())
        self.max_image_index_text_var = StringVar(value=self.image_index.get())
        self.predict_label = StringVar(value='')
        self.display_label_label = StringVar(value='')

        self.labels = ["standing", "sitting", "kneeling", "sternal", "lateral left", "lateral right", "udder left", "udder right", "empty", "unknown", "impossible"]

        menu = CTkMenuBar(self)
        menu.grid(row=0, column=0, columnspan=2, sticky='nsew')

        button_1 = menu.add_cascade("Project")
        button_2 = menu.add_cascade("Edit")
        button_3 = menu.add_cascade("Settings")
        button_4 = menu.add_cascade("About")

        dropdown1 = CustomDropdownMenu(widget=button_1)
        dropdown1.add_option(option="Create Project", command=self.create_file_button_event)
        dropdown1.add_option(option="Load Project", command=self.load_file_button_event)
        dropdown1.add_option(option="Load Images Folder", command=self.load_images_button_event)
        dropdown1.add_option(option="Load Images Ethogram", command=self.load_ethogram_button_event)
        dropdown1.add_option(option="Save", command=self.save_button_event)

        dropdown2 = CustomDropdownMenu(widget=button_2)
        dropdown2.add_option(option="Reset", command=self.reset_button_event)
        sub_menu = dropdown2.add_submenu("Select Label")
        for label in self.labels:
            sub_menu.add_option(option=label, command=lambda x=label: self.select_label(x))

        dropdown3 = CustomDropdownMenu(widget=button_3)
        sub_menu = dropdown3.add_submenu("Appearance Mode")
        sub_menu.add_option(option="System", command=lambda x='system': self.set_appearance_mode(x))
        sub_menu.add_option(option="Dark", command=lambda x='dark': self.set_appearance_mode(x))
        sub_menu.add_option(option="Light", command=lambda x='light': self.set_appearance_mode(x))
        sub_menu = dropdown3.add_submenu("Scaling")
        sub_menu.add_option(option="100%", command=lambda x=1: self.set_widget_scaling(x))
        sub_menu.add_option(option="150%", command=lambda x=1.5: self.set_widget_scaling(x))
        sub_menu.add_option(option="200%", command=lambda x=2: self.set_widget_scaling(x))

        dropdown4 = CustomDropdownMenu(widget=button_4)
        dropdown4.add_option(option="v20240208")
        dropdown4.add_option(option="Cochou Téo")

        self.ethogram_frame = HetogramFrame(master=self, width=165)

        self.display_frame = DisplayFrame(master=self)

        self.image = None
        self.openfilename = None
        self.saveasfilename = None
        self.i_dir = None
        self.e_dir = None
        self.image_names_labels = {}
        self.image_names = []
        self.save = True
        self.toplevel_window = None
        self.selected_label = None

        self.protocol("WM_DELETE_WINDOW", self.open_warningtoplevel)

    def select_label(self, label):
        if self.selected_label != label:
            self.selected_label = label
            self.image_names = [key for key, value in self.image_names_labels.items() if value[1] == label]
            if len(self.image_names) > 0:
                self.max_image_index_text_var.set(len(self.image_names))
                self.display_frame.slider.configure(to=len(self.image_names)-1, number_of_steps=len(self.image_names)-1)
                self.get_first()
                self.display_image()
            else:
                self.selected_label = None
                self.image_names = list(self.image_names_labels.keys())
        else:
            self.selected_label = None
            self.image_names = list(self.image_names_labels.keys())
            self.max_image_index_text_var.set(len(self.image_names))
            self.image_index.set(0)
            self.display_frame.slider.configure(to=len(self.image_names)-1, number_of_steps=len(self.image_names)-1)
            self.get_first()
            self.display_image()
    
    def create_file_button_event(self):
        self.openfilename = filedialog.asksaveasfilename(filetypes=[('csv files', '*.csv')], defaultextension=('csv files', '*.csv'))
        if self.openfilename:
            with open(self.openfilename, mode='w',newline='') as csv_file:
                fieldnames = ['filename', 'label', 'predict']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
            self.display_frame.label_optionmenu.configure(values=self.labels)
            self.display_frame.grid(row=1, column=1, padx=(1,0), pady=0, sticky='nsew')
            self.bind('<Up>', self.up)
            self.bind('<Down>', self.down)

    def load_file_button_event(self):
        filename = filedialog.askopenfilename(filetypes=[('csv files', '*.csv')])
        if filename:
            self.openfilename = filename
        if self.openfilename:
            self.image_names_labels = {}
            self.image_names = []
            csvfile = open(self.openfilename, 'r')
            spamreader = csv.reader(csvfile, delimiter=',')
            for index, row in enumerate(spamreader):
                if index >= 1: 
                    self.image_names_labels[row[0]] = [row[1], row[2]]
                    self.image_names.append(row[0])
            self.display_frame.label_optionmenu.configure(values=self.labels)
            self.display_frame.grid(row=1, column=1, padx=(1,0), pady=0, sticky='nsew')
            self.bind('<Up>', self.up)
            self.bind('<Down>', self.down)

    def load_images_button_event(self):
        if self.openfilename:
            self.i_dir = filedialog.askdirectory()
            if self.i_dir:
                for filename in os.listdir(self.i_dir):
                    ext = os.path.splitext(filename)[-1]
                    if (ext == '.png' or ext == '.jpg') and filename not in self.image_names_labels:
                        self.image_names_labels[filename] = ['none', 'none']
                        self.image_names.append(filename)
                self.display_frame.slider.configure(from_=0, to=len(self.image_names_labels)-1, number_of_steps=len(self.image_names_labels), state='normal')
                self.get_first()
                self.image_index_text_var.set(self.image_index.get()+1)
                self.max_image_index_text_var.set(len(self.image_names))
                self.display_image()

                self.image_index.trace_add('write', self.check_slider_var)

                self.bind('<Left>', self.previous)
                self.bind('<Right>', self.next)
                self.bind('<Return>', self.valid)

    def get_first(self):
        for index, image_name in enumerate(self.image_names):
            if self.image_names_labels[image_name][0] == 'none':
                self.image_index.set(index)
                return
        self.image_index.set(0)

    def load_ethogram_button_event(self):
        if self.openfilename:
            list = ["standing.jpg", "sitting.jpg", "kneeling.png", "sternal.jpg", "lateral left.jpg", "lateral right.png", "udder left.jpg", "udder right.jpg", "empty.jpg", "unknown.png", "impossible.png"]
            unknown = None
            impossible = None
            index = 0
            for filename in list:
                label = os.path.splitext(filename)[0]
                ext = os.path.splitext(filename)[-1]
                if (ext == '.png' or ext == '.jpg') and label != 'unknown' and label != 'impossible':
                    image = Image.open(resource_path(os.path.join('data\\ethogram\\sow\\', filename)))
                    CTkButton(self.ethogram_frame, text=label, image=CTkImage(image, size=get_size(140, 140, image.size[0], image.size[1])), compound='top', command=lambda x=label: self.set_label_var(x), font=CTkFont(weight='bold')).grid(row=index, column=0, padx=5, pady=1, sticky='nsew')
                    index += 1
                elif label == 'unknown':
                    unknown = resource_path(os.path.join('data\\ethogram\\sow\\', filename))
                elif label == 'impossible':
                    impossible = resource_path(os.path.join('data\\ethogram\\sow\\', filename))
            if unknown:
                image = Image.open(unknown)
                CTkButton(self.ethogram_frame, text='unknown', image=CTkImage(image, size=get_size(140, 140, image.size[0], image.size[1])), compound='top', command=lambda x=label: self.set_label_var(x), font=CTkFont(weight='bold')).grid(row=index, column=0, padx=5, pady=1, sticky='nsew')
                index += 1
            if impossible:
                image = Image.open(impossible)
                CTkButton(self.ethogram_frame, text='impossible', image=CTkImage(image, size=get_size(140, 140, image.size[0], image.size[1])), compound='top', command=lambda x=label: self.set_label_var(x), font=CTkFont(weight='bold')).grid(row=index, column=0, padx=5, pady=1, sticky='nsew')
                index += 1
            self.ethogram_frame.grid(row=1, column=0, padx=0, pady=0, sticky='nsew')
        else:
            self.e_dir = None
                    
    def set_label_var(self, filename):
        self.label_var.set(filename)
        self.valid()

    def save_button_event(self):
        if self.openfilename:
            self.saveasfilename = filedialog.asksaveasfilename(filetypes=[('csv files', '*.csv')], defaultextension=('csv files', '*.csv'))
            if self.saveasfilename:
                with open(self.saveasfilename, mode='w',newline='') as csv_file:
                    fieldnames = ['filename','label', 'predict']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()

                    for key, value in self.image_names_labels.items():
                        writer.writerow({'filename': key, 'label': value[0], 'predict': value[1]})
                self.save = True

    def reset_button_event(self):
        if not self.save:
            self.open_resettoplevel()
        else:
            self.reset()

    def reset(self):
        
        self.unbind('<Left>')
        self.unbind('<Right>')
        self.unbind('<Return>')
        self.unbind('<Up>')
        self.unbind('<Down>')

        self.ethogram_frame.grid_forget()
        self.display_frame.grid_forget()
        self.ethogram_frame.destroy()
        self.display_frame.destroy()

        self.image = None
        self.openfilename = None
        self.saveasfilename = None
        self.i_dir = None
        self.e_dir = None
        self.image_names_labels = {}
        self.image_names = []
        self.save = True
        self.toplevel_window = None
        self.selected_label = None

        self.image_index = IntVar(value=0)
        self.label_var = StringVar(value='none')
        self.image_index_text_var = StringVar(value=self.image_index.get())
        self.max_image_index_text_var = StringVar(value=self.image_index.get())
        self.predict_label = StringVar(value='')
        self.display_label_label = StringVar(value='')

        self.ethogram_frame = HetogramFrame(master=self, width=165)
        self.display_frame = DisplayFrame(master=self)

    def set_appearance_mode(self, mode):
        set_appearance_mode(mode)

    def set_widget_scaling(self, value):
        set_widget_scaling(value)

    def display_image(self):
        self.image = Image.open(os.path.join(self.i_dir, self.image_names[self.image_index.get()]))
        size=get_size(self.display_frame.label.winfo_width(), self.display_frame.label.winfo_height(), self.image.size[0], self.image.size[1])
        self.display_frame.label.configure(image=CTkImage(self.image,
                                  size=size))
        self.check_label_image()

    def check_slider_var(self, var, index, mode):
        self.display_image()
        self.image_index_text_var.set(self.image_index.get()+1)

    def previous(self, event=None):
        if self.i_dir:
            self.image_index.set(max(0, self.image_index.get()-1))
            if self.selected_label is None or self.selected_label == self.image_names_labels[self.image_names[self.image_index.get()]][1]:
                pass
            else:
                if self.image_index.get() > 0:
                    self.previous()

    def next(self, event=None):
        if self.i_dir:
            self.image_index.set(min(len(self.image_names_labels)-1, self.image_index.get()+1))
            if self.selected_label is None or self.selected_label == self.image_names_labels[self.image_names[self.image_index.get()]][1]:
                pass
            else:
                if self.image_index.get() < len(self.image_names)-1:
                    self.next()

    def valid(self, event=None):
        if self.i_dir:
            self.image_names_labels[self.image_names[self.image_index.get()]][0] = self.display_frame.label_optionmenu.get()
            self.save = False
            self.next()

    def change_label(self, mode):
        if self.label_var.get() != 'none':
            index = self.labels.index(self.label_var.get())
        else:
            index = 0
        self.label_var.set(self.labels[(index + mode)%len(self.labels)])
        self.display_label_label.set(f"True: {self.label_var.get()}, Predict: {self.predict_label.get()}")

    def up(self, event=None):
        self.change_label(-1)

    def down(self, event=None):
        self.change_label(+1)

    def check_label_image(self):
        if self.image_names_labels[self.image_names[self.image_index.get()]][1] != 'none':
            self.predict_label.set(self.image_names_labels[self.image_names[self.image_index.get()]][1])
        else:
            self.predict_label.set('')   
        if self.image_names_labels[self.image_names[self.image_index.get()]][0] == 'none':
            self.label_var.set(self.image_names_labels[self.image_names[self.image_index.get()]][1])
            self.display_frame.valid_button.configure(fg_color='red')
        else:
            self.label_var.set(self.image_names_labels[self.image_names[self.image_index.get()]][0])
            self.display_frame.valid_button.configure(fg_color='green')
        self.display_label_label.set(f"True: {self.label_var.get()}, Predict: {self.predict_label.get()}")

    def open_warningtoplevel(self):
        if not self.save:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = CloseToplevelWindow(self)
            self.toplevel_window.focus()
        else:
            self.destroy()

    def open_resettoplevel(self):
        if not self.save:
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ResetToplevelWindow(self)
            self.toplevel_window.focus()


app = App()
app.mainloop()