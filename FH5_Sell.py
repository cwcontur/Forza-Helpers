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
    Confirm_Hovered = os.path.join(pic_path, "Confirm_Hovered.png") # Create Auction -> Confirm
    Confirm_Not = os.path.join(pic_path, "Confirm_Not.png") # Create Auction -> Confirm
    Auc_Car_Hovered = os.path.join(pic_path, "Auc_Car_Hovered.png") # Starting screen for program
    Create_Auction = os.path.join(pic_path, "Create_Auction.png") # Auc_Car_hovered -> Create Auction
    Starting_Auction = os.path.join(pic_path, "Starting_Auction.png") # Confirm -> Starting Auction
    Live_Auction = os.path.join(pic_path, "Live_Auction.png") # Starting Auction -> Live Auction -> [Message Buyer Client]
    
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
        
        self.start_button = ttk.Button(self.main_frame, text="Start Auction", style="Accent.TButton", state="disabled")
        self.start_button.grid(row=0, column=0, ipady=5, padx=7, pady=10, sticky="ew")  
        self.start_toggled = False  
         
        # Separator line
        # ==================                  
        self.separator_butt = ttk.Separator(self.main_frame)
        self.separator_butt.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        self.verify_button = ttk.Button(self.main_frame, text="Verify", style="Toggle.TButton")
        self.verify_button.grid(row=2, column=0, ipadx=30, ipady=5, padx=7, pady=10, sticky="ew")     

        self.readying = ttk.Button(self.main_frame, text="Ready", style="Toggle.TButton", state="disabled")
        self.readying.grid(row=3, column=0, ipadx=30, ipady=5, padx=7, pady=10, sticky="ew")    

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
                    print("slut")
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
            msg = "Seller-Computer is connected to server!"
            self.list_pos += 1
            log_now = str(datetime.utcnow().strftime('%H:%M:%S')) + msg
            self.listbox.insert(self.list_pos, log_now) # Inserts messages into log
            self.listbox.yview("end")
            self.client_socket.send(bytes(msg, "utf8")) # Sends messages through socket
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
        
                        
# ! Program startup
# ! --------------------------------------
if __name__ == "__main__":

    app = tk.Tk()
    app.title("FH5 Seller")
    app.geometry(f"{600}x{325}")
    app.iconbitmap("cookie.ico")

    sv_ttk.set_theme("light")
        
    App(app).pack(expand=True, fill="both")
    app.mainloop()
# ! --------------------------------------