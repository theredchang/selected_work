import threading
from netmiko import ConnectHandler

def worker1():
    connection = ConnectHandler(
        device_type='cisco_ios_telnet',
        host = "192.168.79.131",
        username="",
        password="",
        port=30011


    )
    connection.send_command("sh ip int b")
    output = connection.send_command("sh ip int b")
    print(output)

def worker2():
    connection = ConnectHandler(
        device_type='cisco_ios_telnet',
        host = "192.168.79.131",
        username="",
        password="",
        port=30012

    )
    connection.send_command("sh ip int b")
    output = connection.send_command("sh ip int b")
    print(output)

t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)

t1.start()
t2.start()
t1.join()
t2.join()