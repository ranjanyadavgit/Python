server_config = {

    'server1': {'ip': '192.168.1.1','port':'8000','status':'active'},
    'server2': {'ip': '192.168.1.2','port':'8080','status':'active'},
    'server3': {'ip': '192.168.1.3','port':'9000','status':'inactive'}
}

def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status','server not found')


server_name='server3'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")

-----
Lenovo@DESKTOP-M5DT73G MINGW64 /c/Python/day-11
$ python practical.py 
server3 status: inactive
