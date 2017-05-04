from Tkinter import *
import serial
ser=serial.Serial()
ser.port="COM18"
ser.baudrate=9600
ser.open()

login=Tk()
i=3
username="default"
password="default"
def get_info():
    username=username_entry.get()
    password=password_entry.get()
   

    if(username=="sharath"):
        print "Username Verified"
        if(password=="sharath"):
            print "password Verified"
           
            master = Tk()
            heading=Label(master, text="WELCOME TO HOME AUTOMATION WIZARD")
            heading.place(relx=1, x=-900, y=10)
            a=ser.isOpen()
            if (a):
                serial_status=Label(master, text="Connection Established")
                serial_status.place(relx=1, x=-240, y=100)
            
            else :
                               serial_status2=Label(master, text="Connection Failed")
                               serial_status2.place(relx=1, x=-240, y=100)



            def light1c():
                print "LIGHT 1"
                ser.write("0")

            def light2c():
                print "LIGHT 2"
                ser.write("1")

            def light3c():
                print "light 3"
                ser.write("2")

            def light4c():
                print "LIGHT 4"
                ser.write("3")

            def light5c():
                print "LIGHT 4"
                ser.write("4")

            def fan1c():
                print "FAN 1"
                ser.write("5")

            def fan2c():
                print "FAN 2"
                ser.write("6")

            def fan3c():
                print "FAN 3"
                ser.write("7")

            def gatec():
                print "gate "
                ser.write("8")

            def motorc():
                print "motor"
                ser.write("9")

            def buzzerc():
                print "Buzzer Turned off"
                ser.write("p")
            def shutdown():
                print "ALL TURNED OFF"
                ser.write("q")
            def fan_speed1(i):
                
                if(i>0):
                   
                    if (i=="1"):
                        ser.write("a")
                        print "controlling the speed of fan",i
                    if(i=="2"):
                        ser.write("b")
                        print "controlling the speed of fan",i
                    if(i=="3"):
                        ser.write("c")
                        print "controlling the speed of fan",i
                    if(i=="4"):
                        ser.write("d")
                        print "controlling the speed of fan",i
                    if(i=="5"):
                        ser.write("e")
                        print "controlling the speed of fan",i
                    

                    
            def fan_speed2(i):
                if(i>0):
                    print "controlling the speed of fan"
                    if (i=="1"):
                        ser.write("f")
                    if(i=="2"):
                        ser.write("g")
                    if(i=="3"):
                        ser.write("h")
                    if(i=="4"):
                        ser.write("i")
                    if(i=="5"):
                        ser.write("j")

            def fan_speed3(i):
                if(i>0):
                    print "controlling the speed of fan"
                    if (i=="1"):
                        ser.write("k")
                    if(i=="2"):
                        ser.write("l")
                    if(i=="3"):
                        ser.write("m")
                    if(i=="4"):
                        ser.write("n")
                    if(i=="5"):
                        ser.write("o")
             


            light1= Button(master, text="LIGHT 1",bd="5",height="5", width="10", command=light1c)
            light1.place(relx=1, x=-1400, y=100)

            light2= Button(master, text="LIGHT 2",bd="5",height="5", width="10", command=light2c)
            light2.place(relx=1, x=-1160, y=100)

            light3= Button(master, text="LIGHT 3",bd="5",height="5", width="10", command=light3c)
            light3.place(relx=1, x=-920, y=100)

            light4= Button(master, text="LIGHT 4",bd="5",height="5", width="10", command=light4c)
            light4.place(relx=1, x=-680, y=100)

            light5= Button(master, text="LIGHT 5",bd="5",height="5", width="10", command=light5c)
            light5.place(relx=1, x=-440, y=100)

            fan1= Button(master, text="FAN 1", bd="5",width="27", height="5", command=fan1c)
            fan1.place(relx=1, x=-1400, y=250)

            fan1spd= Scale(master, label="FAN 1", orient="horizontal", width="30", to="5",length="200",command=fan_speed1)
            fan1spd.place(relx=1, x=-1400, y=350)


            fan2= Button(master, text="FAN 2",bd="5",width="27", height="5", command=fan2c)
            fan2.place(relx=1, x=-950, y=250)

            fan2spd= Scale(master, label="FAN 2", orient="horizontal", width="30", to="5",length="200", command=fan_speed2)
            fan2spd.place(relx=1, x=-950, y=350)

            fan3= Button(master, text="FAN 3",bd="5",width="27", height="5", command=fan3c)
            fan3.place(relx=1, x=-550, y=250)

            fan3spd= Scale(master, label="FAN 3", orient="horizontal", width="30", to="5",length="200",command=fan_speed3)
            fan3spd.place(relx=1, x=-550, y=350)

            gate= Button(master, text="GATE ",bd="5" ,height="5", width="20",command=gatec)
            gate.place(relx=1, x=-1300, y=500)

            motor= Button(master, text="MOTOR",bd="5",height="5", width="20", command=motorc)
            motor.place(relx=1, x=-600, y=500)

            buzzer= Button(master, text="Buzzer STOP",bd="5",height="5", width="20", command=buzzerc)
            buzzer.place(relx=1, x=-1000, y=500)

            shut_down= Button(master, text="TURN OFF ALL DEVICES",bd="5",height="5", width="150", command=shutdown)
            shut_down.place(relx=1, x=-1400, y=650)




        else :
           
            print "Wrong password"
            wrong_password=Label(login, text="Wrong password TRY  AGAIN!!!!", fg="RED")
            wrong_password.place(relx=1, x=-1200, y=300, anchor="ne")
            
           
    else :
       
        print "wrong Username"
        wrong_username=Label(login, text="Wrong username TRY  AGAIN!!!!", fg="RED")
        wrong_username.place(relx=1, x=-1200, y=300, anchor="ne")
       
       



    
head=Label(login, text="Login to the house")
head.pack()

username_label=Label(login, text="USERNAME:")
username_label.place(relx=1, x=-1400, y=100, anchor="ne")

password_label=Label(login, text="PASSWORD:")
password_label.place(relx=1, x=-1400, y=200, anchor="ne")

username_entry=Entry(login)
username_entry.place(relx=1, x=-1200, y=100, anchor="ne")

password_entry=Entry(login,show="x")
password_entry.place(relx=1, x=-1200, y=200, anchor="ne")

login_button=Button(login, text="LOG-in", command=get_info)
login_button.place(relx=1, x=-1200, y=400, anchor="ne")

mainloop()
