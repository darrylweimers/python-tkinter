import json
from tkinter import filedialog
import os
from Templates.Template import FileModify
from tkinter.filedialog import *
from tkinter import *
from tkinter.ttk import *


class WidgetCreator:

    @staticmethod
    def create_separator_widget(parent, title):
        frame = Frame(parent).pack(side=TOP, fill=X, expand=YES)
        label = Label(parent, text=title).pack(side=LEFT, fill=X, expand=NO)
        Separator(parent, orient=HORIZONTAL).pack(side=TOP, fill=X, expand=YES)
        return frame


    @staticmethod
    def create_data_entry(parent, name):
        size = len(name)
        frame = Frame(parent)
        label = Label(frame, text=name, width=size + 5)
        entry_var = StringVar()
        entry = Entry(frame, textvariable=entry_var)
        # Layout
        label.pack(side=LEFT, expand=NO)
        entry.pack(side=LEFT, fill=X, expand=YES)
        return frame, entry, entry_var

    @staticmethod
    def create_button(parent, name):
        button = Button(parent, text=name)
        # layout
        button.pack(side=RIGHT)
        return button

    @staticmethod
    def create_menu(parent, list_of_name, list_of_func):
        menu = Menu(parent, tearoff=0)
        # for index in range(len(list_of_name)):
        #     menu.add_command(label=list_of_name[index], command=list_of_func[index])
        return menu

    @staticmethod
    def create_listbox_with_scrollbar(parent):
        scrollbar = Scrollbar(parent)
        listbox = Listbox(parent, yscrollcommand=scrollbar.set, selectmode=MULTIPLE)
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        return listbox

    @staticmethod
    def create_list_widget(parent, name):
        frame = LabelFrame(parent, text=name)
        list_box = WidgetCreator.create_listbox_with_scrollbar(frame)
        # Layout
        list_box.pack(fill=BOTH, expand=YES)
        return frame, list_box

    @staticmethod
    def create_combobox(parent, tuple_of_elements):
        combobox_var = StringVar()
        combobox = Combobox(parent, textvariable=combobox_var)


class FileSystem:

    @staticmethod
    def get_directory():
        return askdirectory()

    @staticmethod
    def get_file_path():
        return askopenfilename()

    @staticmethod
    def read_file(file_path=''):
        content = ''
        if not (file_path is '' or file_path is None):
            with open(file_path, 'r+') as file_read:
                content = file_read.read()
                file_read.close()
        return content


class ReplaceConfig(WidgetCreator):

    @staticmethod
    def create_input(master, label=''):
        frame = Frame(master, padding=8)
        entry = Entry(frame)
        label = Label(frame, text=label, width=10)
        label.pack(fill=X, expand=FALSE, side=LEFT)
        entry.pack(fill=X, expand=TRUE, side=LEFT)
        return frame, entry, label

    def __init__(self, master):
        # Widget
        self.frame = Frame(master)

        self.button_execute = Button(self.frame, text='Execute')
        self.frame_find, self.entry_find, self.label_find = self.create_input(self.frame, 'Find')
        self.frame_replace, self.entry_replace, self.label_replace = self.create_input(self.frame, "Replace")

        # Layout
        self.frame.pack(fill=BOTH, expand=TRUE)
        self.frame_find.grid(row=0, column=0, sticky=W+E)
        self.frame_replace.grid(row=1, column=0, sticky=W+E)
        self.button_execute.grid(row=3, column=0, sticky=W+E)


class DocumentCompareViewer(FileSystem, WidgetCreator):
    @staticmethod
    def create_text_view(master, label):
        frame = Labelframe(master, text=label, padding=8)
        text = Text(frame, state=DISABLED)
        text.pack(fill=BOTH, expand=YES)
        return frame, text

    def __init__(self, master):
        self.master = master

        # Text View
        self.frame = Frame(self.master)
        self.frame_text_view_original, self.text_original = self.create_text_view(self.frame, "Original")
        self.frame_text_view_new, self.text_new = self.create_text_view(self.frame, "New")

        self._update_layout()

    def _update_layout(self):
        # Entry Layout
        self.frame.pack(fill=BOTH, expand=TRUE)
        self.frame_text_view_original.pack(fill=BOTH, side=LEFT)
        self.frame_text_view_new.pack(fill=BOTH, side=LEFT)

    def set_original_text(self, file_path):
        content = self.read_file(file_path)
        self.text_original['state'] = NORMAL
        self.text_original.insert(END, content)
        self.text_original['state'] = DISABLED


