from tkinter import *
from PIL import Image, ImageTk
import requests

top = Tk()
top.title("Weather App")
top.geometry("600x500")

# 821bf4868da7dc2fb17ce68d29308b08 "Api key"
# Api URL: https://api.openweathermap.org/data/3.0/weather?lat={lat}&lon={lon}&exclude={part}&appid={API key}

path = "E:/self work/project/weather forcasting/tree1.jpg"
img = ImageTk.PhotoImage(Image.open(path))
bg_image = Label(top, image=img)
bg_image.place(x=0, y=0, width=600, height=500)


def response_L2(weather_detailas):
    try:
        City = weather_detailas['name']
        Condition = weather_detailas['weather'][0]['description']
        Temperature = weather_detailas['main']['temp']
        Temp=(Temperature-32)*5/9
        Humidity = weather_detailas['main']['humidity']

        results = 'City:%s\nCondition:%s\nTemperature:%s F\nTemp:%d C\nHumidity:%s' % (City, Condition,Temperature,Temp,Humidity)

    except:
        results = 'There are some error try again '

    return results


def get_data(city):
    api_key = "821bf4868da7dc2fb17ce68d29308b08"
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {'APPID': api_key, 'q': city, 'units': 'imperial'}
    reponse = requests.get(api_url, parameters)
    weather_details = reponse.json()

    print(weather_details)
    print("City :",weather_details['name'])
    print("Description :",weather_details['weather'][0]['description'])
    print("Temp :",weather_details['main']['temp'])
    print("Humidity :",weather_details['main']['humidity'])


    L2['text'] =response_L2(weather_details)

    logo=weather_details['weather'][0]['icon']
    open_logo(logo)
def open_logo(icon):
    size=int(F2.winfo_height()*0.25)
    path2="./img/"+icon+".png"
    img1=ImageTk.PhotoImage(Image.open(path2).resize((size,size)))
    weather_logo.delete("all")
    weather_logo.create_image(0,0,anchor="nw",image=img1)
    weather_logo.image=img1


L1 = Label(bg_image, text="Enter city name to get weather details", font="Arial 15 bold", bd=5, bg="sky blue",
           fg="black")
L1.place(x=100, y=10)

F1 = Frame(bg_image, bg="sky blue", bd=5)
F1.place(x=100, y=50, width=400, height=50)
E1 = Entry(F1, bd=5, font="Arial 12 bold", width=28)
E1.grid(row=0, column=0, sticky="w")
B1 = Button(F1, text="Get Weather", bd=5, font="Arial 12 bold", command=lambda: get_data(E1.get()))
B1.grid(row=0, column=1, padx=10, sticky="e")

F2 = Frame(bg_image, bg="sky blue", bd=5)
F2.place(x=100, y=150, width=400, height=250)
L2 = Label(F2, bd=5, font="Arial 12 bold",justify=LEFT,anchor="nw")
L2.place(relwidth=1, relheight=1)

weather_logo=Canvas(L2,bg="white",bd=0,highlightthickness=0)
weather_logo.place(x=300,y=5)

top.mainloop()
