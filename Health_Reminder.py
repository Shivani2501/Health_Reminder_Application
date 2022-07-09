import tkinter as tk
import time
import requests
import bs4
import plyer
import webbrowser


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, CovidUpdatesPage, SympAndPrevCovidPage,
                  SympAndPrevCommonPage, BMIPage, NotificationSettPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Health Reminder')
        self.controller.state('zoomed')
        self.controller.iconphoto(False, tk.PhotoImage(file='health-report.png'))

        heading_label = tk.Label(self,
                                 text='HEALTH REMINDER',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c',
                                 )
        heading_label.pack(pady=150)

        def menu_p():
            controller.show_frame('MenuPage')

        next_button = tk.Button(self,
                                command=menu_p,
                                text='Next',
                                font='bold',
                                relief='raised',
                                borderwidth=3,
                                width=20,
                                height=2)
        next_button.pack(pady=100, ipady=4)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label1_1 = tk.Label(self,
                                    text=' Sections ',
                                    font=('orbitron', 45, 'bold'),
                                    foreground='#ffffff',
                                    background='#3d3d5c',
                                    relief='raised',
                                    borderwidth=3,
                                    )
        heading_label1_1.pack(pady=10, anchor='w')

        def home_page_func():
            controller.show_frame('StartPage')

        home_button1 = tk.Button(self,
                                 text='Home',
                                 command=home_page_func,
                                 relief='raised',
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        home_button1.pack(pady=3, anchor='w')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        def covid_updates_func():
            controller.show_frame('CovidUpdatesPage')

        heading_label1_2 = tk.Label(button_frame,
                                    text='Covid-19 Updates',
                                    font=('orbitron', 30,),
                                    foreground='#ffffff',
                                    background='#33334d',
                                    )
        heading_label1_2.grid(row=0, column=0, pady=5, padx=30)

        go_button1 = tk.Button(button_frame,
                               text='Go',
                               command=covid_updates_func,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        go_button1.grid(row=1, column=0, pady=5)

        def symp_and_prev_covid_func():
            controller.show_frame('SympAndPrevCovidPage')

        heading_label1_3 = tk.Label(button_frame,
                                    text='Symp & prev of Covid 19',
                                    font=('orbitron', 30,),
                                    foreground='#ffffff',
                                    background='#33334d',
                                    )
        heading_label1_3.grid(row=2, column=0, pady=40, padx=30)

        go_button1 = tk.Button(button_frame,
                               text='Go',
                               command=symp_and_prev_covid_func,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        go_button1.grid(row=3, column=0, pady=5)

        def symp_and_prev_common_func():
            controller.show_frame('SympAndPrevCommonPage')

        heading_label1_4 = tk.Label(button_frame,
                                    text='Symp & prev of Common Diseases',
                                    font=('orbitron', 30,),
                                    foreground='#ffffff',
                                    background='#33334d',
                                    )
        heading_label1_4.grid(row=4, column=0, pady=40, padx=30)

        go_button1 = tk.Button(button_frame,
                               text='Go',
                               command=symp_and_prev_common_func,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        go_button1.grid(row=5, column=0, pady=5)

        def bmi_func():
            controller.show_frame('BMIPage')

        heading_label1_5 = tk.Label(button_frame,
                                    text='Body Mass Index',
                                    font=('orbitron', 30,),
                                    foreground='#ffffff',
                                    background='#33334d',
                                    )
        heading_label1_5.grid(row=0, column=1, pady=15, padx=150)

        go_button1 = tk.Button(button_frame,
                               text='Go',
                               command=bmi_func,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        go_button1.grid(row=1, column=1, pady=5, padx=150)

        def notification_sett_func():
            controller.show_frame('NotificationSettPage')

        heading_label1_6 = tk.Label(button_frame,
                                    text='Notification Settings',
                                    font=('orbitron', 30,),
                                    foreground='#ffffff',
                                    background='#33334d',
                                    )
        heading_label1_6.grid(row=2, column=1, pady=5, padx=150)

        go_button1 = tk.Button(button_frame,
                               text='Go',
                               command=notification_sett_func,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        go_button1.grid(row=3, column=1, pady=5, padx=150)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


class CovidUpdatesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label2_1 = tk.Label(self,
                                    text=' Covid 19 Updates ',
                                    font=('orbitron', 40, 'bold'),
                                    foreground='#ffffff',
                                    background='#3d3d5c',
                                    relief='raised',
                                    borderwidth=3,
                                    )
        heading_label2_1.pack(pady=7, anchor='w')

        def menu_page_func():
            controller.show_frame('MenuPage')

        menu_button1 = tk.Button(self,
                                 text='Menu',
                                 command=menu_page_func,
                                 relief='raised',
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        menu_button1.pack(pady=10, anchor='w')

        def get_html_data(url):
            data = requests.get(url)
            return data

        def get_corona_detail_of_india():
            url = "https://www.mohfw.gov.in/"
            html_data = get_html_data(url)
            bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
            all_details = " "
            info_div = bs.find("div", class_='col-xs-8 site-stats-count').find("li", class_="bg-blue").find_next(
                "strong",
                class_="mob-hide").get_text()
            count = bs.find("div", class_='col-xs-8 site-stats-count').find("li", class_="bg-blue").find_next("span",
                                                                                                              class_="active_per").find_next(
                "strong", class_="mob-hide").get_text()
            all_details = all_details + info_div + "         : " + count + "\n"

            info = bs.find("div", class_='col-xs-8 site-stats-count').find("li", class_="bg-green").find_next("strong",
                                                                                                              class_="mob-hide").get_text()
            coun = bs.find("div", class_='col-xs-8 site-stats-count').find("li", class_="bg-green").find_next("span",
                                                                                                              class_="discharged_per").find_next(
                "strong", class_="mob-hide").get_text()
            all_details = all_details + info + "      : " + coun + "\n"

            info_d = bs.find("div", class_='col-xs-8 site-stats-count').find("li", class_="bg-red").find_next("strong",
                                                                                                              class_="mob-hide").get_text()
            cou = bs.find("div", class_='col-xs-8 site-stats-count').find("li", class_="bg-red").find_next("span",
                                                                                                           class_="death_per").find_next(
                "strong", class_="mob-hide").get_text()
            all_details = all_details + info_d + "          : " + cou + "\n"

            total = bs.find("div", class_="col-xs-8 site-stats-count sitetotal").find("div",
                                                                                      class_="fullbol").find_next(
                "span", class_="totalvac").get_text()
            toa = bs.find("div", class_="col-xs-8 site-stats-count sitetotal").find("div", class_="fullbol").find_next(
                "span", class_="coviddata").get_text()
            all_details = all_details + total + " " + toa + "\n"
            return all_details

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        space_label1 = tk.Label(button_frame, height=9, bg='#33334d')
        space_label1.pack()

        updates_label = tk.Label(button_frame,
                                 text=get_corona_detail_of_india(),
                                 font=('orbitron', 25),
                                 bg='#33334d',
                                 fg='white')
        updates_label.pack()

        def refresh():
            new_data = get_corona_detail_of_india()
            updates_label['text'] = new_data

        refresh_button = tk.Button(button_frame,
                                   text='Refresh',
                                   command=refresh(),
                                   relief='raised',
                                   borderwidth=3,
                                   width=40,
                                   height=3)
        refresh_button.pack(pady=20)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


class SympAndPrevCovidPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label3_1 = tk.Label(self,
                                    text=' Symptoms & Prevention of Covid 19 ',
                                    font=('orbitron', 40, 'bold'),
                                    foreground='#ffffff',
                                    background='#3d3d5c',
                                    relief='raised',
                                    borderwidth=3,
                                    )
        heading_label3_1.pack(pady=10, anchor='w')

        def menu_page_func():
            controller.show_frame('MenuPage')

        menu_button2 = tk.Button(self,
                                 text='Menu',
                                 command=menu_page_func,
                                 relief='raised',
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        menu_button2.pack(pady=10, anchor='w')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        space_label1 = tk.Label(button_frame, height=4, bg='#33334d')
        space_label1.pack()

        covid_label = tk.Label(button_frame, height=10, fg="white", font=("orbitron", 17), bg='#33334d',
                               text="Coronavirus (COVID-19) is the name of a dreaded diseases"
                                    " that spread from the city of Wuhan in China.\n"
                                    " But now this Coronavirus infection has spread rapidly throughout the world.\n"
                                    "The coronavirus is threat to the Human Life.\n"
                                    "This Virus is very subtle but effective virus.\n"
                                    "This virus is 900 times smaller than a human's hair"
                                    " and such a virus is so dangerous to human life.\n\n\n"
                                    "Click the button below to know about it's"
                                    " symptoms and preventions as well as some of it's treatments,\n"
                                    "to tackle this virus in an efficient way. ")
        covid_label.pack()

        def open1():
            webbrowser.open("covid-19.html")

        html_button1 = tk.Button(button_frame,
                                 text='Go',
                                 command=open1,
                                 relief='raised',
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        html_button1.pack(padx=400, pady=40)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


class SympAndPrevCommonPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label4_1 = tk.Label(self,
                                    text=' Symptoms and Prevention of Common Diseases ',
                                    font=('orbitron', 40, 'bold'),
                                    foreground='#ffffff',
                                    background='#3d3d5c',
                                    relief='raised',
                                    borderwidth=3,
                                    )
        heading_label4_1.pack(pady=10, anchor='w')

        def menu_page_func():
            controller.show_frame('MenuPage')

        menu_button3 = tk.Button(self,
                                 text='Menu',
                                 command=menu_page_func,
                                 relief='raised',
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        menu_button3.pack(pady=10, anchor='w')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        space_label1 = tk.Label(button_frame, height=4, bg='#33334d')
        space_label1.pack()

        common_diseases_label = tk.Label(button_frame,
                                         height=8,
                                         fg="white",
                                         font=("orbitron", 17),
                                         bg='#33334d',
                                         text="It is not surprising that the top causes of death "
                                              "might vary from place to place.\n"
                                              "But, the measures we should take to improve our health "
                                              "may be the same everywhere.\n"
                                              "It is particularly important to recognize those disease"
                                              "that we know can be prevented,\n"
                                              "can be minimized or even reversed with preventive care.\n\n\n"
                                              "So, to know about symptoms and preventions of some common diseases, "
                                              "Click the button below ")
        common_diseases_label.pack()

        def open2():
            webbrowser.open("common_diseases.html")

        html_button2 = tk.Button(button_frame,
                                 text='Go',
                                 command=open2,
                                 relief='raised',
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        html_button2.pack(padx=400, pady=20)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


class BMIPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label5_1 = tk.Label(self,
                                    text=' Body Mass Index ',
                                    font=('orbitron', 40, 'bold'),
                                    foreground='#ffffff',
                                    background='#3d3d5c',
                                    relief='raised',
                                    borderwidth=3,
                                    )
        heading_label5_1.pack(pady=10, anchor='w')

        def menu_page_func():
            controller.show_frame('MenuPage')

        menu_button4 = tk.Button(self,
                                 text='Menu',
                                 command=menu_page_func,
                                 relief='raised',
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        menu_button4.pack(pady=10, anchor='w')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        space_label1 = tk.Label(button_frame, height=4, bg='#33334d')
        space_label1.pack()

        height_label = tk.Label(button_frame,
                                text='Enter your Height (in M)',
                                font=('orbitron', 13),
                                bg='#33334d',
                                fg='white')
        height_label.pack(pady=10)

        my_height = tk.StringVar()
        height_entry_box = tk.Entry(button_frame,
                                    textvariable=my_height,
                                    font=('orbitron', 12),
                                    width=22)
        height_entry_box.focus_set()
        height_entry_box.pack(ipady=7)

        weight_label = tk.Label(button_frame,
                                text='Enter your Weight (in Kg)',
                                font=('orbitron', 13),
                                bg='#33334d',
                                fg='white')
        weight_label.pack(pady=10)

        my_weight = tk.StringVar()
        weight_entry_box = tk.Entry(button_frame,
                                    textvariable=my_weight,
                                    font=('orbitron', 12),
                                    width=22)
        weight_entry_box.pack(ipady=7)

        def bmi_calculation():
            space_label2['text'] = ""
            space_label3['text'] = ""
            space_label4['text'] = ""
            ht = float(height_entry_box.get())
            wt = int(weight_entry_box.get())
            ans = int(wt/(ht*ht))
            space_label2['text'] = "Your BMI is: "
            space_label3['text'] = ans
            if ans <= 18.5:
                space_label4['text'] = "You are Underweight"
            elif 18.5 < ans < 25:
                space_label4['text'] = "You are Normal"
            else:
                space_label4['text'] = "You are overweight"

        ok_button = tk.Button(button_frame,
                              text='OK',
                              command=bmi_calculation,
                              relief='raised',
                              borderwidth=3,
                              width=40,
                              height=3)
        ok_button.pack(pady=20)

        space_label2 = tk.Label(button_frame,
                                text='',
                                height=2,
                                bg='#33334d',
                                foreground='white',
                                font=('orbitron', 15))
        space_label2.pack()

        space_label3 = tk.Label(button_frame,
                                text='',
                                height=2,
                                bg='#33334d',
                                foreground='white',
                                font=('orbitron', 15))
        space_label3.pack()

        space_label4 = tk.Label(button_frame,
                                text='',
                                height=2,
                                bg='#33334d',
                                foreground='white',
                                font=('orbitron', 15))
        space_label4.pack()

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


class NotificationSettPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label6_1 = tk.Label(self,
                                    text=' Notification Settings ',
                                    font=('orbitron', 40, 'bold'),
                                    foreground='#ffffff',
                                    background='#3d3d5c',
                                    relief='raised',
                                    borderwidth=3,
                                    )
        heading_label6_1.pack(pady=10, anchor='w')

        def menu_page_func():
            controller.show_frame('MenuPage')

        menu_button5 = tk.Button(self,
                                 text='Menu',
                                 command=menu_page_func,
                                 relief='raised',
                                 borderwidth=3,
                                 width=20,
                                 height=3)
        menu_button5.pack(pady=10, anchor='w')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        space_label2 = tk.Label(button_frame, height=4, bg='#33334d')
        space_label2.pack()

        notification_label = tk.Label(button_frame,
                                      text='Enter your Health Notification',
                                      font=('orbitron', 13),
                                      bg='#33334d',
                                      fg='white')
        notification_label.pack(pady=10)

        my_notification = tk.StringVar()
        notification_entry_box = tk.Entry(button_frame,
                                          textvariable=my_notification,
                                          font=('orbitron', 12),
                                          width=22)
        notification_entry_box.focus_set()
        notification_entry_box.pack(ipady=8, ipadx=50)

        notification_label2 = tk.Label(button_frame,
                                       text='Set Reminder Time (in Minutes)',
                                       font=('orbitron', 13),
                                       bg='#33334d',
                                       fg='white')
        notification_label2.pack(pady=10)

        my_notification2 = tk.StringVar()
        notification_entry_box2 = tk.Entry(button_frame,
                                           textvariable=my_notification2,
                                           font=('orbitron', 12),
                                           width=22)
        notification_entry_box2.pack(ipady=8, ipadx=50)

        notification_label3 = tk.Label(button_frame,
                                       text='How many times do you want the reminder?',
                                       font=('orbitron', 13),
                                       bg='#33334d',
                                       fg='white')
        notification_label3.pack(pady=10)

        my_notification3 = tk.StringVar()
        notification_entry_box3 = tk.Entry(button_frame,
                                           textvariable=my_notification3,
                                           font=('orbitron', 12),
                                           width=22)
        notification_entry_box3.pack(ipady=8, ipadx=50)

        def notify_me():
            reminder_text = str(my_notification.get())
            reminder_time = float(my_notification2.get()) * 60
            reminder_frequency = int(my_notification3.get())
            i = 0
            while i <= reminder_frequency:
                plyer.notification.notify(
                    title="HEALTH REMINDER ",
                    message=reminder_text,
                    timeout=30,
                    app_icon='healthrem.ico'
                )
                time.sleep(reminder_time)
                i = i+1

        ok_button2 = tk.Button(button_frame,
                               text='OK',
                               command=notify_me,
                               relief='raised',
                               borderwidth=3,
                               width=40,
                               height=3)
        ok_button2.pack(pady=30)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()