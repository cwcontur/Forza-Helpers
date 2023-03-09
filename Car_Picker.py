import time
from tkinter import ttk
import sv_ttk         
import tkinter as tk
from tkinter import *
global net_start
import random 
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk
try:
    file = open("hopefully_car_list.txt", "r")
except:
    print("Failed to load information list!")
    exit(1)

dir_path = os.getcwd() # Current working directory
pic_path = os.path.join(dir_path, "Car_Class_Badges/") # Directory path of images

class App(ttk.Frame):
    def __init__(self, parent, compound=tk.RIGHT):
        super().__init__(parent, padding=7)
        self.columnconfigure(0, weight=0)
        
        self.rowconfigure(0, weight=1)
        
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="news")
        self.main_frame.rowconfigure(0, weight=1)
        
        # self.button_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        # self.button_frame.grid(row=0, column=0, padx=7, pady=7, sticky="news")
        
        # self.butt = ttk.Button(self.button_frame, text="butt")
        # self.butt.grid(row=0, column=0, padx=7, pady=7, sticky="news")
        
        self.secondary_frame = ttk.Frame(self.main_frame, style="Card.TFrame")
        self.secondary_frame.grid(row=0, column=1, padx=(0,7), pady=0, sticky="news")
        self.secondary_frame.rowconfigure(0, weight=1)
        
        self.canvas = tk.Canvas(self.secondary_frame)
        self.canvas.grid(row=0, column=0, padx=(5,0), pady=5, sticky="news")
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        self.info_frame = ttk.Frame(self.canvas)
        self.info_frame.grid(row=0, column=0, padx=(5,0), pady=5, sticky="news")
        self.info_frame.bind("<Configure>", lambda event, canvas=self.canvas: self.onFrameConfigure(canvas))
        
        self.scrollbar = ttk.Scrollbar(self.secondary_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, padx=(0,1), pady=5, sticky='ns')
        self.canvas.create_window((4,4), window=self.info_frame, anchor="nw")

        
        # ? Inserts car data into frame for viewing
        # ? =========================================
        self.sec_pos = 0
        self.pos = 0
        self.car_ratings = []
        self.car_infos = [[] for i in range(684)]
        self.badge_names = []
        self.lab_numnames = []
        self.ye_numnames = []
        self.car_numnames = []
        self.cunt_numnames = []
        
        # Gets file paths to all badge images
        for num in range(684):
            string = "Car_Class_Badges/" + str(num) + ".png"
            self.badge_names.append(string)
            self.lab_numnames.append(str(num))
            
        for items in file:
            items = items.strip('\n') # Removes annoying newline
            if self.pos == 0: # Car name
                self.temp = str(items)
                self.car_infos[self.sec_pos].append(self.temp)
            elif self.pos == 2: # Car country
                self.temp = str(items)
                self.car_infos[self.sec_pos].append(self.temp)
            elif self.pos == 3: # Car rating
                self.temp = str(self.badge_names[self.sec_pos])
                self.car_infos[self.sec_pos].append(self.temp)
                self.car_ratings.append(str(items))
            elif self.pos == 1: # Car year
                self.temp = str(items)
                self.car_infos[self.sec_pos].append(self.temp)
       
            self.pos += 1
            if self.pos == 4:
                self.pos = 0
                self.temp_img = Image.open(self.badge_names[self.sec_pos])
                self.temp_img = self.temp_img.resize((42, 20), resample=Image.Resampling.LANCZOS)
                self.temp_img = ImageTk.PhotoImage(self.temp_img)
                self.lab_numnames[self.sec_pos] = ttk.Label(self.info_frame, image=self.temp_img)
                self.lab_numnames[self.sec_pos].image = self.temp_img
                self.lab_numnames[self.sec_pos].grid(row=self.sec_pos, column=0, padx=2, pady=2, sticky="w")
                self.sec_pos += 1
                self.update()

        # ? =========================================
        
        self.righthand = ttk.Frame(self.main_frame, style="Card.TFrame")
        self.righthand.grid(row=0, column=2, padx=(0,7), pady=0, sticky="news")
        self.righthand.rowconfigure((1,2), weight=1)
        self.righthand.columnconfigure(0, weight=1)
        
        self.button_frame = ttk.Frame(self.righthand)
        self.button_frame.grid(row=0, column=0, padx=5, pady=(5,0), sticky="news")
        self.button_frame.columnconfigure(1, weight=1)
        
        self.butt = ttk.Button(self.button_frame, text="Generate")
        self.butt.grid(row=0, column=1, padx=(5,0), sticky="news")
    
        self.num_of_cars = ttk.Spinbox(self.button_frame, from_=0, to=100, increment=1)
        self.num_of_cars.insert(0, "6")
        self.num_of_cars.grid(row=0, column=0, padx=0, sticky="news")
        
        self.grammar_frame = ttk.Frame(self.righthand, style="Card.TFrame")
        self.grammar_frame.grid(row=1, column=0, padx=5, pady=5, sticky="news")
        self.grammar_frame.columnconfigure(0, weight=0)
        self.grammar_box = Text(self.grammar_frame, height=15, width=52, wrap="word", font=("Segoe UI",10),relief="flat")
        self.grammar_box.grid(row=0, column=0, padx=7, pady=7, sticky="news")
        self.grammar_box.insert("0.0", "Randomly picked cars will go here...")
        self.grammar_box.configure(state="disabled")

        self.result_frame = ttk.Frame(self.righthand, style="Card.TFrame")
        self.result_frame.grid(row=2, column=0, padx=5, pady=5, sticky="news")
        self.result_box = Text(self.result_frame, height=4, width=52, wrap="word", font=("Segoe UI",10),relief="flat")
        self.result_box.grid(row=0, column=0, padx=7, pady=7, sticky="news")
        self.result_box.insert("0.0", "<<Final Result>>")
        self.result_box.configure(state="disabled")

        self.car_choices = []
        self.cars = []
        
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all")) 
    # def random_choices(self):
    #     temp = self.num_of_cars.get()
    #     self.car_choices = []
    #     self.cars = []
    #     for x in range(int(temp)):
    #         item = random.randrange(0,684)
    #         self.car_choices.append(item)
    #     self.grammar_box.configure(state="normal")
    #     self.grammar_box.delete("1.0","end")
    #     for car in self.car_choices:
    #         iid = self.info_tree.get_children('')[car]
    #         name = self.info_tree.item(iid)['values']
    #         self.grammar_box.insert('0.0', (str(name) + "\n"))
    #         self.cars.append(name)
    #     self.grammar_box.configure(state="disabled")
    #     self.final_choice()
        
    # def final_choice(self):
    #     length = len(self.car_choices)
    #     choice = random.randrange(0, length)
    #     result = self.cars[choice]
    #     self.result_box.configure(state="normal")
    #     self.result_box.delete("1.0","end")
    #     self.result_box.insert('0.0', (str(result) + "\n"))
    #     self.result_box.configure(state="disabled")
# ! Program startup
# ! --------------------------------------
if __name__ == "__main__":
    
    app = tk.Tk()
    app.title("FH5 Buyer")
    app.geometry(f"{800}x{450}")
    app.iconbitmap("cookie.ico")

    sv_ttk.set_theme("light")
        
    App(app).pack(expand=True, fill="both")
    app.mainloop()
# ! --------------------------------------