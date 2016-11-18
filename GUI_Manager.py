#Version 0.0.1
from Tkinter import *
import tkFont
from PIL import ImageTk, Image
from soundHandler import soundHandler
#from UserFile_Handler import UserFile_Handler

class GUI_Manager:
    #userFile = UserFile_Handler()  #object for userfile. used for getting save files and creating new saves
    soundPlayer = soundHandler()    #object for soundHandler. used to play music and sound effects
    
    y = 50  #y coordinate to place text on canvas
    def __init__(self,master = None):
        self.startScreen = Frame(master)                    #Create a frame to hold stuff for startScreen
        self.root = master                                  #Save tk object to loal var 
        self.startScreen.config(height = 500, width = 500)  #Set dimensions for start screen
        master.resizable(width = False, height = False)     #Make window not resizable 
        self.startScreen.pack()                             #pack strartscreen into window

    #Method creates the startscreen for the game
    def startMenu(self):
        buttonFont = tkFont.Font(size = 24)                 #Create custom font for buttons
        titleFont = tkFont.Font(size = 30)                  #Create custom font for buttons
        buttonStart = Button(self.startScreen, text = "New Game",command = lambda: self.startGame(),font = buttonFont)  #created button for start screen 
        buttonStart.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .20)                     #Set button in place, set dimensions
        buttonCont = Button(self.startScreen, text = "Continue Game",command = lambda: self.loadGame(),font = buttonFont)#create button for load screen
        buttonCont.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .45)                      #set button in place, set dimensions
        buttonExit = Button(self.startScreen, text = "Exit Game", font = buttonFont)                                    #create button for game exit
        buttonExit.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .70)                      #set button in place, set dimensions 
        title = Label(self.startScreen,text = "Camp Epsilon", font = titleFont)                                         #Create label for title
        title.place(bordermode = OUTSIDE, height = 90, width = 300, relx = 0.20, rely = .007)                           #set label in place and set dimensions
        #soundplayer.updateMusic(placeholder)   #play music on screen

    #Method that creates the load screen for the game. 
    def loadGame(self):
        self.startScreen.pack_forget()                      #Take away frame that holds starts screen stuff from window
        self.loadScreen = Frame(self.root)                  #Create new frame that holds stuff for load screen
        self.loadScreen.config(height = 500, width = 500)   #Set dimensions
        self.loadScreen.pack()                              #pack screen into window
        buttonFont = tkFont.Font(size = 24)                 #Set font size
        files = []      #list that will hold butttons for save files
        counter = 0     #used in placing buttons
        ycoord = 100    #y coordinate to place buttons
        #saveFiles = userFile.getFileNames()        #Called to get save files 
        names = ["bill","mandy","edd","dora","jimmy"]#Test list for names. Will delete later
        for name in names:                           #For loop that goes through all file names 
            files.append(Button(self.loadScreen, text = name,font = buttonFont))#Testing. Will delete later.
            #files.append(Button(self.loadScreen, text = name,font = buttonFont,command = lambda: userFile.loadFile(name)))#Creates buttons that will tell userFile_Handler to load file
            files[counter].place(relx = .30, y = ycoord) #Place button in frame
            counter += 1 #update counter
            ycoord += 75 #update y coordinate
        buttonReturn = Button(self.loadScreen, text = "Return to start", command = lambda: self.LoadToStart())#Button to return to start screen
        buttonReturn.place(height = 100, width = 200, x= 150, y = 400)#place button and set dimensions

    #Method to switch load screen to start screen
    def LoadToStart(self):
        self.loadScreen.destroy()   #Destroys loadscreen frame.
        self.startScreen.pack()     #put start screen back into window.

    #Method that creates popup window for file name entry. Changes start screen to game screen
    def startGame(self):
        self.startScreen.pack_forget()          #Take away frame that holds starts screen stuff from window
        buttonFont = tkFont.Font(size = 15)     #create custom font for buttons
        self.entry = Toplevel(self.root,height = 250, width = 300)  #Create new window
        self.entry.title("Enter a name")        #Set title of window. Text thats on top left of window
        self.entry.resizable(height = False, width = False) #Make window not resizable
        instruct = Label(self.entry,text = "Enter name for save file.") #Create text to instruct player to type name
        instruct.place(x = 0,y = 50)    #Place label
        field = Entry(self.entry)       #Create entry box for player
        field.place(x = 150,y = 50)     #place entry in frame
        confirm = Button(self.entry, text = "Ok", command = (lambda:self.start(field.get())), font  = buttonFont) #create button for player
        confirm.place(x = 125,y = 135)  #Set buttons
        buttonReturn = Button(self.entry, text = "Return to Menu", command = (lambda:self.newToStart()), font  = buttonFont)#create button for returning to start screen
        buttonReturn.place(x = 90, y = 185) #place button to popup window
        self.textbox = Frame(self.root) #Create frame that will hold text in the game
        self.textbox.config(height = 500, width = 500)  #Set dimensions for frame
        self.textbox.pack() #pack frame into main window
        self.scroll = Scrollbar(self.textbox)   #create scrollbar 
        self.scroll.pack(side = RIGHT, fill = Y)#pack scrollbar into window
        self.canvas = Canvas(self.textbox, scrollregion = (0,1000,200,1000),height = 400, width = 400, bg = "white",yscrollcommand = self.scroll.set )#create canvas that will hold text. set scrollbar to scroll canvas vertically
        self.canvas.pack(side = LEFT)#pack canvas left side of frame
        
        
    def start(self,name):
        #files = userFile.getFileNames() #get name of save files
        room = True     #flag if theres room for save files
        dupe = False    #flag if theres already save file with current 
        files = ['billy','edd','mandy','matt'] #test list will delete later
        for names in files:     #for loop tht goes through names. 
            if(names == name):  #If variable name =s one them set flag to true
                dupe = True
                break           #break loop
        if(len(files) == 5):    #if length of list with names = 5 then set room flag to false
            room = False
        if(dupe):   #if the name entry is a already exists as save file. case matters.place warning label
            dupeWarning = Label(self.entry,text = "A file with this name already exists",justify = CENTER)
            dupeWarning.place(x = 50,y = 70)
        if(room == False):#if the max limit of files is reached place warning label.
            roomWarning = Label(self.entry,text = "Max number of save files reached. Please return to Start Menu and go to Load Game to delete a file.",wraplength = 205,justify = CENTER)
            roomWarning.place(x = 50,y = 90)
        if( room and dupe == False):#if both flags don't trip errors
            print name #test will delete
            #self.userFile.saveFile(name)   #create save file
            self.entry.destroy()    #destroy window
            self.GUI_HandlerDSC("Hi")   #testing writing on canvas will delete

    #Method to move new game to start screen
    def newToStart(self):
        self.textbox.destroy()  #destroy frame holding text box
        self.entry.destroy()    #destroy window used to get save file name
        self.startScreen.pack() #pack start screen into main window

    #method for when choice buttons are clicked
    def buttonClick(self,lineNumber):
        #dataFile.CurrentLine = lineNumber  #update currentline
        #self.buttonFrame.destroy()         #destroy frame that holds choice buttons
        pass #placeholder will delete

    #method that handles description keyword lines
    #Current bug: Text is not writing to canvas.
    def GUI_HandlerDSC(self,description):
        DSCfont = tkFont.Font(size = 15)    #create custom font
        self.canvas.create_text(10,self.y,fill = "blue",text = description, font = DSCfont)#create text to put onto canvas
        self.canvas.create_text(150,150,fill = "blue",text = "kokoko", font = DSCfont)  #testing will delete
        self.y += 50    #update y coordinate for adding text to canvas.
        self.canvas.create_text(50,50,fill = "blue",text = "20 dogs chase red cars while cats rain from above", font = DSCfont)#testing will delete
        print "hi" #testing will delete
