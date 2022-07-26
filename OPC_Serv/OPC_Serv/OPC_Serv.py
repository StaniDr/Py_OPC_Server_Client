
import opcua
import random
import time

from abc import ABC, abstractmethod


confOPC = []

def add(x, y):
    return x + y

def is_positive(x):
    return x > 0

try:
    myFile = open('config.txt','r')
except IOError as e:
    print('NoFileFound config.txt')
else:
    with myFile:
        for line in myFile:
          confOPC.append(line.strip())

        name_OPC  = confOPC[0]
        opc_address  = confOPC[1]
        https_address = confOPC[2]
        name_obj_1  = confOPC[3]


s = opcua.Server()
s.set_server_name(name_OPC)
s.set_endpoint(opc_address)
   
# Register the OPC-UA namespace
idx = s.register_namespace(https_address)
# start the OPC UA server (no tags at this point)  
s.start() 
   
objects = s.get_objects_node()
myobject = objects.add_object(idx, name_obj_1)
 
#теги по объектам теоретически можно впоследствии скомпоновать через массивы структур
var1 = myobject.add_variable(idx, 'v1_cmd_open', 0)
var1.set_writable(writable=True)
   
var2 = myobject.add_variable(idx, 'v1_cmd_close', 0)
var2.set_writable(writable=True)

var3 = myobject.add_variable(idx, 'v1_out_open', 0)
var3.set_writable(writable=True)

var4 = myobject.add_variable(idx, 'v1_out_close', 0)
var4.set_writable(writable=True)

var5 = myobject.add_variable(idx, 'v1_nu_open', 0)
var5.set_writable(writable=True)

var6 = myobject.add_variable(idx, 'v1_nu_close', 0)
var6.set_writable(writable=True)

var7 = myobject.add_variable(idx, 'v1_out_alarm', 0)
var7.set_writable(writable=True)

var8 = myobject.add_variable(idx, 'v1_cmd_reset', 0)
var8.set_writable(writable=True)

#-------------------------------------------------------------------
var10 = myobject.add_variable(idx, 'v2_cmd_open', 0)
var10.set_writable(writable=True)
   
var11 = myobject.add_variable(idx, 'v2_cmd_close', 0)
var11.set_writable(writable=True)

var12 = myobject.add_variable(idx, 'v2_out_open', 0)
var12.set_writable(writable=True)

var13 = myobject.add_variable(idx, 'v2_out_close', 0)
var13.set_writable(writable=True)

var14 = myobject.add_variable(idx, 'v2_ust_pol', 0)
var14.set_writable(writable=True)

var15 = myobject.add_variable(idx, 'v2_nu_pol', 0)
var15.set_writable(writable=True)
#------------------------------------------------------------------
var16 = myobject.add_variable(idx, 'f1_dv1_cmd_open', 0)
var16.set_writable(writable=True)
   
var17 = myobject.add_variable(idx, 'f1_dv1_cmd_close', 0)
var17.set_writable(writable=True)

var18 = myobject.add_variable(idx, 'f1_dv1_out_open', 0)
var18.set_writable(writable=True)

var19 = myobject.add_variable(idx, 'f1_dv1_out_close', 0)
var19.set_writable(writable=True)
#------------------------------------------------------------------
var20 = myobject.add_variable(idx, 'p1_f1_v1_cmd_open', 0)
var20.set_writable(writable=True)
   
var21 = myobject.add_variable(idx, 'p1_f1_v1_cmd_close', 0)
var21.set_writable(writable=True)

var22 = myobject.add_variable(idx, 'p1_f1_v1_out_open', 0)
var22.set_writable(writable=True)

var23 = myobject.add_variable(idx, 'p1_f1_v1_out_close', 0)
var23.set_writable(writable=True)
  
# Create some simulated data

#-------------------- клапан(абстр.родит.класс) ---------------    
class Valve(ABC):

    def __init__(self):
    #сигналы обратной связи(полевого уровня)
        self.nu_open = False
        self.nu_close = False
    #неисправность
        self.out_alarm = False

    #методы для установки состояния
    @abstractmethod
    def set_open(self):
        self.out_open  = True
        self.out_close = False

    @abstractmethod
    def set_close(self):
        self.out_open  = False
        self.out_close = True

    @abstractmethod
    def reset_alarm(self):
        pass

    @abstractmethod
    def get_open(self):
        return(self.out_open)

    @abstractmethod
    def get_close(self):
        return(self.out_close)


