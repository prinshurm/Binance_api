import websocket, json

cc = 'btcusd'
interval = '1m'


socket = f'wss://stream.binance.com:9443/ws/{cc}t@kline_{interval}'


def on_message(ws, message):
    print(message)


def on_close(ws, close_status_code, close_msg):
    print("connection closed")


ws = websocket.WebSocketApp(socket, on_message = on_message, on_close = on_close)

ws.run_forever()