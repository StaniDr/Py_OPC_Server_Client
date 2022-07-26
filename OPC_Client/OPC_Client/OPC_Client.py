
import tkinter as tk
#from turtle import left, right
import tk_tools
import opcua
 
# Connect to the OPC-UA server as a client
client = opcua.Client("opc.tcp://localhost:4840")
client.connect()
print("Client Connected")

root = tk.Tk()
root.title("OPC-UA Client Station 1")

root.geometry('300x500')

#кнопка - открыть
def update_butO():
   but1 = client.get_node("ns=2;i=2")
   but1.set_value(True)

#кнопка - закрыть
def update_butC():
   but2 = client.get_node("ns=2;i=3")
   but2.set_value(True)

#переключатель-имит.пол.сигнала "открыт"
def update_butNO():
   but3 = client.get_node("ns=2;i=6")
   if not but3.get_value():
        but3.set_value(True)
   else:
        but3.set_value(False)

#переключатель-имит.пол.сигнала "закрыт"
def update_butNC():
   but4 = client.get_node("ns=2;i=7")
   if not but4.get_value():
        but4.set_value(True)
   else:
        but4.set_value(False)

#кнопка - сброс(квитировать аварию)
def update_butR():
   but5 = client.get_node("ns=2;i=9")
   but5.set_value(True)

#---------------------------------------------------------
#кнопка - открыть V2
def update_butO_v2():
   but11 = client.get_node("ns=2;i=10")
   but11.set_value(True)

#кнопка - закрыть V2
def update_butC_v2():
   but12 = client.get_node("ns=2;i=11")
   but12.set_value(True)
#----------------------------------------------------------
#кнопка - открыть
def update_butO_fdv1():
   but1_fdv1 = client.get_node("ns=2;i=16")
   but1_fdv1.set_value(True)

#кнопка - закрыть
def update_butC_fdv1():
   but2_fdv1 = client.get_node("ns=2;i=17")
   but2_fdv1.set_value(True)

#-------------------------------------------------------------
#кнопка - открыть
def update_butO_p1f1v1():
   but1_p1f1v1 = client.get_node("ns=2;i=20")
   but1_p1f1v1.set_value(True)

#кнопка - закрыть
def update_butC_p1f1v1():
   but2_p1f1v1 = client.get_node("ns=2;i=21")
   but2_p1f1v1.set_value(True)


v_name = tk.Label(text="d_valve:", fg="white", bg="black", width=33)
v_name.place(x=0,y=0)

labOpen = tk.Label(text="Opened", fg="black", bg="gray", width=10)
labOpen.place(x=0,y=22, height = 25)

butOpen = tk.Button(text="Open", width=10, command = update_butO)
butOpen.place(x=80,y=22)

butNuOpen = tk.Button(text="NU_Open", width=10, command = update_butNO)
butNuOpen.place(x=160,y=22)

labClose = tk.Label(text="Closed", fg="black", bg="gray", width=10)
labClose.place(x=0,y=50, height = 25)

butClose = tk.Button(text="Close", width=10, command = update_butC)
butClose.place(x=80,y=50)

butNuClose = tk.Button(text="NU_Close", width=10, command = update_butNC)
butNuClose.place(x=160,y=50)

labAlarm = tk.Label(text="Alarm", fg="black", bg="gray", width=10)
labAlarm.place(x=0,y=78, height = 25)

butReset = tk.Button(text="Reset", width=10, command = update_butR)
butReset.place(x=80,y=78)

#------------------------- V2 --------------------------------------
v_name_v2 = tk.Label(text="an_valve:", fg="white", bg="black", width=33)
v_name_v2.place(x=0,y=110)

labOpen_v2 = tk.Label(text="Opened", fg="black", bg="gray", width=10)
labOpen_v2.place(x=0,y=132, height = 25)

butOpen_v2 = tk.Button(text="Open", width=10, command = update_butO_v2)
butOpen_v2.place(x=80,y=132)

labClose_v2 = tk.Label(text="Closed", fg="black", bg="gray", width=10)
labClose_v2.place(x=0,y=160, height = 25)

butClose_v2 = tk.Button(text="Close", width=10, command = update_butC_v2)
butClose_v2.place(x=80,y=160)

labUst_v2 = tk.Label(text="Ust_Pol", fg="black", bg="gray", width=10)
labUst_v2.place(x=0,y=200, height = 25)

entry_ust = tk.Entry(fg="white", bg="gray", bd = 2, width=12, justify = 'center')
entry_ust.place(x=80,y=200, height = 25)

labNu_v2 = tk.Label(text="Curr_Pol", fg="black", bg="gray", width=10)
labNu_v2.place(x=0,y=228, height = 25)

entry_nu = tk.Entry(fg="white", bg="gray", bd = 2, width=12, justify = 'center')
entry_nu.place(x=80,y=228, height = 25)

entry_ust.insert(0,50)

#--------------------- установка f1 ------------------------------------

v_name_fdv1 = tk.Label(text="Facility_dvalv1:", fg="white", bg="black", width=33)
v_name_fdv1.place(x=0,y=255)

labOpen_fdv1 = tk.Label(text="Opened", fg="black", bg="gray", width=10)
labOpen_fdv1.place(x=0,y=280, height = 25)

