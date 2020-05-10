import tkinter as tk
import requests


root = tk.Tk()

# api_key=b3a8e91a78f6e97f13b3dc9872a7f134
#api_call=api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

def format_response(weather):
	name='city: ' + weather['name']
	temp='temp: '+ str(weather['main']['temp'])
	return name + '\n' + temp
    


def get_weather(city):
	
	weather_key='b3a8e91a78f6e97f13b3dc9872a7f134'
	url='https://api.openweathermap.org/data/2.5/weather?q='
	newurl=url + city + '&appid=' + weather_key
	response=requests.get(newurl).json()
	weather=response
	print('city: ' + weather['name'])
	print('temp: '+ str(weather['main']['temp']))
	label['text']=format_response(weather)




canvas = tk.Canvas(root, height = 700, width= 800)
canvas.pack()

bgimage=tk.PhotoImage(file='37126_balloon-png.png')
bglabel=tk.Label(root,image=bgimage)
bglabel.place(relheight=1,relwidth=1)

top_frame=tk.Frame(root, bg = 'grey')
top_frame.place(relx=0.25,rely=0.1,relwidth=0.50,relheight=0.05)

enter_city=tk.Entry(top_frame)
enter_city.place(relx=0.01,rely=0.1,relwidth=0.70,relheight=0.8)

weathersearch=tk.Button(top_frame, text='Get weather', bg='grey',command=lambda: get_weather(enter_city.get()))
weathersearch.pack(side='right')


middle_frame=tk.Frame(root, bg='grey')
middle_frame.place(relx=0.25,rely=0.2,relheight=0.5,relwidth=0.50)

label=tk.Label(middle_frame, anchor='nw', justify='left')
label.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)



#label=tk.Label(frame, text='Type in the box below', bg='white')
#label.pack()

#entry=tk.Entry(frame, bg='white')
#entry.pack(expand=True, fill='both')

#button = tk.Button(root,text="Test button", bg='red')
#button.place(relx=0,rely=0)
root.mainloop()