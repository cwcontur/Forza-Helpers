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
        log_now = str(datetime.utcnow().strftime('%H:%M:%S') + " - Game window found!")
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
    Confirm_Hovered = os.path.join(pic_path, "Confirm_Hovered.png") # Create Auction -> Confirm
    Confirm_Not = os.path.join(pic_path, "Confirm_Not.png") # Create Auction -> Confirm
    Auc_Car_Hovered = os.path.join(pic_path, "Auc_Car_Hovered.png") # Starting screen for program
    Auc_Car_Not = os.path.join(pic_path, "Auc_Car_Not.png") # Starting screen for program
    Create_Auction = os.path.join(pic_path, "Create_Auction.png") # Auc_Car_hovered -> Create Auction
    Starting_Auction = os.path.join(pic_path, "Starting_Auction.png") # Confirm -> Starting Auction
    Live_Auction = os.path.join(pic_path, "Live_Auction.png") # Starting Auction -> Live Auction -> [Message Buyer Client]
    Initial_Price_Hovered = os.path.join(pic_path, "Initial_Price_Hovered.png") # [left arrow] until Minimum Buy
    Initial_Price_Not = os.path.join(pic_path, "Initial_Price_Not.png")
    Buyout_Price_Not = os.path.join(pic_path, "Buyout_Price_Not.png") # [enter] -> Click -> set Minimum price
    Buyout_Price_Hovered = os.path.join(pic_path, "Buyout_Price_Hovered.png")
    Auction_Car_Not = os.path.join(pic_path, "Auction_Car_Not.png") # [enter] -> Initial Price
    Auction_Car_Hovered = os.path.join(pic_path, "Auction_Car_Hovered.png")
    Minimum_Buy_Not = os.path.join(pic_path, "Minimum_Buy_Not.png") 
    Minimum_Buy_Hovered = os.path.join(pic_path, "Minimum_Buy_Hovered.png") # Confirm -> Starting auction
    
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
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)
        
        self.main_frame = ttk.Frame(self, style="Card.TFrame")
        self.main_frame.grid(row=0, rowspan=2, column=1, padx=10, pady=10, sticky="news")
        self.main_frame.rowconfigure(6, weight=1)
        
        self.start_button = ttk.Button(self.main_frame, text="Start Auction", style="Accent.TButton", state="disabled", command=self.start_system)
        self.start_button.grid(row=0, column=0, ipady=5, padx=7, pady=10, sticky="ew")  
        self.start_toggled = False  
         
        # Separator line
        # ==================                  
        self.separator_butt = ttk.Separator(self.main_frame)
        self.separator_butt.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        self.verify_button = ttk.Button(self.main_frame, text="Verify", style="Toggle.TButton", state="disabled", command=self.verifying)
        self.verify_button.grid(row=2, column=0, ipadx=30, ipady=5, padx=7, pady=10, sticky="ew")     

        self.readying = ttk.Button(self.main_frame, text="Ready", style="Toggle.TButton", state="disabled", command=self.getting_ready)
        self.readying.grid(row=3, column=0, ipadx=30, ipady=5, padx=7, pady=10, sticky="ew")    

        # ? Networking utilities
        # ? ==========================================
        self.network_frame = ttk.Frame(self)
        self.network_frame.grid(row=1, column=0, padx=10, pady=(0,10), sticky="news")
        
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
        self.secondary_frame.grid(row=0, column=0, padx=10, pady=10, sticky="news")
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

        self.list_pos += 1
        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Buyer operation must be ready first!"
        self.listbox.insert(self.list_pos, log_now) # Inserts messages into log
        self.listbox.yview("end")
        
        self.is_verified = False
        self.update()
        # self.running_auc_checks = False
        
        # self.auction_checks = 0

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
    # ! Networking stuff
    # ! ====================================
    def network_testing(self):
        self.net_message = " --< Seller-Computer ready to sell! >--"
        self.send()
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
                if "Buyer-Computer" in log_now:
                    self.computers_connected = True
                    if self.server_connection:
                        self.net_message = " - Seller-Computer already connected!"
                        msg = self.net_message
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + msg
                        self.listbox.insert(self.list_pos, log_now) # Inserts messages into log
                        self.listbox.yview("end")
                        self.client_socket.send(bytes(msg, "utf8")) # Sends messages through socket
                if "seller_access" in log_now:
                    self.verify_button.config(state="enabled")
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Buyer system has finished readying!"
                    self.listbox.insert(self.list_pos, log_now) # Inserts messages into log
                    self.listbox.yview("end")
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
            msg = " - Seller-Computer is connected to server!"
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
    def verifying(self):
        if window_exist:
            forza.activate() # Bring program into focus
            time.sleep(.05)
            forza.maximize() # Make program full screen
            time.sleep(.05)
            self.net_message = " - Seller system is verifying access!"
            self.send()
            # ! Checks for initial auction car button to begin auctioning vehicle
            # ! ===============================================
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Checking for Auction Car button..."
            self.listbox.insert(self.list_pos, log_now)  
            self.listbox.yview("end") 
            self.update()
            self.start_time = time.time()
            while True:
                self.auction_car_not_looking = pyautogui.locateOnScreen(Auc_Car_Not, confidence=.8)
                self.auction_car_hovered_looking = pyautogui.locateOnScreen(Auc_Car_Hovered, confidence=.8)
                if self.auction_car_not_looking:
                    pyautogui.click(self.auction_car_not_looking)
                    pyautogui.press('enter')
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Auction Car button found!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.update()
                    break
                elif self.auction_car_hovered_looking:
                    pyautogui.press('enter')
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Auction Car button found!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.update()
                    break
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                    
                    if self.temp == 3: # 3 second wait time
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - No Auction Car button!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        return
                self.update()
            # ! ===============================================
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Checking for Auction Car button..."
            self.listbox.insert(self.list_pos, log_now)  
            self.listbox.yview("end") 
            self.update()
            self.start_time = time.time()
            while True:
                self.create_auction_looking = pyautogui.locateOnScreen(Create_Auction, confidence=.8)
                if self.create_auction_looking:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - On creating auction screen!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.update()
                    break
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                    
                    if self.temp == 3: # 3 second wait time
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Create auction screen not found!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        return
                self.update()
            
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - --< Auction access verified! >--"
            self.listbox.insert(self.list_pos, log_now)
            self.listbox.yview("end")
            self.update()   
            self.net_message = log_now
            self.send()
            self.readying.config(state="enabled")   
            self.is_verified = True
        else:
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Game isn't open, can't verify!"
            self.listbox.insert(self.list_pos, log_now)
            self.listbox.yview("end")
            self.start_toggled == False
            self.start_button.configure(text="Start", style="Toggle.TButton")

    def getting_ready(self):
        if window_exist:
            forza.activate() # Bring program into focus
            time.sleep(.05)
            forza.maximize() # Make program full screen
            time.sleep(.05)
            self.net_message = " - Seller system is getting ready for auction!"
            self.send()
            # ! Checks for car pricing option and sees if the price is at its lowest or not
            # ! ===============================================
            self.not_at_min = False
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Seeing if car price is at its minimum..."
            self.listbox.insert(self.list_pos, log_now)  
            self.listbox.yview("end") 
            self.update()
            self.start_time = time.time()
            while True:
                self.initial_price_hovered_looking = pyautogui.locateOnScreen(Initial_Price_Hovered, confidence=.8)
                self.initial_price_not_looking = pyautogui.locateOnScreen(Initial_Price_Not, confidence=.8)
                self.min_buy_not_looking = pyautogui.locateOnScreen(Minimum_Buy_Not, confidence=.8)
                self.min_buy_hovered_looking = pyautogui.locateOnScreen(Minimum_Buy_Hovered, confidence=.8)
                
                if self.initial_price_hovered_looking:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car price needs to be lowered!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.not_at_min = True
                    self.update()
                    break
                elif self.initial_price_not_looking:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car price needs to be lowered!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.not_at_min = True # Button needs to be hovered before price can be adjusted
                    self.update()
                    break
                elif self.min_buy_not_looking:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car price already lowered!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.not_at_min = False
                    self.update()
                    break
                elif self.min_buy_hovered_looking:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car price already lowered!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.not_at_min = False
                    self.update()
                    break
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                    
                    if self.temp == 3: # 3 second wait time
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Can't find car pricing needing adjustment!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        return
                self.update()
                
            self.ready_to_adjust = False # Flag for whether or not price can be lowered
            # ! Checks for buyout price selection so that price can be adjusted accordingly
            # ! ===============================================
            if self.not_at_min:
                # ! ===============================================
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Seeing if car price is at its minimum..."
                self.listbox.insert(self.list_pos, log_now)  
                self.listbox.yview("end") 
                self.update()
                self.start_time = time.time()
                while True:
                    self.buyout_price_hovered_looking = pyautogui.locateOnScreen(Buyout_Price_Hovered, confidence=.8)
                    self.buyout_price_not_looking = pyautogui.locateOnScreen(Buyout_Price_Not, confidence=.8)
                    if self.buyout_price_hovered_looking:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car price will now be adjusted!"
                        self.listbox.insert(self.list_pos, log_now)  
                        self.listbox.yview("end") 
                        self.update()
                        self.ready_to_adjust = True
                        break
                    elif self.buyout_price_not_looking:
                        pyautogui.click(self.buyout_price_not_looking)
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car price will now be adjusted!"
                        self.listbox.insert(self.list_pos, log_now)  
                        self.listbox.yview("end") 
                        self.update()
                        self.ready_to_adjust = True
                        break
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                        
                        if self.temp == 3: # 3 second wait time
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Unable find buyout price for adjusting!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.listbox.yview("end")
                            return
                    self.update()
                # ! ===============================================
            else:
                # ! Hovers over confirm button to make car auction go live for purchase
                # ! ===============================================
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Seeing if car price is at its minimum..."
                self.listbox.insert(self.list_pos, log_now)  
                self.listbox.yview("end") 
                self.update()
                self.start_time = time.time()
                while True:
                    self.confirm_hovered_looking = pyautogui.locateOnScreen(Confirm_Hovered, confidence=.8)
                    self.confirm_not_looking = pyautogui.locateOnScreen(Confirm_Not, confidence=.8)
                    
                    if self.confirm_hovered_looking:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car is ready to go to live for sale!"
                        self.listbox.insert(self.list_pos, log_now)  
                        self.listbox.yview("end") 
                        self.update()
                        break
                    elif self.confirm_not_looking:
                        pyautogui.click(self.confirm_not_looking)
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car is ready to go to live for sale!"
                        self.listbox.insert(self.list_pos, log_now)  
                        self.listbox.yview("end") 
                        self.update()
                        break
                    else:
                        self.current_time = time.time()
                        self.lapsed = self.current_time - self.start_time
                        self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                        
                        if self.temp == 3: # 3 second wait time
                            self.list_pos += 1
                            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Unable find buyout price for adjusting!"
                            self.listbox.insert(self.list_pos, log_now)
                            self.listbox.yview("end")
                            return
                    self.update()
                self.ready_to_start = True
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - --< Auction ready to go live! >--"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                self.net_message = log_now
                self.send()
                return
                # ! ===============================================
            # ! Adjusts car pricing to its minimum
            # ! ===============================================
            self.not_at_min = False
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Seeing if car price is at its minimum..."
            self.listbox.insert(self.list_pos, log_now)  
            self.listbox.yview("end") 
            self.update()
            self.start_time = time.time()
            while True:
                self.initial_price_hovered_looking = pyautogui.locateOnScreen(Initial_Price_Hovered, confidence=.8)
                self.min_buy_hovered_looking = pyautogui.locateOnScreen(Minimum_Buy_Hovered, confidence=.8)
                if self.initial_price_hovered_looking:
                    pyautogui.press('left arrow')
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Price lowered..."
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.update()
                elif self.min_buy_hovered_looking:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Price lowered all the way!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.update()
                    break
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                    
                    if self.temp == 3: # 3 second wait time
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Unable to lower buyout price!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        return
                self.update()
            # ! ===============================================
            # ! Hovers over confirm button to make car auction go live for purchase
            # ! ===============================================
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Seeing if car price is at its minimum..."
            self.listbox.insert(self.list_pos, log_now)  
            self.listbox.yview("end") 
            self.update()
            self.start_time = time.time()
            while True:
                self.confirm_hovered_looking = pyautogui.locateOnScreen(Confirm_Hovered, confidence=.8)
                self.confirm_not_looking = pyautogui.locateOnScreen(Confirm_Not, confidence=.8)
                
                if self.confirm_hovered_looking:
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car is ready to go to live for sale!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.update()
                    break
                elif self.confirm_not_looking:
                    pyautogui.click(self.confirm_not_looking)
                    self.list_pos += 1
                    log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Car is ready to go to live for sale!"
                    self.listbox.insert(self.list_pos, log_now)  
                    self.listbox.yview("end") 
                    self.update()
                    break
                else:
                    self.current_time = time.time()
                    self.lapsed = self.current_time - self.start_time
                    self.temp = int(time.strftime("%S", time.gmtime(self.lapsed)))
                    
                    if self.temp == 3: # 3 second wait time
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Unable find buyout price for adjusting!"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        return
                self.update()
            # ! ===============================================
            self.ready_to_start = True
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - --< Auction ready to go live! >--"
            self.listbox.insert(self.list_pos, log_now)
            self.listbox.yview("end")
            self.update()
            self.net_message = log_now
            self.send()
            if self.ready_to_start and self.computers_connected and self.server_connection:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<| Both systems are ready for auction! |>>"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update() 
            return
        else:
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Game isn't open, can't verify!"
            self.listbox.insert(self.list_pos, log_now)
            self.listbox.yview("end")
            self.start_toggled == False
            self.start_button.configure(text="Start", style="Toggle.TButton")
    
    def start_system(self):
        if window_exist:
            forza.activate() # Bring program into focus
            time.sleep(.05)
            forza.maximize() # Make program full screen
            time.sleep(.05)
            self.net_message = " - Seller system is ABOUT TO START AUCTION!"
            self.send()
            if self.ready_to_start and self.computers_connected and self.server_connection:
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<< AUCTION ABOUT TO GO LIVE >>>"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update() 
                pyautogui.press('enter')
                # ! ===================================
                # ! CHECKING IF AUCTION IS BEING STARTED
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Is the auction starting???"
                self.listbox.insert(self.list_pos, log_now)    
                self.update()
                while True:
                    self.starting_auction_looking = pyautogui.locateOnScreen(Starting_Auction, confidence=.85)
                    if self.starting_auction_looking:
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - << AUCTION IS STARTING! >>"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.update()
                        break
                    self.update()
                
                # ! ===================================
                # ! CHECKING IF AUCTION IS BEING STARTED
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Is the auction starting???"
                self.listbox.insert(self.list_pos, log_now)    
                self.update()
                while True:
                    self.live_auction_looking = pyautogui.locateOnScreen(Live_Auction, confidence=.85)
                    if self.live_auction_looking:
                        self.net_message = "start_buying"
                        self.send()
                        self.list_pos += 1
                        log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<< AUCTION IS LIVE!!!!!!! >>>"
                        self.listbox.insert(self.list_pos, log_now)
                        self.listbox.yview("end")
                        self.update()
                        break
                    self.update()
                    
                return
            else: 
                self.list_pos += 1
                log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - <<< Something is not ready for auction to start >>>"
                self.listbox.insert(self.list_pos, log_now)
                self.listbox.yview("end")
                self.update()
                return
        else:
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + " - Game isn't open, can't verify!"
            self.listbox.insert(self.list_pos, log_now) 
            self.listbox.yview("end")
            return            
# ! Program startup
# ! --------------------------------------
if __name__ == "__main__":

    app = tk.Tk()
    app.title("FH5 Seller")
    app.geometry(f"{600}x{325}")
    app.iconbitmap("seller.ico")

    sv_ttk.set_theme("light")
        
    App(app).pack(expand=True, fill="both")
    app.mainloop()
# ! --------------------------------------