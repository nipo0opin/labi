from kivy.app import App, ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDRoundFlatButton, MDFillRoundFlatButton, MDFlatButton
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.textinput import TextInput
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.icon_definitions import md_icons
import socket

 
#class CustomLayout(Screen):
#    def __init__(self, **kwargs):
#        super(CustomLayout, self).__init__(**kwargs)
#    def func(self):
#        print("hello is a function")
#class SimpleLay(Screen):
 #   staff =   ObjectProperty(None)
 #   def __init__(self, **kwargs):
 #       super(SimpleLay, self).__init__(**kwargs)
 #   def smak(self):
 #       print("korolivskii smak") 
 #   def sdsd(self):
#        self.root.ids.labl.lab.text = "asdasd"

#on_press: root.manager.current = 'cust'
#on_press: root.smak()

self_id = 101

server_port = 55000
massage=""
identeficator = 0
adres_id=0

#class MSG()
    
def send_massage(_id, _msg):
    print("id ",_id," _msg ",_msg)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(mainApp.ip_server)
    if sock.connect((mainApp.ip_server, server_port)):
            print("error conection")
    else:
        sock.send(bytes(str(self_id)+"_"+_msg+"_"+str(_id), encoding = 'UTF-8'))  
        data = sock.recv(1024)  
        analize(data)
        sock.close()
        
def analize(recv_data):
    print("analize_recv_data :",recv_data.decode('UTF-8'))

    
class update():
    def update_chat(_id):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((mainApp.ip_server, server_port))
        s.send(bytes("update_"+str(_id), encoding='UTF-8'))
        tmp=s.recv(1024)
        print("update:",tmp)
        return tmp.decode('UTF-8')
    
class ex_contact(BoxLayout):
    pass

class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def tests(self):
        pass
    
    pass
class CustomMassage(MDFillRoundFlatButton):
    root_mas = ObjectProperty()
    
    def on_release(self, **kwargs):
        super().on_release(**kwargs)
        self.root_mas.msg_callback(self)
        
class CustomButton(MDFillRoundFlatButton):
    root_widget = ObjectProperty()

    def on_release(self, **kwargs):
        super().on_release(**kwargs)
        self.root_widget.btn_callback(self)
        
class Massanger(Screen):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        
    def msg_callback(self, btn):
        print("massage text = ", btn.text)
        
            
    def init_massage(self, txtx):
        #if len(txtx) > 0 and txtx != " Input you massage... ":
        massage = txtx
        self.ids.txt.text= ""
        _id = adres_id
            #----socket----
        send_massage(Contacts.getid(), massage)
            ##------inserting----massages------------
        self.ids.massage_space.data.insert(0,{'text':str(massage), 'root_mas':self})#{'text':str(massage), 'pos_hint': {'right':1, 'center_X':'None'}, 'color':'white', 'background_color':(0,.38,.64,1), 'root_mas':self})
       
    def but_upd(self):
        update.update_chat(Contacts.idn)
        
    def set_but(self):
        print(self)
        self.ids.send_texture.size = self.ids.send_button.size
        self.ids.send_texture.pos = self.ids.send_button.pos
        self.ids.back_texture.size = self.ids.back_button.size
        self.ids.back_texture.pos = self.ids.back_button.pos
        self.ids.txt.text= " Input you massage... " 
    pass


class Profile(Screen):
    def setip(self, txt):
        mainApp.ip_server = txt
        self.ids.ipaddress.text=""
        print("ip confirmed :",mainApp.ip_server)
    pass


class Contacts(Screen):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        

    idn = 0
    
    def init_addr_id(self, ide):
        Contacts.idn = ide
        print(self," root")
        self.manager.current='massanger'
        print(Contacts.idn, "addres id")
    def getid():
        return Contacts.idn
        
    def addContact(self, txt):
        if len(str(txt)):
            self.ids.contacts_space.data.insert(0,{'text':str(txt), 'root_widget':self})
            self.ids.labelcontact.text=""
        pass
    def btn_callback(self, btn):
        Contacts.init_addr_id(self, btn.text)
        print(btn, btn.text)
    


    
class mainApp(MDApp):
    ip_server = 'localhost'
    def build(self):
        #Clock.max_iteration=20
        sm = ScreenManager()
        sm.add_widget(Contacts(name='contacts'))
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Massanger(name='massanger'))
        sm.add_widget(Profile(name='profile'))
        global root
        root = self.root
        #sm.add_widget(CustomLayout(name='cust'))
        
        return sm
    
        
mainApp().run()

