from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from tkinter import *
from PIL import Image, ImageTk
import tkinter
import requests
import subprocess
import time
from bs4 import BeautifulSoup

def Scraping():
  usuario = user.get()
  contrasenia = password.get()
  raiz.destroy()
  driver = webdriver.Chrome()
  while True:
    driver.get("https://sum.unmsm.edu.pe/loginWebSum/login.htm")
    mBox = driver.find_element("xpath", '/html/body/div/div[2]/form/div[1]/input')
    mBox.send_keys(usuario)
    mBox = driver.find_element("xpath", '/html/body/div/div[2]/form/div[2]/input')
    mBox.send_keys(contrasenia)
    driver.find_element("xpath",'/html/body/div/div[2]/form/div[3]/button').click()
    driver.find_element("xpath", '/html/body/div/div/div/div/div/div/form/div/button').click()
    driver.find_element("xpath",'/html/body/div/div/div[1]/section/div/div[2]/ul/li[3]/a').click()
    driver.find_element("xpath",'/html/body/div/div/div[1]/section/div/div[2]/ul/li[3]/ul/li[1]/a').click()
    try:
      element = driver.find_element("xpath",'/html/body/div/div/div[1]/section/div/div[1]/div/span[1]')
      var = 1
    except NoSuchElementException:
      var = 0
    if var == 1:
      window=Tk()
      window.title("RESULTADO")
      window.resizable(0,0)
      window.iconbitmap("C:\\Users\\LENOVO\\Desktop\\NesoSoftware\\unmsm.ico")
      window.geometry("235x150")
      window.config(bg="#202020")
      fun=tkinter.Label(window, text="Se inició sesión correctamente",bg="#00FF19",fg="black")
      fun.pack()
      fun.place(x=35,y=10)
      image = Image.open("C:\\Users\\LENOVO\\Desktop\\NesoSoftware\\chika.png")
      image = image.resize((90, 80))
      image = ImageTk.PhotoImage(image)
      label = tkinter.Label(window, image=image,borderwidth=0)
      label.pack()
      label.place(x=65,y=50)
      window.mainloop()
    else: text="No se pudo iniciar sesion"



raiz=Tk()
raiz.title("Log In")
raiz.resizable(0,0)
raiz.iconbitmap("C:\\Users\\LENOVO\\Desktop\\NesoSoftware\\unmsm.ico")
raiz.geometry("235x250")
raiz.config(bg="#202020")

fun=tkinter.Label(raiz, text="        INGRESE SUS DATOS        ",bg="black",fg="white",font=("Rajdhani", 12))
fun.pack()
fun.place(x=0,y=20)

img_user = Image.open("C:\\Users\\LENOVO\\Desktop\\NesoSoftware\\user.png")
img_user = img_user.resize((25,25))
img_user = ImageTk.PhotoImage(img_user)
label = tkinter.Label(raiz, image=img_user,borderwidth=0)
label.pack()
label.place(x=10,y=58)

user=Entry(raiz,bg="#535353",fg="white",width=15)
user.pack()
user.place(x=41,y=60)

correo=tkinter.Label(raiz,text="@unmsm.edu.pe",bg="black",fg="white",font=("Arial",8))
correo.pack()
correo.place(x=137,y=60)

img_password = Image.open("C:\\Users\\LENOVO\\Desktop\\NesoSoftware\\password.png")
img_password = img_password.resize((25,25))
img_password = ImageTk.PhotoImage(img_password)
label = tkinter.Label(raiz, image=img_password,borderwidth=0)
label.pack()
label.place(x=10,y=93)

password=Entry(raiz,show="*",bg="#535353",fg="white",width=30)
password.pack()
password.place(x=41,y=95)


img_cat = Image.open("C:\\Users\\LENOVO\\Desktop\\NesoSoftware\\gato.png")
img_cat = img_cat.resize((90, 80))
img_cat = ImageTk.PhotoImage(img_cat)
label = tkinter.Label(raiz, image=img_cat,borderwidth=0)
label.pack()
label.place(x=70,y=160)

button_send=Button(raiz,text="Enviar",bg="#202020",fg="white",command=Scraping)
button_send.pack()
button_send.place(x=95,y=130)

Copyright=tkinter.Label(raiz, text="© Created for NesoDev",bg="#202020",fg="gray",font=("Rajdhani", 7))
Copyright.pack()
Copyright.place(x=63,y=230)

raiz.mainloop()