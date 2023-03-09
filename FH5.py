# ===================================================
#
#   ,-.       _,---._ __  / \
#  /  )    .-'       `./ /   \
# (  (   ,'            `/    /|
#  \  `-"             \'\   / |
#   `.              ,  \ \ /  |
#    /`.          ,'-`----Y   |
#   (            ;        |   '
#   |  ,-.    ,-'  Connor |  /
#   |  | (   |   Contursi | /
#   )  |  \  `.___________|/
#   `--'   `--'
#
# > Create By: Connor Contursi
# > Date: 12 / 07 / 2022
#
# > A program which navigates Discord UI to automatically participate in server bot holiday event. 
# > (a.k.a. I'm lazy and I want to win for no reason just to see if I can)
#
# ===================================================

import os
import pyautogui
import pygetwindow as gw
import time
import keyboard
import customtkinter

forza = "" # Initializer for Discord window name
window_open = False # Sanity check to make sure Discord window is open and available to be focused

forza = ""
window_exist = False
# ? Checks for open windows applications to see if game is open and gets name of window
# ? =================================================================
for x in pyautogui.getAllWindows():
    if 'Forza' in x.title:
        forza = gw.getWindowsWithTitle(x.title)[0]
        print("Game window found: ", forza)
        window_exist = True
        # startup_log.append(gw_found)
    else:
        window_exist = False
        
if not window_exist:
    print("Error: Game window not found!")
    # quit()

time.sleep(.5)
# forza.activate() # Bring program into focus
time.sleep(.2)

# forza.maximize() # Make program full screen
time.sleep(.2)

tab = pyautogui.locateOnScreen('cai_tab.png', confidence=.6)
if tab:
    pyautogui.click(tab) # Click
    print("Tab focused")
else:
    print("Dumb cunt")

print("===== < Program log output > =====")

# run = True

# while run:
#     if keyboard.is_pressed("num 4"):
#         star = pyautogui.locateOnScreen('cai_star.png', confidence=.6)
#         if star:
#             pyautogui.moveTo(star)
#             pyautogui.move(-10, 0) # Terrible
#             pyautogui.click()
#     elif keyboard.is_pressed("num 5"):
#         star = pyautogui.locateOnScreen('cai_star.png', confidence=.6)
#         if star:
#             pyautogui.moveTo(star)
#             pyautogui.move(9, 0) # Bad
#             pyautogui.click()
#     elif keyboard.is_pressed("num 7"):
#         star = pyautogui.locateOnScreen('cai_star.png', confidence=.6)
#         if star:
#             pyautogui.moveTo(star)
#             pyautogui.move(29, 0) # Good
#             pyautogui.click()
#     elif keyboard.is_pressed("num 8"):
#         star = pyautogui.locateOnScreen('cai_star.png', confidence=.6)
#         if star:
#             pyautogui.moveTo(star)
#             pyautogui.move(47, 0) # Fantastic
#             pyautogui.click()
    
#     if keyboard.is_pressed("num 1"):
#         b_arr = pyautogui.locateOnScreen('cai_back.png', confidence=.9)
#         b_hov = pyautogui.locateOnScreen('ba_hov.png', confidence=.8)  
#         print("You pressed '1'.")
#         if b_arr:
#             pyautogui.click(b_arr)
#             print("Found!")
#         elif b_hov:
#             pyautogui.click(b_hov)
#             print("Found!")
#     elif keyboard.is_pressed("num 2"):
#         f_arr = pyautogui.locateOnScreen('cai_forward.png', confidence=.7)
#         f_hov = pyautogui.locateOnScreen('fo_hov.png', confidence=.8)  
#         print("You pressed '2'.")
#         if f_arr:
#             pyautogui.click(f_arr)
#             print("Found!")
#         elif f_hov:
#             pyautogui.click(f_hov)
#             print("Found!")

dir_path = os.getcwd() # Current working directory

delete_msg = os.path.join(dir_path, "FH5/", "delete_msg.png")
download = os.path.join(dir_path, "FH5/", "download.png")
downloading = os.path.join(dir_path, "FH5/", "downloading.png")