butOpen_fdv1 = tk.Button(text="Open", width=10, command = update_butO_fdv1)
butOpen_fdv1.place(x=80,y=280)

labClose_fdv1 = tk.Label(text="Closed", fg="black", bg="gray", width=10)
labClose_fdv1.place(x=0,y=310, height = 25)

butClose_fdv1 = tk.Button(text="Close", width=10, command = update_butC_fdv1)
butClose_fdv1.place(x=80,y=310)

#--------------------- завод p1 установка f1 клапан v1 ------------------------------------

v_name_p1f1v1 = tk.Label(text="Plant1_F1_V1:", fg="white", bg="black", width=33)
v_name_p1f1v1.place(x=0,y=340)

labOpen_p1f1v1 = tk.Label(text="Opened", fg="black", bg="gray", width=10)
labOpen_p1f1v1.place(x=0,y=365, height = 25)

butOpen_p1f1v1 = tk.Button(text="Open", width=10, command = update_butO_p1f1v1)
butOpen_p1f1v1.place(x=80,y=365)

labClose_p1f1v1 = tk.Label(text="Closed", fg="black", bg="gray", width=10)
labClose_p1f1v1.place(x=0,y=395, height = 25)

butClose_p1f1v1 = tk.Button(text="Close", width=10, command = update_butC_p1f1v1)
butClose_p1f1v1.place(x=80,y=395)



def update_hmi():
    # update the gauges with the OPC-UA values every 1 second
   #entry.delete(0, 5)
   #entry.insert(0,client.get_node("ns=2;i=2").get_value())
   #temp = client.get_node("ns=2;i=3")
   #temp.set_value(entry2.get())

   #открыт - кнопку маскируем
   if client.get_node("ns=2;i=4").get_value():
        labOpen.configure(bg="green")
        butOpen.configure(state = 'disabled')
   else:
        labOpen.configure(bg="gray")
        butOpen.configure(state = 'normal')

   #закрыт - кнопку маскируем
   if client.get_node("ns=2;i=5").get_value():
        labClose.configure(bg="green")
        butClose.configure(state = 'disabled')  
   else:
        labClose.configure(bg="gray")
        butClose.configure(state = 'normal')
   
   #кнопка - имитация пол.сигнала открыт  
   if client.get_node("ns=2;i=6").get_value():
        butNuOpen.configure(bg="green")
   else:
        butNuOpen.configure(bg="white")

   #кнопка - имитация пол.сигнала закрыт 
   if client.get_node("ns=2;i=7").get_value():
        butNuClose.configure(bg="green")
   else:
        butNuClose.configure(bg="white")

   #индикатор - авария
   if client.get_node("ns=2;i=8").get_value():
        labAlarm.configure(bg="red")
   else:
        labAlarm.configure(bg="gray")

#---------------------------------------------------
   #открыт - кнопку маскируем
   if client.get_node("ns=2;i=12").get_value():
        labOpen_v2.configure(bg="green")
        butOpen_v2.configure(state = 'disabled')
   else:
        labOpen_v2.configure(bg="gray")
        butOpen_v2.configure(state = 'normal')

   #закрыт - кнопку маскируем
   if client.get_node("ns=2;i=13").get_value():
        labClose_v2.configure(bg="green")
        butClose_v2.configure(state = 'disabled')  
   else:
        labClose_v2.configure(bg="gray")
        butClose_v2.configure(state = 'normal')

   entry_nu.delete(0, 5)
   entry_nu.insert(0,client.get_node("ns=2;i=15").get_value())

   #entry_ust.delete(0, 5)
   #entry_ust.insert(0,client.get_node("ns=2;i=14").get_value())

   temp = client.get_node("ns=2;i=14")
   temp.set_value(entry_ust.get())
#-------------------- f1 ---------------------------------------
   #открыт - кнопку маскируем
   if client.get_node("ns=2;i=18").get_value():
        labOpen_fdv1.configure(bg="green")
        butOpen_fdv1.configure(state = 'disabled')
   else:
        labOpen_fdv1.configure(bg="gray")
        butOpen_fdv1.configure(state = 'normal')

   #закрыт - кнопку маскируем
   if client.get_node("ns=2;i=19").get_value():
        labClose_fdv1.configure(bg="green")
        butClose_fdv1.configure(state = 'disabled')  
   else:
        labClose_fdv1.configure(bg="gray")
        butClose_fdv1.configure(state = 'normal')

#-------------------- p1 ---------------------------------------
   #открыт - кнопку маскируем
   if client.get_node("ns=2;i=22").get_value():
        labOpen_p1f1v1.configure(bg="green")
        butOpen_p1f1v1.configure(state = 'disabled')
   else:
        labOpen_p1f1v1.configure(bg="gray")
        butOpen_p1f1v1.configure(state = 'normal')

   #закрыт - кнопку маскируем
   if client.get_node("ns=2;i=23").get_value():
        labClose_p1f1v1.configure(bg="green")
        butClose_p1f1v1.configure(state = 'disabled')  
   else:
        labClose_p1f1v1.configure(bg="gray")
        butClose_p1f1v1.configure(state = 'normal')
#-----------------------------------------------------------------
   root.after(1000, update_hmi)
 
root.after(500, update_hmi)
 
root.mainloop()





input("Press any key...")



 

