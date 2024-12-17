from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send('{"type":"accept", "status":"accepted"}')

        #user = self.scope.get("user")
        #print(user)
        print(self.scope.get("user"))
        print(self.scope.get("user").id)
        print(self.scope.get("user").first_name)
        print(self.scope.get("user").last_name)

        print(self.scope.get("sessions"))
        
    def receive(self, text_data):
        print(text_data)

        self.send('{"type":"event_arrive", "status":"arrived"}')
    
    def disconnect(self, code):
        print(code)
        print("hello, the connection is stopped")