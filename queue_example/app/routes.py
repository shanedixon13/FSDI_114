from flask import Flask, request

app = Flask(__name__)

class Queue:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return self.items ==[]
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)

QUEUE = Queue()

@app.get("/messages/<int:qty>")
def get_messages(qty):
    out = {"messages": []}
    messages = []
    if not QUEUE.is_empty():
        while not QUEUE.is_empty() and qty > 0:
            messages.append(QUEUE.dequeue())
            qty -= 1
    out["messages"] = messages
    return out

@app.post("/messages")
def post_message():
    msg = request.json
    QUEUE.enqueue(msg)
    return "OK", 204