emote = os.path.join(dir_path, "FH5/", "emote.png")
horn = os.path.join(dir_path, "FH5/", "horn.png")
link = os.path.join(dir_path, "FH5/", "link.png")
car = os.path.join(dir_path, "FH5/", "car.png")
clothing = os.path.join(dir_path, "FH5/", "clothing.png")
import datetime
from playsound import playsound

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Give, now")
        self.geometry(f"{200}x{100}")
        
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


        self.main_frame = customtkinter.CTkFrame(self, corner_radius = 10)
        self.main_frame.grid(row=0,column=0,padx=10,pady=10,sticky="news")
        self.main_frame.grid_rowconfigure((0,1), weight=0)
        self.main_frame.columnconfigure((0,1), weight=0)    
            
        self.label = customtkinter.CTkLabel(self.main_frame, text="Kill Yourself")
        self.label.grid(row=0,column=0,padx=2,pady=2,sticky="news")
        
        self.start_button = customtkinter.CTkButton(self.main_frame, text="Start", corner_radius=10, anchor="center", command=self.start_func)
        self.start_button.grid(row=1,column=0,padx=5,pady=5,sticky="news")
        
        self.active = False
        self.item_counter = 0
    def start_func(self):
        print("Starting...")
        # ? ==================
        forza.activate() # Bring program into focus
        time.sleep(.2)
        forza.maximize() # Make program full screen
        time.sleep(.2)
        # ? ==================
        self.start_button.configure(hover_color="green")
        self.update()

        self.failsafe = True
        
        # self.active = True
        self.mouse_pos_1 = 0
        self.mouse_pos_2 = 0
        self.counter = 0
        self.start_t = time.time()
        self.current_t = 0
        self.lapsed = None
        self.temp = 0
        while self.failsafe:
            # self.emote_look = pyautogui.locateOnScreen(emote, confidence=.7)
            # self.horn_look = pyautogui.locateOnScreen(horn, confidence=.7)
            # self.link_look = pyautogui.locateOnScreen(link, confidence=.7)
            self.car_look = pyautogui.locateOnScreen(car, confidence=.7)
            # self.clothing_look = pyautogui.locateOnScreen(clothing, confidence=.7)
            
            # if self.counter <= 500:
            #     time.sleep(.5)
            #     self.link_look = pyautogui.locateOnScreen(link, confidence=.7)
            #     if self.link_look:
            #         continue
            #     else:
            #         print("NOTHING FOUND; HALTING PROGRAM!")
            #         self.start_button.configure(hover_color="#F14444")
            #         self.update()
            #         break
            
            self.mouse_pos_1 = pyautogui.position()
            

            
            # while self.active:
            # if self.emote_look:
            #     print("Download button not found!")
                
            # elif self.download_look:
            #     print("Download button found!")
            #     pyautogui.press('enter')
                
            # elif self.delete_msg_look:
            #     print("Emote found!")
                
            # elif self.downloading_look:
            #     print("Emote found!")
                
            # elif self.horn_look:
            #     print("Emote found!")
                
            # elif self.link_look:
            #     print("Emote found!")   
                
            # elif self.car_look:
            #     print("Emote found!") 
                
            if self.car_look:
                print("Car found!")
                # pyautogui.keyDown('x')
                # time.sleep(.05)
                # pyautogui.keyUp('x')
                pour = self.what
                pour()
                time.sleep(.2)
                self.start_t = time.time()
            else:
                self.current_t = time.time()
                self.lapsed = self.current_t - self.start_t
                self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))

            # time.sleep(.1)               
            self.update()   
            # print(self.lapsed.seconds)         
            if self.temp == 10:
                print("HALTING PROGRAM!")
                self.start_button.configure(hover_color="#F14444")
                audio_file = os.path.join(dir_path, 'not.wav')
                playsound(audio_file)
                break                
                                    
            self.mouse_pos_2 = pyautogui.position()
            if self.mouse_pos_1 != self.mouse_pos_2:
                print("HALTING PROGRAM!")
                self.start_button.configure(hover_color="#F14444")
                break
            
            self.counter += 1
        print("here")
        self.update()
        
    def what(self):
        self.download_look = pyautogui.locateOnScreen(download, confidence=.7)
        # self.delete_msg_look = pyautogui.locateOnScreen(delete_msg, confidence=.7)
        
        # self.to_download = True
        
        if self.download_look:
            print("Download button found!")
            pyautogui.press('enter')
            self.in_progress = False
            self.waiting = True
            while self.waiting:
                self.downloading_look = pyautogui.locateOnScreen(downloading, confidence=.7)
                if self.downloading_look:
                    self.in_progress = True

                if (self.in_progress == True):
                    self.waiting = False
            print("downloaded!")
            # time.sleep(.2)
            # self.download_look = pyautogui.locateOnScreen(download, confidence=.7)
            # time.sleep(.2)
            
        # elif not self.download_look:
        #     print("Deleting message!")
        #     pyautogui.press('x')
        #     waiting = True
        #     while waiting:
        #         self.delete_msg_look = pyautogui.locateOnScreen(delete_msg, confidence=.7)
        #         if self.delete_msg_look:
        #             pyautogui.press('enter')
        #             break
                            
 
                        
    def mouse_test(self):
        test = False
        while not test:
            temp1 = pyautogui.position()
            time.sleep(.1)
            temp2 = pyautogui.position()
            if temp1 != temp2:
                print("Mouse moved!")
                break
            
                
        
        
        
        # create scrollable checkbox frame
        # self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=200, command=self.checkbox_frame_event,
        #                                                          item_list=[f"item {i}" for i in range(50)])
        # self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        # self.scrollable_checkbox_frame.add_item("new item")

        # # create scrollable radiobutton frame
        # self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(master=self, width=500, command=self.radiobutton_frame_event,
        #                                                                 item_list=[f"item {i}" for i in range(100)],
        #                                                                label_text="ScrollableRadiobuttonFrame")
        # self.scrollable_radiobutton_frame.grid(row=0, column=1, padx=15, pady=15, sticky="ns")
        # self.scrollable_radiobutton_frame.configure(width=200)
        # self.scrollable_radiobutton_frame.remove_item("item 3")

        # # create scrollable label and button frame
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=300, command=self.label_button_frame_event, corner_radius=0)
        # self.scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
        # for i in range(20):  # add items with images
        #     self.scrollable_label_button_frame.add_item(f"image and item {i}", image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "test_images", "chat_light.png"))))

    # def checkbox_frame_event(self):
    #     print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")

    # def radiobutton_frame_event(self):
    #     print(f"radiobutton frame modified: {self.scrollable_radiobutton_frame.get_checked_item()}")

    # def label_button_frame_event(self, item):
    #     print(f"label button frame clicked: {item}")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()