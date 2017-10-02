#!/usr/bin/env python3

import websocket
import requests

def get_token():
    print("Making token request")
    r = requests.get('https://tinychat.com/api/v1.0/room/token/' + room)
    result = r.json()
    token = result['result']
    return token

def connect_socket():
    header = [
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3040.0 Safari/537.36',
        'Accept-Language: en-US,en;q=0.8',
        'Accept-Encoding: gzip, deflate, sdch, br',
        'Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits'
    ]

    # This connect function's parameters MUST not be changed.
    ws.connect(
        "wss://wss.tinychat.com",
        header=header,
        host="wss.tinychat.com",
        origin="https://tinychat.com",
        subprotocols=["tc"]
    )

def connect_room():
    # This packet's structure MUST not be changed.
    connect_msg = '{"tc":"join","req":1,"useragent":"tinychat-client-webrtc-chrome_win32-2.0.9-255","token":"' + get_token() + '","room":"' + room + '","nick": "'+ nickname +'"}'
    send_msg(connect_msg)

def send_msg(msg):
    ws.send(msg)

if __name__ == "__main__":
    room = input("What room? ")
    nickname = input("What is your nickname? ")

    ws = websocket.WebSocket()
    connect_socket()
    connect_room()

    while True:
        print(ws.next())
