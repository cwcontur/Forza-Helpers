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
# ===================================================
# import definitions    
import os
import pyautogui
import pygetwindow as gw
import time
import keyboard
import datetime
import os
from PIL import Image, ImageTk
import time
from tkinter import ttk
import PIL.Image
# import tkinter
import sv_ttk         
import tkinter as tk
from tkinter import *
from datetime import datetime
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
global net_start

global log
log = []

global window_exist
forza = "" # Initializer for Discord window name
window_exist = False # Sanity check to make sure Discord window is open and available to be focused
# ? Checks for open windows applications to see if game is open and gets name of window
# ? =================================================================
for x in pyautogui.getAllWindows():
    if 'Forza' in x.title:
        forza = gw.getWindowsWithTitle(x.title)[0]
        log_now = str(datetime.utcnow().strftime('%H:%M:%S') + " - Game window found: ")
        log.append(log_now)
        window_exist = True
        break
    else:
        window_exist = False
        
if not window_exist:
    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Error: Game window not found!"
    log.append(log_now)
    
dir_path = os.getcwd() # Current working directory
pic_path = os.path.join(dir_path, "Auc_Trimed/") # Directory path of images
try:
    # * All images to needed to navigate and use GUI
    Adv_Search = os.path.join(pic_path, "Adv_Search.png") # Up Arrow -> Enter
    Adv_Tag_Hovered = os.path.join(pic_path, "Adv_Tag_Hovered.png") # Enter
    Auc_Buy_Hovered = os.path.join(pic_path, "Auc_Buy_Hovered.png") # Enter
    Auc_Buy = os.path.join(pic_path, "Auc_Buy.png") # Down Arrow -> Enter
    Base_Search = os.path.join(pic_path, "Base_Search.png") # X
    Buy_Success = os.path.join(pic_path, "Buy_Success.png") # Enter
    Buyout_N = os.path.join(pic_path, "Buyout_N.png") # Up Arrow -> Enter
    Buyout_Y = os.path.join(pic_path, "Buyout_Y.png") # Enter
    Claiming = os.path.join(pic_path, "Claiming.png") # [WAIT]
    Collect_Not = os.path.join(pic_path, "Collect_Not.png") # Up Arrow -> Enter
    Collect_Yes = os.path.join(pic_path, "Collect_Yes.png")  # Enter
    First_Screen = os.path.join(pic_path, "First_Screen.png") # Enter
    Man_Key = os.path.join(pic_path, "Man_Key.png") # Type 'Focusedspade' -> Enter
    No_Auc = os.path.join(pic_path, "No_Auc.png") # Esc -> [First_Screen]
    Cody = os.path.join(pic_path, "Focusedspade.png")
    Confirm_Hovered = os.path.join(pic_path, "Confirm_Hovered.png")
    Confirm_Not = os.path.join(pic_path, "Confirm_Not.png")
    Auc_Options = os.path.join(pic_path, "Auc_Options.png")
    Adv_Search_Screen = os.path.join(pic_path, "Adv_Search_Screen.png")
    Tag_Typed = os.path.join(pic_path, "Tag_Typed.png")
    FocusedSpade = os.path.join(pic_path, "Focusedspade.png")
    
    Net_Check = os.path.join(pic_path, "check.png")
    Net_Not = os.path.join(pic_path, "x.png")
    
    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Images loaded!"
    log.append(log_now)
except:
    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Failed to load images!"
    log.append(log_now)

