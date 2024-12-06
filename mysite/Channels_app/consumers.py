from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })
    
    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": "Hello i got your message!",
        })

    def websocket_disconnect(self, event):
        self.send({
            "type": "websocket.close",
            "code": 1000,  # Close connection with status code 1normal closure)000 (
        })
        print("WebSocket disconnected")