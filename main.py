from time import *
from tkinter import *

from pygame import mixer

user_time = None


def hour(user_t):
    if user_t > 60:
        h_time = int(user_t / 60)
        user_t = user_t % 60
    else:
        h_time = 0
    return h_time, user_t


def timer(h_time, user_time, sec_time):
    while h_time >= 0:
        while user_time >= 0 :
            while sec_time:
                time_counter = "{:02d}:{:02d}:{:02d}".format(h_time, user_time, sec_time)
                time_label.config(text=time_counter)
                sec_time -= 1
                window.update()
                sleep(1)
            else:
                time_counter = "{:02d}:{:02d}:{:02d}".format(h_time, user_time, sec_time)
                time_label.config(text=time_counter)
                window.update()
                sleep(1)
            user_time -= 1
            sec_time = 59
        h_time -= 1
        user_time = 59
    else:
        mixer.init()
        a = mixer.Sound("alarma.mp3")
        a.play()
        sleep(3)
        a.stop()


def main() :
    global user_time
    # user_time = int(input("Enter your time (in minutes):"))
    h_time, user_time = hour(user_time)
    sec_time = 0
    timer(h_time, user_time, sec_time)


def start_func() :
    global user_time
    user_time = int(text_area.get())
    main()


window = Tk()
window.geometry("600x400")

text_area = StringVar()

time_label = Label(window, font=("Ink Free", 50), text="00:00:00", fg="red", bg="black", padx=10, pady=10, border=0)
time_label.pack()

input_var = Entry(window, textvariable=text_area, width=10, font=("Ink Free", 35))
input_var.pack()

frame = Frame(window)
frame.pack()

play_btn = Button(frame, text="Play", command=start_func, font=("Ink Free", 25), border=0, bg="#c7c7c7")
play_btn.pack()
stop_btn = Button(frame, text="Restart", command=main, font=("Ink Free", 25), border=0, bg="#c7c7c7")
stop_btn.pack()

window.mainloop()
