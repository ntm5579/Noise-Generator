from tkinter import *
from tkinter.filedialog import askopenfilename
from Functions import *

def GUI_Init():
    menuList = []

    def loadAndUnload(menuToLoad):
        for menu in menuList:
            if menu != menuToLoad:
                menu.grid_forget()
        menuToLoad.grid(column = 0, row= 0)

    window = Tk()
    window.geometry('800x600')
    window.title("Gui Test")
    window.resizable(False, False) 

    universalFrame = Frame(window, width= 30, height = 2, bg= 'aqua')
    universalFrame.grid(column= 1, row = 0, sticky= "NE")

    #loads the last window and then takes that item off of the list of pages, watch the minus two indexing issus
    backButton = Button(universalFrame, text= "Back", width = 15, height = 2, command=lambda: loadAndUnload(previousWindow[-2]))
    backButton.grid(column=0, row= 0, padx= 5, pady = 5)

    homeButton = Button(universalFrame, text= "Home", width = 10, height = 2, command=lambda: loadAndUnload(mainMenu))
    homeButton.grid(column=1, row= 0, padx= 5, pady = 5)

    mainMenu = Frame(window)
    mainMenu.grid(column = 0, row= 0, padx= 15)
    menuList.append(mainMenu)

    previousWindow = [mainMenu]

    menuLabel = Label(mainMenu, text="Menu", width= 65, height= 2, bg = "Coral")
    menuLabel.grid(column= 0, row= 0, padx= 10, columnspan=2)

    uploadButton = Button(mainMenu, text= "Upload your own image", width = 20, height = 4, command= lambda:loadAndUnload(uploadMenu))
    uploadButton.grid(column = 0, row= 1, padx= 5, pady = 10)

    uploadMenu = Frame(window)
    menuList.append(uploadMenu)

    uploadLabel = Label(uploadMenu, text = "Uploading and shit", width= 65, height=2, bg = "Coral")
    uploadLabel.grid(column = 0, row= 0, padx= 10, columnspan=2)

    filename = ''
    def imageUpload():
        global filename
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)
        #might have to global this shit
        #make this a preview of upload
        uploadedImageDisplay = ''

    #set up command to get a file path to work with, have this function enable the blurbutton and scramble button
    uploadImageButton = Button(uploadMenu, text= "Click hear to upload \n an Image", width = 20, height = 4, command=imageUpload)
    uploadImageButton.grid(column= 0, row = 1, columnspan=2, padx= 5, pady = 5)

    #hook this up to the blur func and pass argument of file path, enable when you get a file path
    blurButton = Button(uploadMenu, text= "Click hear to upload \n an Image", state="disabled", width = 20, height = 4)
    blurButton.grid(column= 0, row = 2, padx= 5, pady = 5)

    scrambleButton = Button(uploadMenu, text= "Click hear to upload \n an Image", state="disabled", width = 20, height = 4)
    scrambleButton.grid(column= 1, row = 2, padx= 5, pady = 5)
    

    createMenu = Frame(window)
    menuList.append(createMenu)

    createButton = Button(mainMenu, text="Create a new image", width = 20, height = 4, command=lambda: loadAndUnload(createMenu))
    createButton.grid(column = 1, row= 1, padx= 5)

    createLabel = Label(createMenu, text = "Creating and shit", width= 65, height= 2, bg = "coral")
    createLabel.grid(column = 0, row= 0, padx= 5)

    noiseButton = Button(createMenu, text= "Make Some Noise", width = 60, height = 4)
    noiseButton.grid(column= 0, row = 2, padx= 5, pady = 5)

    window.mainloop()

#prevents this Gui_Init from getting called on import of loadBar()
if __name__ == "__main__":
    GUI_Init()