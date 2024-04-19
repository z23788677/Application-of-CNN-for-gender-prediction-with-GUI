import os
import tkinter as tk
from tkinter import filedialog
import cv2
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model

#load the model
model = load_model('model\gender.h5')

def predict(resized_imgae):
        global pred_gender
        x = np.expand_dims(resized_imgae, axis=0)
        outcome = model.predict(x)
        print(outcome)

        if 0.95 >= outcome[::,0]:
                pred_gender = "這是男生"
        else:
                pred_gender = "這是女生"
        return pred_gender

def resize_image(path):
        global img_pil
        global img_predict
        img = image.load_img(path)
        img_np = image.img_to_array(img)
        img_fordisplay = cv2.resize(img_np, (400, 320))
        img_predict = cv2.resize(img_np, (64, 64))
        img_pil = Image.fromarray(img_fordisplay.astype('uint8'))
        return (img_pil, img_predict)

def display_image():
        global label_img
        image_path = filedialog.askopenfilename()
        resize_image(image_path)
        predict(img_predict)
        label_img = ImageTk.PhotoImage(image=img_pil)
        show_image.config(image=label_img)

        if pred_gender == "這是女生":
                show_gender.config(text = "這是女生(This is female)",fg = "pink")
        if pred_gender == "這是男生":
                show_gender.config(text = "這是男生(This is male)",fg = "deepskyblue")

win = tk.Tk ()
win.iconbitmap("icon.ico")
win.title("Gender predictor by CNN")
win.geometry("600x600+450+100")
win.resizable(0,0)
win.config(bg="#323232")

title_text = tk.Label(text="Select image, Let AI do the rest", fg="white", bg="#323232")
title_text.config(font="微軟正黑體 30")
title_text.pack()

show_image = tk.Label(text = "",fg="white",bg="#323232")
show_image.pack()

select_image = tk.Button(text = "Select the file",fg = "white", bg = "#323232" ,command = display_image)
select_image.config(font="微軟正黑體 16")
select_image.place(x = 220, y=400)

gender = tk.Label (text = "Binary Gender: ", fg="red", bg="#323232")
gender.config(font="微軟正黑體 16")
gender.place(x = 150, y=500)

show_gender = tk.Label (text = "", fg = "blue", bg = "#323232")
show_gender.config(font="微軟正黑體 16")
show_gender.place(x = 300, y=500)

win.mainloop()