class App(ttk.Frame):
    def __init__(self, parent, compound=tk.RIGHT):
        super().__init__(parent, padding=7)
        self.columnconfigure(1, weight=1)
        
        self.rowconfigure(0, weight=1)
        
        self.main_frame = ttk.Frame(self, style="Card.TFrame")
        self.main_frame.grid(row=0, rowspan=2, column=0, padx=10, pady=10, sticky="news")
        self.main_frame.rowconfigure(6, weight=1)
        
        self.start_button = ttk.Button(self.main_frame, text="Start", style="Accent.TButton", state="disabled", command=self.start)
        self.start_button.grid(row=0, column=0, ipadx=30, ipady=5, padx=7, pady=10, sticky="ew")  
        self.start_toggled = False    
         # Separator line
        # ==================                  
        self.separator_butt = ttk.Separator(self.main_frame)
        self.separator_butt.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
               
        self.verify_button = ttk.Button(self.main_frame, text="Setup", style="Toggle.TButton", command=self.verify)
        self.verify_button.grid(row=2, column=0, ipadx=30, ipady=5, padx=7, pady=10, sticky="ew")   
         
        self.readying = ttk.Button(self.main_frame, text="Ready", style="Toggle.TButton", state="disabled", command=self.get_ready)
        self.readying.grid(row=3, column=0, ipadx=30, ipady=5, padx=7, pady=(0,10), sticky="ew")  

        # ? Networking utilities
        # ? ==========================================

        self.network_frame = ttk.Frame(self)
        self.network_frame.grid(row=1, column=1, padx=10, pady=(0,10), sticky="news")
        
        self.connected_img = ImageTk.PhotoImage(PIL.Image.open(Net_Check).resize((40,40)))
        self.connect_disp = tk.Label(self.network_frame, image=self.connected_img)

        self.not_con_img = ImageTk.PhotoImage(PIL.Image.open(Net_Not).resize((40,40)))
        self.not_con_disp = tk.Label(self.network_frame, image=self.not_con_img)
        self.not_con_disp.grid(row=0, column=3, sticky="news")   
        
        # self.network_butt = ttk.Button(self.network_frame, text="Network", style="Toggle.TButton", command=self.butt_test)
        # self.network_butt.grid(row=0, column=1, padx=5, sticky="ew")
        
        self.net_connect = ttk.Button(self.network_frame, text="Connect", style="Toggle.TButton", command=self.start_networking)
        self.net_connect.grid(row=0, column=2, padx=5, sticky="ew")
        
        self.net_test = ttk.Button(self.network_frame, text="Network Test", style="Toggle.TButton", command=self.network_testing)
        self.net_test.grid(row=0, column=0, sticky="ew")
        # ? ==========================================
        # Separator line
        # ==================                  
        self.separator = ttk.Separator(self.main_frame)
        self.separator.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        
        # Toggle theme from light to dark
        # ==================           
        self.theme_toggle = ttk.Checkbutton(self.main_frame, text="Dark Theme", style="Switch.TCheckbutton", command=sv_ttk.toggle_theme)
        self.theme_toggle.grid(row=6, column=0, padx=10, pady=(0,10), sticky="s")  
        
        # Side frame that doesn't contain the main buttons
        # ==================           
        self.secondary_frame = ttk.Frame(self, style="Card.TFrame")
        self.secondary_frame.grid(row=0, column=1, padx=10, pady=10, sticky="news")
        self.secondary_frame.columnconfigure(0, weight=0)
        self.secondary_frame.columnconfigure(0, weight=1)
        self.secondary_frame.rowconfigure(0, weight=1)
        
        # ? Scrollable Listbox
        # ? ====================================                    
        self.listbox = tk.Listbox(self.secondary_frame, height=5, relief='flat')
        self.scrollbar = ttk.Scrollbar(self.secondary_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.config_listbox(yscrollcommand=self.scrollbar.set)
        self.__compound = compound
        self._grid_widgets()
        # ? ====================================                    
        # * Keeps track of the position of the debug display
        self.list_pos = 0
        
        
        for line in log:
            self.listbox.insert(self.list_pos, line)
            self.list_pos += 1

        self.is_verifying = False
        self.update()
        self.running_auc_checks = False
        
        self.auction_checks = 0

        # Only sends connection message upon initial connection
        self.net_start = True
        self.net_message = ""
        self.client_socket = socket()
        
        self.ready_to_start = False # Flag to see if verify and ready buttons have been successful 
        self.server_connection = False # Is this client connected to the comm server?
        self.computers_connected = False # Variable to keep track of whether or not the computers are linked
        
    # ? """Puts the two whole widgets in the correct position depending on compound."""
    # ? ====================================            
    def _grid_widgets(self):
        scrollbar_column = 0 if self.__compound is tk.LEFT else 1
        self.listbox.grid(row=0, column=0, padx=(10,0), pady=10, sticky="nswe")
        self.scrollbar.grid(row=0, column=scrollbar_column, padx=(0,10), pady=10, sticky="ns") 
    # ? ====================================    
    # ? """Configure resources of the Listbox widget."""
    # ? ====================================    
    def config_listbox(self, *args, **kwargs):
        self.listbox.configure(*args, **kwargs)   
    # ? ====================================  
    # ! ====================================  
    # ! Establishes server connection for communications
    # ! ====================================        
    def start_networking(self):
        self.list_pos += 1
        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Establishing network connection..."
        self.listbox.insert(self.list_pos, log_now) # Inserts messages into log
        self.listbox.yview("end")
        self.not_con_disp.grid_forget()
        self.connect_disp.grid(row=0, column=3, padx=3, sticky="ew")
        
        HOST = '192.168.86.36' # IPV4 address
        PORT = 33000
        if not PORT:
            PORT = 33000
        else:
            PORT = int(PORT)

        self.BUFSIZ = 1024
        ADDR = (HOST, PORT)

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(ADDR)

        # Thread handler for socket networking
        receive_thread = Thread(target=self.receive) 
        receive_thread.start()
        self.send()
    # ! ==================================== 
    # ! Receives messages on a separate thread so that GUI doesn't freeze
    # ! ==================================== 
    def receive(self):
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode("utf8") # Receives messages from server socket
                self.list_pos += 1
                log_now = msg
                self.listbox.insert(self.list_pos, log_now) # Inserts messages into log
                self.listbox.yview("end")
                if ("Seller-Computer" in log_now) and (not self.computers_connected):
                    self.computers_connected = True
                    if self.server_connection:
                        self.net_message = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Buyer-Computer already connected!"
                        msg = self.net_message
                        self.client_socket.send(bytes(msg, "utf8")) # Sends messages through socket
                
                if "start_buying" in log_now:
                    self.verify_button.config(state="enabled")
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<< BEGINNING BUY SEQUENCE >>>"
                    self.listbox.insert(self.list_pos, log_now) # Inserts messages into log
                    self.listbox.yview("end")
                    self.update()
                    self.start()
            except OSError:  # Possibly client has left the chat.
                break
    # ! ==================================== 
    # ! Sends messages to server that other client will receive
    # ! ====================================             
    def send(self, event=None):  # event is passed by binders.
        # Prints message only on connection so that both clients know who's connected
        if self.net_start:
            self.net_message = " - [This is a placeholder message.]"
            self.net_start = False
            msg = " - Buyer-Computer is connected to server!"
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + msg
            self.listbox.insert(self.list_pos, log_now) # Inserts messages into log
            self.listbox.yview("end")
            self.client_socket.send(bytes(msg, "utf8")) # Sends messages through socket
            self.server_connection = True
        else:
            msg = self.net_message # Gets input from this client to send to server
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + msg
            self.client_socket.send(bytes(log_now, "utf8")) # Sends messages through socket
            # Closes socket connection if client sends a 'quit' message
            if msg == "{quit}":
                self.client_socket.close()
    # ! ==================================== 
    # ! Closes socket connection as needed
    # ! ==================================== 
    def on_closing(self, event=None):
        self.net_message = "{quit}"
        self.net_start = True
        self.send() # Sends quit message to server to close socket
    # ! ====================================
    # ! ====================================
        # ! Networking stuff
    # ! ====================================
    def network_testing(self):
        self.net_message = " --| Buyer computer test! |--"
        self.send()
    # ! ====================================
    # ? =======================================================================
    # ? Types Cody's gamertag in before starting auction search to make auction access quicker
    # ? =======================================================================
    def verify(self):
        if window_exist:
            forza.activate() # Bring program into focus
            time.sleep(.05)
            forza.maximize() # Make program full screen
            time.sleep(.05)
            self.net_message = " - Buyer system is verifying access!"
            self.send()
            # ! Checks to see if game is on main auction access button
            # ! ==============================================================================
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for auction access screen..."
            self.listbox.insert(self.list_pos, log_now) 
            self.listbox.yview("end")
            self.update()
            self.start_time = time.time()
            while True:
                self.first_screen_look = pyautogui.locateOnScreen(First_Screen, confidence=.8)
                if self.first_screen_look:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Auction access found!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    pyautogui.press('enter')
                    break                    
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                    
                    if self.temp == 6:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Not on Auction button!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Auction button check took too long!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.start_toggled == False
                        self.start_button.configure(text="Start", style="Toggle.TButton")
                        return
                self.update()
                
            self.search_result = False
            # ! Checks to see if basic search screen is visible
            # ! ===================================
            self.start_time = time.time()
            while True:
                self.base_search_look = pyautogui.locateOnScreen(Base_Search, confidence=.8)
                if self.base_search_look:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Base search screen found!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.search_result = True
                    break
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                            
                    if self.temp == 5:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Search screen took too long!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        return
            # ! ===================================     
            # ! If the search screen exists, then press x to access advanced search
            # ! ===================================   
            if self.search_result:
                pyautogui.press('x')
                # ! =================================== 
                # ! Checks advanced screen for gamertag search option and selects it if available
                # ! ===================================        
                self.start_time = time.time()
                while True:
                    self.adv_search_look = pyautogui.locateOnScreen(Adv_Search, confidence=.8)
                    self.adv_tag_hovered = pyautogui.locateOnScreen(Adv_Tag_Hovered, confidence=.8)
                    
                    if self.adv_search_look:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Advanced search screen found!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        pyautogui.click(self.adv_search_look)
                        break
                    
                    elif self.adv_tag_hovered:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Advanced search screen hovered tag found!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        pyautogui.click(self.adv_tag_hovered)
                        break
                    
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                        
                        if self.temp == 5:
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Advanced search screen took too long!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.listbox.yview("end")
                            return
                    self.update()
                # ! ===================================
                # ! ===================================
                # ! Checks to see if Cody's gamertag has already been entered so program doesn't try to type it twice
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for gamertag..."
                self.listbox.insert(self.list_pos, log_now)      
                self.listbox.yview("end")
                self.update()
                self.start_time = time.time()
                while True:
                    self.tag_typed_look = pyautogui.locateOnScreen(Tag_Typed, confidence=.8)
                    self.tag_not_look = pyautogui.locateOnScreen(FocusedSpade, confidence=.8)
                    if self.tag_typed_look:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Gamertag already typed!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - --< Initial auction setup done! >--"
                        self.listbox.insert(self.list_pos, log_now)
                        self.readying.config(state="enabled")
                        self.listbox.yview("end")
                        self.update()
                        pyautogui.press('esc')
                        return
                    elif self.tag_not_look:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Gamertag already typed!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - --< Initial auction setup done! >--"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.readying.config(state="enabled")
                        self.update()
                        pyautogui.press('esc')
                        return
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                        
                        if self.temp == 2:
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Gamertag not typed!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.listbox.yview("end")
                            break                        
                # ! ===================================
                # ! ===================================
                # ! Types in Cody's gamertag so that it can be searched
                pyautogui.press('enter')
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Trying to type gamertag..."
                self.listbox.insert(self.list_pos, log_now)   
                self.listbox.yview("end")
                self.update()
                self.start_time = time.time()
                while True:
                    self.man_key_look = pyautogui.locateOnScreen(Man_Key, confidence=.8)
                    if self.man_key_look:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Typing in Cody's gamertag!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        pyautogui.write('focusedspade', interval = 0.04)
                        pyautogui.press('enter')
                        self.update()
                        break    
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                        if self.temp == 5:
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Manual keyword search took too long!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.listbox.yview("end")
                            return  
                    self.update()
                # ! ===================================
                # ! Goes back to main screen for actual auction program to search
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for advanced search screen..."
                self.listbox.insert(self.list_pos, log_now)  
                self.listbox.yview("end") 
                self.update()
                self.start_time = time.time()
                while True:
                    self.adv_screen_look = pyautogui.locateOnScreen(Adv_Search_Screen, confidence=.95)
                    if self.adv_screen_look:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - On advanced search screen!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Going back to starting auction screen!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        pyautogui.press('esc')
                        self.update()
                        break
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                        if self.temp == 5:
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Advanced search took too long to load!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.listbox.yview("end")
                            return  
                    self.update()
                # ! ===================================
            else:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Couldn't find search screen!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.start_toggled == False
                self.start_button.configure(text="Start", style="Toggle.TButton")
                # ! ==============================================================================  
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - --< Initial auction setup done! >--"
            self.listbox.insert(self.list_pos, log_now)    
            self.listbox.yview("end")
            self.readying.config(state="enabled") 
        else:
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Game isn't open, can't verify!"
            self.listbox.insert(self.list_pos, log_now)
            self.listbox.yview("end")
            self.start_toggled == False
            self.start_button.configure(text="Start", style="Toggle.TButton")
            

    # ? =======================================================================    
    # ? =======================================================================
    def start(self):
        if self.start_toggled == False:
            self.start_toggled = True
            self.start_button.configure(text="Stop", style="Accent.TButton")
        else:
            self.start_toggled == False
            self.start_button.configure(text="Start", style="Toggle.TButton")
        
        self.readying.config(state="disabled")
        self.main_function()
    
    def get_ready(self):
        if window_exist:
            forza.activate() # Bring program into focus
            time.sleep(.05)
            forza.maximize() # Make program full screen
            time.sleep(.05)
            self.net_message = " - Buyer system is getting ready for auction!"
            self.send()
            self.correct_starting_point = True
            # ! ===================================
            # ! Checks to make sure program is back on advanced search screen before continuing
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for advanced search screen..."
            self.listbox.insert(self.list_pos, log_now)            
            self.update()
            self.start_time = time.time()
            while True:
                self.adv_screen_look = pyautogui.locateOnScreen(Adv_Search_Screen, confidence=.95)
                if self.adv_screen_look:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - On advanced search screen!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.update()
                    self.correct_starting_point = True
                    break
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                    if self.temp == 1:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Advanced search took too long to load!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.start_toggled == False
                        self.correct_starting_point = False
                        break
                self.update()
            if not self.correct_starting_point:
                # ! ===================================
                # ! Checks to see if game is on main auction access button
                # ! ==============================================================================
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for auction access screen..."
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                self.start_time = time.time()
                while True:
                    self.first_screen_look = pyautogui.locateOnScreen(First_Screen, confidence=.8)
                    if self.first_screen_look:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Auction access found!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        pyautogui.press('enter')
                        self.correct_starting_point = False
                        break                    
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                        
                        if self.temp == 1:
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Not on Auction button!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.listbox.yview("end")
                            break
                    self.update()
                # ! Checks to see if basic search screen is visible
                # ! ===================================
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for base search screen..."
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.start_time = time.time()
                while True:
                    self.base_search_look = pyautogui.locateOnScreen(Base_Search, confidence=.8)
                    if self.base_search_look:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Base search screen found!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.correct_starting_point = False
                        break
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                                
                        if self.temp == 1:
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Search screen took too long!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.listbox.yview("end")
                            return
                    self.update()
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Accessing advanced search!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                pyautogui.press('x')
                self.update()
                # ! ===================================
                # ! Checks to make sure program is back on advanced search screen before continuing
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for advanced search screen..."
                self.listbox.insert(self.list_pos, log_now)    
                self.update()
                self.start_time = time.time()
                while True:
                    self.adv_screen_look = pyautogui.locateOnScreen(Adv_Search_Screen, confidence=.95)
                    if self.adv_screen_look:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - On advanced search screen!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.update()
                        break
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                        if self.temp == 5:
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Advanced search took too long to load!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.start_toggled == False
                            self.start_button.configure(text="Start", style="Toggle.TButton")  
                            self.listbox.yview("end")
                            return  
                    self.update()
                # ! ===================================
            else:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - --< Ready to access auctions! >--"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                self.ready_to_start = True
                self.net_message = " - seller_access"
                self.send()
                if self.ready_to_start and self.computers_connected and self.server_connection:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<| Buyer system is ready for auction! |>>"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.update()   
                else:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<< Something is not ready for auction to start >>>"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.update()  
                return

            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - --< Ready to access auctions! >--"
            self.listbox.insert(self.list_pos, log_now)
            self.ready_to_start = True
            self.net_message = "seller_access"
            self.send()
            self.listbox.yview("end")
            self.update()
            
            if self.ready_to_start and self.computers_connected and self.server_connection:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<| Buyer system is ready for auction! |>>"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()   
            else:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<< Something is not ready for auction to start >>>"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()                

        else:
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Game isn't open, can't verify!"
            self.listbox.insert(self.list_pos, log_now) 
            self.listbox.yview("end")
            return
        
        if self.running_auc_checks:
            self.main_function()
    # ? =======================================================================    
    # ? =======================================================================
    def main_function(self):
        if window_exist:
            if self.auction_checks == 0:
                forza.activate() # Bring program into focus
                time.sleep(.05)
                forza.maximize() # Make program full screen
                time.sleep(.05)
            
            if self.auction_checks == 3:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Checked for auctions too many times!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.start_toggled == False
                self.start_button.configure(text="Start", style="Toggle.TButton")  
                return   
            self.auction_checks += 1   
            pyautogui.press('x')
            # ! ===================================
            # ! Checks to make sure program is back on advanced search screen before continuing
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for advanced search screen..."
            self.listbox.insert(self.list_pos, log_now)    
            self.listbox.yview("end")
            self.update()
            self.start_time = time.time()
            while True:
                self.adv_screen_look = pyautogui.locateOnScreen(Adv_Search_Screen, confidence=.95)
                if self.adv_screen_look:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - On advanced search screen!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.update()
                    pyautogui.press('enter')
                    self.look_for_auction()
                    break
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                    if self.temp == 5:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Advanced search took too long to load!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.start_toggled == False
                        self.start_button.configure(text="Start", style="Toggle.TButton")  
                        return  
                self.update()
            # ! ===================================             
        else:
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Game isn't open, can't verify!"
            self.listbox.insert(self.list_pos, log_now)
            self.listbox.yview("end")
            self.start_toggled == False
            self.start_button.configure(text="Start", style="Toggle.TButton")   
    # ? =======================================================================
    # ? =======================================================================    
    def look_for_auction(self):
        # [get_to_search] -> No_Auc (if not true) -> if:Auc_Buy elif:Auc_Buy_Hovered -> [buy_car]
        # ! ===================================
        # ! Looks to see if there are any auctions available and will attempt purchase if there are
        self.list_pos += 1
        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Looking for auctions..."
        self.listbox.insert(self.list_pos, log_now)    
        self.listbox.yview("end")
        self.start_time = time.time()
        while True:
            self.no_auc_look = pyautogui.locateOnScreen(No_Auc, confidence=.7)
            self.auc_options_look = pyautogui.locateOnScreen(Auc_Options, confidence=.75)
            if self.no_auc_look:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - No auctions to display!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                pyautogui.press('esc')
                self.update()
                self.running_auc_checks = True
                self.get_ready()
                break    
            elif self.auc_options_look:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Auction found!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                pyautogui.press('y')
                self.update()
                self.buy_car()
                break
            else:
                self.current_time = time.time()
                self.lapsed = self.current_time - self.start_time
                self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Waiting for auctions to load..."
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                if self.temp == 10:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Auctions took too long to load!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    pyautogui.press('esc')
                    self.start_toggled == False
                    self.start_button.configure(text="Start", style="Toggle.TButton")
                    self.update()
                    self.running_auc_checks = True
                    self.get_ready()
                    return  
            self.update()
        # ! ===================================
    # ? =======================================================================
    def buy_car(self):
        # [look_for_auction] - > if:Buyout_N elif:Buyout_Y -> Buy_Success -> if:Collect_Yes elif:Collect_No -> Claiming
        # ! ===================================
        # ! Tries to buy car if able to
        self.list_pos += 1
        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Attempting to buy..."
        self.listbox.insert(self.list_pos, log_now) 
        self.listbox.yview("end")
        self.update()   
        self.start_time = time.time()
        while True:
            self.auc_buy_look = pyautogui.locateOnScreen(Auc_Buy, confidence=.8)
            self.auc_buy_hovered_look = pyautogui.locateOnScreen(Auc_Buy_Hovered, confidence=.8)
            if self.auc_buy_look:
                pyautogui.click(self.auc_buy_look)
                pyautogui.press('enter')
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Attempting buyout!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                break
            elif self.auc_buy_hovered_look:
                pyautogui.press('enter')
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Attempting buyout!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                break
            else:
                self.current_time = time.time()
                self.lapsed = self.current_time - self.start_time
                self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                if self.temp == 5:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Accessing auction took too long!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.start_toggled == False
                    self.start_button.configure(text="Start", style="Toggle.TButton")
                    return  
        # ! ===================================
        # ! ===================================
        # ! Presses yes to confirm buyout
        self.list_pos += 1
        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Working on purchase..."
        self.listbox.insert(self.list_pos, log_now)   
        self.listbox.yview("end")
        self.update() 
        self.start_time = time.time()
        while True:
            self.buyout_y_look = pyautogui.locateOnScreen(Buyout_Y, confidence=.8)
            self.buyout_n_look = pyautogui.locateOnScreen(Buyout_N, confidence=.8)
            if self.buyout_y_look:
                pyautogui.press('enter')
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Trying to purchase!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                break
            elif self.buyout_n_look:
                pyautogui.click(self.buyout_n_look)
                pyautogui.press('enter')
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Trying to purchase!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                break
            else:
                self.current_time = time.time()
                self.lapsed = self.current_time - self.start_time
                self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                if self.temp == 5:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Purchase attempt took too long!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.start_toggled == False
                    self.start_button.configure(text="Start", style="Toggle.TButton")
                    return     
        # ! ===================================
        # ! ===================================
        # ! Checks for buyout successful screen to see if buyout worked
        self.list_pos += 1
        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Checking if buyout was successful..."
        self.listbox.insert(self.list_pos, log_now)
        self.listbox.yview("end")
        self.update()    
        self.start_time = time.time()
        while True:
            self.buy_success_look = pyautogui.locateOnScreen(Buy_Success, confidence=.8)
            if self.buy_success_look:
                pyautogui.press('enter')
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car successfully purchased!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                break
            else:
                self.current_time = time.time()
                self.lapsed = self.current_time - self.start_time
                self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                if self.temp == 5:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Buyout taking took too long!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.start_toggled == False
                    self.start_button.configure(text="Start", style="Toggle.TButton")
                    return 
        # ! ===================================
        # ! ===================================
        # ! Collects car if buyout was successful
        self.list_pos += 1
        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Trying to collect car..."
        self.listbox.insert(self.list_pos, log_now)    
        self.listbox.yview("end")
        self.update()
        self.start_time = time.time()
        while True:
            self.collect_yes_look = pyautogui.locateOnScreen(Collect_Yes, confidence=.8)
            self.collect_no_look = pyautogui.locateOnScreen(Collect_Not, confidence=.8)
            if self.collect_yes_look:
                pyautogui.press('enter')
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Collecting purchased car!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                break
            elif self.collect_no_look:
                pyautogui.click(self.collect_no_look)
                pyautogui.press('enter')
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Collecting purchased car!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                break
            else:
                self.current_time = time.time()
                self.lapsed = self.current_time - self.start_time
                self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                if self.temp == 5:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Collecting car took too long!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.start_toggled == False
                    self.start_button.configure(text="Start", style="Toggle.TButton")
                    return 
        # ! ===================================
        # ! ===================================
        # ! Checks to see if claiming car was successful
        self.list_pos += 1
        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Was the car claimed...?"
        self.listbox.insert(self.list_pos, log_now)
        self.update()    
        self.start_time = time.time()
        while True:
            self.claiming_look = pyautogui.locateOnScreen(Claiming, confidence=.8)        
            if self.claiming_look:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Congratulations on your new car!"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                return
            else:
                self.current_time = time.time()
                self.lapsed = self.current_time - self.start_time
                self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                if self.temp == 5:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Claiming car is taking forever!"
                    self.listbox.insert(self.list_pos, log_now)
                    self.listbox.yview("end")
                    self.start_toggled == False
                    self.start_button.configure(text="Start", style="Toggle.TButton")
                    return                 
        # ! ===================================
    # ? =======================================================================           
# ! Program startup
# ! --------------------------------------
if __name__ == "__main__":
    
    
    
    app = tk.Tk()
    app.title("FH5 Buyer")
    app.geometry(f"{600}x{325}")
    app.iconbitmap("cookie.ico")

    sv_ttk.set_theme("light")
        
    App(app).pack(expand=True, fill="both")
    app.mainloop()
# ! --------------------------------------