#---------------- дискретный клапан --------------------------
class dValve(Valve):  
    
  timer_nsp_start = False
  timer_nsp_pt = 10
  timer_nsp_q = False

  #команды для нижнего(полевого) уровня
  cmd_nu_open  = False
  cmd_nu_close = False

  #переопределение методов
  def set_open(self):
     super().set_open()
     self.cmd_nu_open = True
     self.cmd_nu_close = False

  def set_close(self):
     super().set_close()
     self.cmd_nu_open = False
     self.cmd_nu_close = True

  def get_open(self):
        return(self.cmd_nu_open and super().get_open())

  def get_close(self):
        return(self.cmd_nu_close and super().get_close())

  def reset_alarm(self):
        self.out_alarm = False
        self.timer_nsp_q = False


  #дополн.неисп.формировать по обратной связи через таймер
  #обработка логики команд и обр.связи = таймер 5сек
  def fc_nsp_cmd(self):     

       self.temp_alm = (self.cmd_nu_open and not self.nu_open) or (self.cmd_nu_close and not self.nu_close)

       if not self.temp_alm:
            self.timer_nsp = time.time()

       if self.temp_alm and not self.timer_nsp_q and not self.timer_nsp_start:
            self.timer_nsp = time.time()
            self.timer_nsp_start = True
       #контрольное время для отладки = 10сек
       if (time.time() - self.timer_nsp > 10) and not self.timer_nsp_q:
           self.timer_nsp_q = True
           self.timer_nsp_start = False
       
       return(self.timer_nsp_q)

  #формирование неисправности
  def set_alarm(self):
    if (self.nu_open and self.nu_close) or self.fc_nsp_cmd():
          self.out_alarm = True
          self.set_close() #при неисправности - закрыть

#------------------------ аналоговый клапан ---------------------------------------
class aValve(Valve): 

    nu_pos = -1  #задание для поленвого уровня
    #100-открыт, 0-закрыт

    #переопределение методов 
    #открыть
    def set_open(self):
        super().set_open()
        self.nu_pos = 100

    #закрыть
    def set_close(self):
        super().set_close()
        self.nu_pos = 0

    #уставка положения
    def set_pol(self, ust_pos):
        self.nu_pos = ust_pos

    def get_open(self):
        return((self.nu_pos == 100) and super().get_open())

    def get_close(self):
        return((self.nu_pos == 0) and super().get_close())

    def reset_alarm(self):
        self.out_alarm = False

#-------------------------- Установка -----------------------------------

class Facility:
    def __init__(self, name, dv, av): 
        self.name = name 
        self.dv1 = dv 
        self.av1 = av
 

#-------------------------- Завод ----------------------------------------

class Plant:
    def __init__(self, name, f1, f2): 
        self.name = name 
        self.inf1 = f1 
        self.inf2 = f2

    
#------------------------- объявления -------------------------------------
v1 = dValve()
v2 = aValve()

f1 = Facility("NA", dValve(), aValve())

temp_f1 = Facility("NA_1", dValve(), aValve())
temp_f2 = Facility("NA_2", dValve(), aValve())

p1 = Plant("NPZ", temp_f1, temp_f2)



while True:
#------------------ клапан дискр. v1 вызов -------------------------------------
#------------ обработка команд верх. уровня (клиента) 
    #получена команда открыть
    if var1.get_value():
       v1.set_open()
       var1.set_value(False)

    #получена команда закрыть
    if var2.get_value(): 
        v1.set_close()
        var2.set_value(False)

    #вернуть статус - открыто - закрыто    
    var3.set_value(v1.get_open())
    var4.set_value(v1.get_close())

    #команды для имитации нижнего уровня()
    v1.nu_open  = var5.get_value()
    v1.nu_close = var6.get_value()

    #проверка на неисправность
    v1.set_alarm()
    var7.set_value(v1.out_alarm)

    #квитировать неисправность
    if var8.get_value(): 
       v1.reset_alarm()
       var8.set_value(False)
#--------------------------------------------------------------------------------
#------------------ клапан аналог. v2 вызов -------------------------------------
    #получена команда открыть
    if var10.get_value():
       v2.set_open()
       var10.set_value(False)

    #получена команда закрыть
    if var11.get_value(): 
        v2.set_close()
        var11.set_value(False)

    #вернуть статус - открыто - закрыто    
    var12.set_value(v2.get_open())
    var13.set_value(v2.get_close())

    #v2.set_pol(var14.get_value())
    var15.set_value(v2.nu_pos)

#----------------- Установка f1 ---------------------------------
#------------------ клапан d. v1 вызов -------------------------------------
    #получена команда открыть
    if var16.get_value():
       f1.dv1.set_open()
       var16.set_value(False)

    #получена команда закрыть
    if var17.get_value(): 
        f1.dv1.set_close()
        var17.set_value(False)

    #вернуть статус - открыто - закрыто    
    var18.set_value(f1.dv1.get_open())
    var19.set_value(f1.dv1.get_close())

#----------------- Завод p1 ---------------------------------
#------------------ Установка f1. Клапан v1 вызов ----------------
    #получена команда открыть
    if var20.get_value():
       p1.inf1.dv1.set_open()
       var20.set_value(False)

    #получена команда закрыть
    if var21.get_value(): 
        p1.inf1.dv1.set_close()
        var21.set_value(False)

    #вернуть статус - открыто - закрыто    
    var22.set_value(p1.inf1.dv1.get_open())
    var23.set_value(p1.inf1.dv1.get_close())

    time.sleep(1)






