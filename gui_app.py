# gui_app.py

import tkinter as tk
from tkinter import *
import PIL.ImageGrab as ImageGrab
import numpy as np
from tensorflow.keras.models import load_model
import cv2

model = load_model("model.h5")

def predict_digit(img):
    img = img.resize((28, 28)).convert('L')  
    img = np.array(img)
    img = 255 - img  
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    prediction = model.predict(img)
    return np.argmax(prediction), max(prediction[0])

def clear_canvas():
    canvas.delete("all")

def draw(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    canvas.create_oval(x1, y1, x2, y2, fill='black', width=20)

def classify_handwriting():
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    img = ImageGrab.grab().crop((x, y, x1, y1))
    digit, acc = predict_digit(img)
    label_result.config(text=f"Prediction: {digit}\nAccuracy: {int(acc * 100)}%")

root = Tk()
root.title("Digit Recognizer")
canvas = Canvas(root, width=200, height=200, bg='white')
canvas.pack()
canvas.bind("<B1-Motion>", draw)

btn_predict = Button(root, text="Predict", command=classify_handwriting)
btn_predict.pack()
btn_clear = Button(root, text="Clear", command=clear_canvas)
btn_clear.pack()
label_result = Label(root, text="", font=("Helvetica", 16))
label_result.pack()

root.mainloop()
