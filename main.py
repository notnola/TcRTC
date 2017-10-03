#!/usr/bin/env python3

import json
import requests
import websocket


def get_token(room):
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


def connect_room(room, nickname):
    # This packet's structure MUST not be changed.
    send_msg({
        'tc': 'join',
        'req': 1,
        'useragent': 'tinychat-client-webrtc-chrome_win32-2.0.9-255',
        'token': get_token(room),
        'room': room,
        'nick': nickname
    })


def on_msg(msg):
    print(msg)
    if msg['tc'] == 'ping':
        send_msg({
            'tc': 'pong'
        })


def send_msg(msg):
    '''Sends a json message to the Tinychat server.
    `msg` must be a value compatible with json.dumps.'''
    ws.send(json.dumps(msg))


if __name__ == "__main__":
    room = input("What room? ")
    nickname = input("What is your nickname? ")

    ws = websocket.WebSocket()
    connect_socket()
    connect_room(room, nickname)

    while True:
        msg = json.loads(ws.next())
        on_msg(msg)
