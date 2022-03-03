from tkinter import *
from webbrowser import get
from PIL import Image,ImageTk
import requests

root = Tk()
root.title("TINT's Weather App Using Python Tkinter GUI")
root.geometry("600x500")

def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = "City:%s\nCondition:%s\nTemperature:%s"%(city,condition,temp)
    except:
        final_str="There was a problem retrieving that information"
    
    return final_str

def get_weather(city):
    weather_key = "82fc4137f7a113eac291dc3eb1c9e72c"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}"
    response = requests.get(url)
    weather = response.json()

    # print(weather)

    result['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)
    
def open_image(icon):
    size = int(frame_two.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open("./Weather_icons/img/"+icon+".png").resize((size,size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0,anchor="nw",image=img)
    weather_icon.image=img

img = Image.open("./img.jpg")
img = img.resize((600,500),Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = Label(root, image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title = Label(root,text="Earth including over 200,000 cities",fg="red",bg="#b7cddd",font=("times new roman",16,"bold"))
heading_title.place(x=80,y=18)

frame_one = LabelFrame(root,bg="#42c2f4",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box = Entry(frame_one,font=("times new roman",25),width=17)
txt_box.grid(row=0,column=0,sticky='w')

btn=Button(frame_one,text="Get Weather",fg="black",font=("times new roman",16,"bold"),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

frame_two = LabelFrame(root,bg="#42c2f4",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result = Label(frame_two,bg="white",justify="left",anchor="nw")
result.place(relwidth=1,relheight=1)

weather_icon = Canvas(result,bg="white",bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)

root.mainloop()