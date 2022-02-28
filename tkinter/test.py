import tkinter as tk
from tkinter import *
from tkinter import Label, filedialog as fd
from tkinter.filedialog import askopenfile
from turtle import bgcolor
from PIL import Image, ImageTk


app = tk.Tk() # beginning of interface
app.title("Image Transformer") # setting title of app
app.geometry("350x350+500+200") # window size & positioning from left and top
app.configure(bg="#856ff8", bd=0, highlightthickness=0, relief='ridge')

label = tk.Label(app, text = 'Image\nTransformer', height=8, bg="#856ff8").pack(side="top") # pack is used to show the object in the app

# display function
def display():
    newWindow = tk.Toplevel(app)
    newWindow.title("Result")
    newWindow.geometry("500x400+500+200")
    pane = Frame(newWindow)
    pane.pack(fill = BOTH, expand = True)

    # Create a photoimage object of the image in the path
    image1 = Image.open("/home/rjan/Documents/college_stuffs/applied_programmin_python/tkinter/image.jpeg")
    aspect_ratio = image1.width /image1.height
    image1 = image1.resize((200, int(200 / aspect_ratio)))

    test = ImageTk.PhotoImage(image1)

    # Label(newWindow,text ="This is a new window").pack()
    # Constructing the first frame, frame1
    b1=LabelFrame(pane)
    inp_label = Label(b1, text="Input image")
    inp_label.pack()
    image_label =  Label(b1,image=test)
    image_label.image =test
    image_label.pack()
    b1.pack(side="left", fill=BOTH , expand=TRUE)

    # Constructing the second frame, frame2
    b2=LabelFrame(pane)
    out_label = Label(b2, text="Output image")
    out_label.pack()
    
    output_image_label = Label(b2,image=test)
    output_image_label.image =test
    output_image_label.pack()
    b2.pack(side="right",fill=BOTH , expand=TRUE)


# button function
def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    if filename:
        print(filename)
        uploadBtn_text.set("Image uploaded")
    
        quanBtn_text= tk.StringVar()
        quanBtn= tk.Button(app,textvariable=quanBtn_text,command=lambda:display()
                    ,font="Raleway",bg="black",fg="white",width=15,
                        bd=0, highlightthickness=0, relief='ridge')
        quanBtn_text.set("Image Quantization")
        quanBtn.pack()

        dethBtn_text= tk.StringVar()
        dethBtn= tk.Button(app,textvariable=dethBtn_text,command=lambda:display()
                    ,font="Raleway",bg="black",fg="white",width=15,
                        bd=0, highlightthickness=0, relief='ridge')
        dethBtn_text.set("Image Dethering")
        dethBtn.pack()
        
        sketchBtn_text= tk.StringVar()
        sketchBtn= tk.Button(app,textvariable=sketchBtn_text,command=lambda:display()
                    ,font="Raleway",bg="black",fg="white",width=15,
                        bd=0, highlightthickness=0, relief='ridge')
        sketchBtn_text.set("Image Sketch")
        sketchBtn.pack()
    
#Upload button
# uploadBtn_text= tk.StringVar()
# upBtn= tk.Button(app,textvariable=uploadBtn_text,command=lambda:upload_file()
#                ,font="Raleway",bg="black",fg="white",width=15,
#                 bd=0, highlightthickness=0, relief='ridge')
# uploadBtn_text.set("Upload image")
# upBtn.pack()

display()

app.mainloop() # ending of interface