import socketio
import json

sio = socketio.Client()

class chatSystem:  
    @property
    def config(self):
        with open("config.json") as f: return json.load(f)
    
    def run_site(self):
        url = "http://localhost:5000"
        sio.connect(url)
    
    @sio.event
    def connect():
        print("Connected")
        
    @sio.event
    def disconnect():
        print("Disconnected from server")
        
    @sio.on('message')
    def message(message):
        
        for current in message['server']: 
            if len(message['message']) >= 300: return
            if current in chatSystem().config['servers']: print(f"{message['username']}: {message['message']}"); return
    
    
    def send_message(self):
        while True:
            message = input()
            if len(message) >= 300: print("You are not allowed to send messages longer than 300"); continue
            sio.emit('message', {"message": message, "username": (chatSystem().config).get("username"), "server": chatSystem().config['servers']})
        
    
chat = chatSystem()
chat.run_site()
chat.send_message()
