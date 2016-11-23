#Version 0.0.8
from Tkinter import *
import tkFont
from soundHandler import soundHandler

class GUI_Manager:
    soundPlayer = soundHandler()    #object for soundHandler. used to play music and sound effects
    y = 50                          #y coordinate to place text on canvas
    lineNumber = 0                  #Line number for choice
    
    def __init__(self,master = None):
        self.startScreen = Frame(master)                    #Create a frame to hold stuff for startScreen
        master.minsize(width = 1000,height = 500)           #Set minimum size to main window
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
        #soundplayer.updateMusic(placeholder)               #play music on screen

    #Method that creates the load screen for the game. 
    def loadGame(self,names):
        self.startScreen.pack_forget()                      #Take away frame that holds starts screen stuff from window
        self.loadScreen = Frame(self.root,bg = "black")     #Create new frame that holds stuff for load screen
        self.loadScreen.config(height = 500, width = 500)   #Set dimensions
        self.loadScreen.pack(expand = True,fill = BOTH)     #pack screen into window
        titleFont = tkFont.Font(size = 30)                  #Set font for titles
        buttonFont = tkFont.Font(size = 18)                 #Set font size
        title = Label(self.loadScreen,text = "Save File Menu",font = titleFont,fg = "red") #Create label for load screen table
        title.place(height = 90,width = 300, relx = .35, rely = .007)
        files = []                                          #list that will hold butttons for save files
        counter = 0                                         #used in placing buttons
        ycoord = 100                                        #y coordinate to place buttons
        self.filename =""                                   #Create var to hold save file
        for name in names:                                  #For loop that goes through all file names 
            files.append(Button(self.loadScreen, text = name,font = buttonFont,command = lambda:(self.setfile(name))))#Creates button with save file name
            files[counter].place(x = 450, y = ycoord)    #Place button in frame
            counter += 1 #update counter
            ycoord += 60 #update y coordinate
        if(len(files) == 0):
            warning = Label(self.loadScreen,text = "No Saves Availiable",font = titleFont,fg = "red")#Create label for when saves are found
            warning.place(height = 90,width  = 500,relx = .25, rely = .30)
        buttonReturn = Button(self.loadScreen, text = "Return to start", command = lambda: self.LoadToStart(),font = buttonFont)#Button to return to start screen
        buttonReturn.place(height = 100, width = 200, x= 400, y = 400)#place button and set dimensions

    #Method used to get file name from to pass to user file
    def setfile(self,name):
        self.filename = name    #Set name to variable

    #Method that creates popup window for file name entry. Changes start screen to game screen
    def startGame(self):
        self.startScreen.pack_forget()                                  #Take away frame that holds starts screen stuff from window
        buttonFont = tkFont.Font(size = 15)                             #create custom font for buttons
        self.entry = Toplevel(self.root,height = 250, width = 300)      #Create new window
        self.entry.title("Enter a name")                                #Set title of window. Text thats on top left of window
        self.entry.resizable(height = False, width = False)             #Make window not resizable
        instruct = Label(self.entry,text = "Enter name for save file.") #Create text to instruct player to type name
        instruct.place(x = 0,y = 50)                                    #Place label
        field = Entry(self.entry)                                       #Create entry box for player
        field.place(x = 150,y = 50)                                     #place entry in frame
        confirm = Button(self.entry, text = "Ok", command = (lambda:self.start(field.get())), font  = buttonFont) #create button for player
        confirm.place(x = 125,y = 135)                                  #Set buttons
        buttonReturn = Button(self.entry, text = "Return to Menu", command = (lambda:self.GameToStart(0)), font  = buttonFont)#create button for returning to start screen
        buttonReturn.place(x = 90, y = 185)                             #place button to popup window
        self.gameScreen = Frame(self.root,bg = "black")                 #Create a frame to hold textbox, choice buttons?, and background?
        self.gameScreen.pack(fill = BOTH,expand = True)                 #Pack frame to window
        self.textbox = Frame(self.gameScreen)                           #Create frame that will hold text in the game
        self.textbox.config(height = 500, width = 500)                  #Set dimensions for frame
        self.textbox.pack()                                             #pack frame into gameScreen
        self.scroll = Scrollbar(self.textbox)                           #create scrollbar 
        self.scroll.pack(side = RIGHT, fill = Y)                        #pack scrollbar into window
        self.canvas = Canvas(self.textbox, scrollregion = (0,0,0,1000),height = 400, width = 400, bg = "white",yscrollcommand = self.scroll.set )#create canvas that will hold text. set scrollbar to scroll canvas vertically
        self.canvas.pack(side = LEFT)                                   #pack canvas left side of frame
        self.scroll.config( command = self.canvas.yview)                #set the scrollbar change the canvas
        logo = PhotoImage(file = 'python_logo.gif')
        option = Button(self.gameScreen, text = "Options", command = (lambda:self.optionMenu()), font  = buttonFont,width = 10, height = 5) #create button for options
        #option.config(image = logo, compound = LEFT)
        option.pack()                                                   #pack button into frame
        self.GUI_HandlerBKG("")                                         #Used to 
        a = "I'll come running like Indiana Jones to rescue you!"#Test stuff will delete
        b ="You'll have to find a way to get out of there "#Test stuff will delete
        #self.GUI_HandlerCHC(0,a,0,b)#Test stuff will delete
        
    def start(self,name):
        #self.userFile.saveFile(name)   #create save file
        self.entry.destroy()    #destroy window

    #method for when choice buttons are clicked
    def buttonClick(self,number):
        self.buttonFrame.destroy()         #destroy frame that holds choice buttons
        self.lineNumber = number

    def optionMenu(self):
        buttonFont = tkFont.Font(family = "times",size = 15)
        self.options = Toplevel(self.root,height = 250, width = 300)
        self.options.title("Option Menu")
        toggleMUS = Button(self.options, text = "Music On/Off", command = (lambda:self.soundPlayer.toggleMusic()), font  = buttonFont)
        toggleMUS.pack()
        toggleSE = Button(self.options, text = "Sound Effects On/Off", command = (lambda:self.soundPlayer.toggleSFX()), font  = buttonFont)
        toggleSE.pack()
        closeOptions = Button(self.options, text = "Return to Game", command = (lambda:self.options.destroy()), font  = buttonFont)
        closeOptions.pack()
        startMenu = Button(self.options, text = "Return to Menu", command = (lambda:self.GameToStart(1)), font  = buttonFont)
        startMenu.pack()

    #Method to switch load screen to start screen
    def LoadToStart(self):
        self.loadScreen.destroy()   #Destroys loadscreen frame.
        self.startScreen.pack()     #put start screen back into window.

    #Method to move new game to start screen
    def GameToStart(self,window):
        if (window == 0):
            self.entry.destroy()    #destroy window used to get save file name
        else:
            self.options.destroy()  #destroy game option menu
        self.gameScreen.destroy()  #destroy frame holding text box
        self.startScreen.pack() #pack start screen into main window
    

    #method that handles description keyword lines
    #Current bug: Text maybe shown incorrect. Examples: Text maybe overlapped with other text(Max line limit is 2 in size 15 font).
    #Current format for create_text(X coordinate(I think the coordinate is middle of text),Ycoordinate, font color, font, max width of text in pixels,text is centered so that left side is (x,y))
    def GUI_HandlerDSC(self,description):
        DSCfont = tkFont.Font(size = 15)    #create custom font
        self.canvas.create_text(0,self.y,fill = "blue",text = description, font = DSCfont,width = 400,anchor = W)#create text to put onto canvas
        self.y += 50    #update y coordinate for adding text to canvas.

    #method handles npc keyword lines
    #Has same bugs as description does. Create_text format is same too.
    def GUI_HandlerNPC(self,dialouge):
        NPCfont = tkFont.Font(size = 15)
        self.canvas.create_text(0,self.y,fill = "green", text = dialouge, font = NPCfont,width = 400,anchor = W)
        self.y += 50

    #method handles choice keywords lines
    def GUI_HandlerCHC(self,lineA,stringA,lineB,stringB):
        CHCfont = tkFont.Font(size = 13)            #Create custom font for choices
        self.buttonFrame = Frame(self.gameScreen)   #Create frame for buttons
        self.buttonFrame.pack(side = BOTTOM)        #place frame on bottom of gamescreen
        buttonA = Button(self.buttonFrame,text = stringA, font = CHCfont,wraplength = 200,command = (lambda: self.buttonClick(lineA)),height = 3,width = 25)
        buttonB = Button(self.buttonFrame,text = stringB, font = CHCfont,wraplength = 200,command = (lambda: self.buttonClick(lineB)),height = 3,width = 25)

        buttonA.grid(row = 0, column = 0)        #Place buttons 
        buttonB.grid(row = 0, column = 1)

    #method for backgrounds
    #Maybe do background frames for left and right of textbox
    #Would require the use of two files for each frame tho.
    def GUI_HandlerBKG(self,background):
        self.back = Frame(self.gameScreen)
        self.back.place(x=0,y=0)
        self.test = Canvas(self.back,height = 500, width = 284,bg = "red",bd=0)
        self.test.pack()
        self.backR = Frame(self.gameScreen)
        self.backR.place(x=710,y=0)
        self.testR = Canvas(self.backR,height = 500, width = 285,bg = "red",bd=0)
        self.testR.pack()

    #Method for music keyword lines
    def GUI_HandlerMUS(self,music):
        soundPlayer.updateMusic(music) #Tells soundPlayer to play music

    #Method for sound effect keywords
    def GUI_HandlerSFX(self,sound):
        soundPlayer.playSound(sound)    #Tells soundPlayer to play the sound effect