#Model
class Directories:

    def __init__(self, save_directory='', write_path=''):
        self.save_directory = save_directory
        self.read_path = write_path


# View
class DirectoryConfig(FileSystem):

    @staticmethod
    def create_input(master, label):
        frame_entry = Labelframe(master, text=label, padding=8)
        entry = Entry(frame_entry)
        button = Button(frame_entry, text="...")
        entry.pack(fill=X, expand=TRUE, side=LEFT)
        button.pack(fill=X, expand=FALSE, side=RIGHT)
        return frame_entry, entry, button

    @staticmethod
    def create_text_variable(widget):
        string_var = StringVar()
        widget['textvariable'] = string_var
        return string_var

    def _ask_directory(self):
        self.directories.save_directory = self.get_directory()
        self.entry_variable_save_location.set(self.directories.save_directory)

    def _ask_file_path(self):
        self.directories.read_path = self.get_file_path()
        self.entry_variable_open_location.set(self.directories.read_path)

    def _update_layout(self):
        # Entry Layout
        self.frame_entry_open_location.pack(fill=X, side=TOP)
        self.frame_entry_save_location.pack(fill=X, side=TOP)

    def __init__(self, master):
        self.directories = Directories()
        self.frame = Frame(master)

        # Entry
        self.frame_entry_open_location, self.entry_open_location, self.open_location_button = self.create_input(self.frame, "open")
        self.frame_entry_save_location, self.entry_save_location, self.save_location_button = self.create_input(self.frame, "save")
        self.entry_variable_open_location = self.create_text_variable(self.entry_open_location)
        self.entry_variable_save_location = self.create_text_variable(self.entry_save_location)

        # Button
        self.save_location_button['command'] = self._ask_directory
        self.open_location_button['command'] = self._ask_file_path

        self._update_layout()


class Application:

    #self.document_compare_viewer.set_original_text(self.directory_config.directories.read_path)

    def new_open_path(self):
        print("open path updated")

    def __init__(self, title='Application'):
        self._root = Tk()
        self._root.title(title)

        self.panned_window1 = Panedwindow(self._root)
        self.panned_window2 = Panedwindow(self._root)
        self.panned_window3 = Panedwindow(self._root)

        self.directory_config = DirectoryConfig(self.panned_window1)
        self.directory_config.entry_open_location['validatecommand'] = self.new_open_path
        self.replace_config = ReplaceConfig(self.panned_window2)
        self.document_compare_viewer = DocumentCompareViewer(self.panned_window3)

        # Layout
        self.panned_window1.pack(fill=BOTH, expand=TRUE)
        self.panned_window2.pack(fill=BOTH, expand=TRUE)
        self.panned_window3.pack(fill=BOTH, expand=TRUE)
        self.directory_config.frame.pack(fill=BOTH, expand=TRUE)

        self._root.mainloop()

Application()




#
# class ReplaceViewer:
#
#     JSON_FILE_PATH = r"C:\Users\darrylweimers\PycharmProjects\ADS\TemplateC\FindAndReplace\FindAndReplace.json"
#
#     @staticmethod
#     def get_directory_to_save_file():
#         print("Directory to save file generated")
#         return askdirectory()
#
#     def __init__(self):
#         self.save_directory = self.get_directory_to_save_file()
#         self._find_and_replace_file_by_referring_to_json()
#
#     def _find_and_replace_file_by_referring_to_json(self, json_file_path=JSON_FILE_PATH):
#         print("File to be edit")
#         open_path = filedialog.askopenfilename()
#         file_name = os.path.basename(open_path)
#         self.save_directory = os.path.join(self.save_directory, file_name)
#
#         # get json to dictionairy
#         json_data = open(json_file_path, 'r+').read()
#         python_dictionary = json.loads(json_data)
#         # file modify
#         file_modify = FileModify(self.save_directory, open_path)
#         file_modify.find_and_replace(python_dictionary)
#         # print
#         print("Task completed")
