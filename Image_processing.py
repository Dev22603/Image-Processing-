# Author: Dev Bachani
# University: Nirma University
import tkinter as tk
import tkinter.font as tkFont
from tkinter import image_types
import cv2
import numpy as np
from tkinter import filedialog
import os
from matplotlib import pyplot as plt
from matplotlib import pylab
from PIL import Image


def bw():
    image_path = filedialog.askopenfilename(title="Open an image File", filetypes=(("image files","*.jpeg"), ("image files","*.png"),("image files","*.jpg"),("image files","*.JPG"),("image files","*.JPEG")))
    originalImage = cv2.imread(image_path)
    if type(originalImage) is np.ndarray:
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original image',originalImage)
        cv2.imshow('Grayscale image', grayImage)
        filename, ext = os.path.splitext(image_path)
        new_filename = f"{filename} grayscale{ext}"
        cv2.imwrite(new_filename,grayImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        return False


def gaussian_blur():
    image_path = filedialog.askopenfilename(title="Open an image File", filetypes=(("image files","*.jpeg"), ("image files","*.png"),("image files","*.jpg"),("image files","*.JPG"),("image files","*.JPEG")))

    originalImage = cv2.imread(image_path)
    if type(originalImage) is np.ndarray:
        blur_img = cv2.GaussianBlur(originalImage, (3,3), sigmaX=34, sigmaY=36)
        cv2.imshow('Original image',originalImage)
        cv2.imshow("Image with Gaussian Blur", blur_img)
        filename, ext = os.path.splitext(image_path)
        new_filename = f"{filename} gaussian blur{ext}"
        cv2.imwrite(new_filename,blur_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        return False
def histogram_BGR():
    image_path = filedialog.askopenfilename(title="Open an image File", filetypes=(("image files","*.jpeg"), ("image files","*.png"),("image files","*.jpg"),("image files","*.JPG"),("image files","*.JPEG")))

    originalImage = cv2.imread(image_path)
    if type(originalImage) is np.ndarray:
        cv2.imshow('Original image',originalImage)
        b,g,r=cv2.split(originalImage)
        plt.hist(b.ravel(), 256, [0, 256])
        plt.hist(g.ravel(), 256, [0, 256])
        plt.hist(r.ravel(), 256, [0, 256])

        filename, ext = os.path.splitext(image_path)
        new_filename = f"{filename} histogram BGR{ext}"
        plt.savefig(new_filename)
        hist= pylab.gcf()
        hist.canvas.set_window_title("Histogram BGR")
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        return False


def histogram():
    image_path = filedialog.askopenfilename(title="Open an image File", filetypes=(("image files","*.jpeg"), ("image files","*.png"),("image files","*.jpg"),("image files","*.JPG"),("image files","*.JPEG")))

    originalImage = cv2.imread(image_path,0)
    if type(originalImage) is np.ndarray:
        cv2.imshow('Original image in grayscale',originalImage)
        plt.hist(originalImage.ravel(), 256, [0, 256])
        filename, ext = os.path.splitext(image_path)
        new_filename = f"{filename} histogram{ext}"
        plt.savefig(new_filename)
        hist= pylab.gcf()
        hist.canvas.set_window_title("Histogram")
        plt.show()
        # cv2.imwrite(new_filename,)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        return False




def edge_detection():
    image_path = filedialog.askopenfilename(title="Open an image File", filetypes=(("image files","*.jpeg"), ("image files","*.png"),("image files","*.jpg"),("image files","*.JPG"),("image files","*.JPEG")))

    originalImage = cv2.imread(image_path)
    if type(originalImage) is np.ndarray:
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original image',originalImage)
        canny=cv2.Canny(grayImage,75,75)
        cv2.imshow("Edge Detection",canny )
        filename, ext = os.path.splitext(image_path)
        new_filename = f"{filename} edge detection{ext}"
        cv2.imwrite(new_filename,canny)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        return False

def compress():
    image_path = filedialog.askopenfilename(title="Open an image File", filetypes=(("image files","*.jpeg"), ("image files","*.png"),("image files","*.jpg"),("image files","*.JPG"),("image files","*.JPEG")))

    originalImage =  Image.open(image_path)
    height, breadth = originalImage.size
    factor=0.75
    compressed_image = originalImage.resize((int(height*factor), int(breadth*factor)),Image.Resampling.LANCZOS)
    filename, ext = os.path.splitext(image_path)
    new_filename = f"{filename} compressed{ext}"
    compressed_image.save(new_filename)
    
    originalImage_view = cv2.imread(image_path)
    CompressedImage_view = cv2.imread(new_filename)
    cv2.imshow('Original image',originalImage_view)
    cv2.imshow('Compressed image',CompressedImage_view)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = tk.Tk()


width = 500
height = 500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,(screenwidth - width) // 2, (screenheight - height) // 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

root.config(background="#737373")  # SETS COLOUR OF WINDOW AS GREY

root.title("Image Processing using Python")

BW_photo_button = tk.Button(root, text="Colour to Grayscale", bg="#666666", height=1,width=18 ,font=("Arial", 16),command=bw)
BW_photo_button.place(relx=0.5,rely=0.3,anchor =tk.CENTER)

Gaussian_photo_button = tk.Button(root, text="Apply Gaussian Blur", bg="#666666",height=1,width=18, font=("Arial", 16),command=gaussian_blur)
Gaussian_photo_button.place(relx=0.5,rely=0.4,anchor =tk.CENTER)

HistogramBGR_photo_button = tk.Button(root, text="Show BGR Histogram", bg="#666666", height=1,width=18,font=("Arial", 16),command=histogram_BGR)
HistogramBGR_photo_button.place(relx=0.5,rely=0.5,anchor =tk.CENTER)

Histogram_photo_button = tk.Button(root, text="Show Histogram", bg="#666666", height=1,width=18,font=("Arial", 16),command=histogram)
Histogram_photo_button.place(relx=0.5,rely=0.6,anchor =tk.CENTER)

Canny_photo_button = tk.Button(root, text="Edge Detection", bg="#666666", height=1,width=18,font=("Arial", 16),command=edge_detection)
Canny_photo_button.place(relx=0.5,rely=0.7,anchor =tk.CENTER)

compress_photo_button = tk.Button(root, text="Compress image", bg="#666666",height=1,width=18 ,font=("Arial", 16),command=compress)
compress_photo_button.place(relx=0.5,rely=0.8,anchor =tk.CENTER)

credit=tk.Label(root,text="Image Processing by Dev Bachani", bg="#737373" ,font=("Arial Rounded MT Bold", 15))
credit.place(relx=0.5,rely=0.1,anchor =tk.CENTER)
root.mainloop()
