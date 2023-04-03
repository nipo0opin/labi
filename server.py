import socket


active_list=['loacalhost']

mass = ['localhost', '124.0.0.234']

class sort():
    def sort(msg):
        if "update" in msg:
            update.update("update")
        else:
            send.send(parse.parseid(msg), parse.parsemsg(msg))
            
class send():
    def send(_id, _msg):
        pass
        #-call id to ip
        #-send msg OR update
        
    pass

class update():
    def update():
        pass
    pass

class parse():
    def parse_id(msg):
        pass
        #return _id
    
    def parsemsg(msg):
        pass
        #return msg_
    
    def parseid_(msg):
        pass
        #return id_
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
sock.bind(('', 55000))  # связываем сокет с портом, где он будет ожидать сообщения
sock.listen(10)  # указываем сколько может сокет принимать соединений
print('Server is running, please, press ctrl+c to stop')

while True:
    conn, addr = sock.accept()  # начинаем принимать соединения
    
    print('connected:', addr)  # выводим информацию о подключении
    
    data = conn.recv(1024)  # принимаем данные от клиента, по 1024 байт

    print(data.decode('UTF-8'))

    tmp_data=data.decode('UTF-8')
    
    conn.send(data)
conn.close()  # закрываем соединение
