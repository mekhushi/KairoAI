import json
import os

class MemoryManager:
    def __init__(self, path="conversation.json"):
        self.path = path
        if os.path.exists(path):
            with open(path, "r") as f:
                self.history = json.load(f)
        else:
            self.history = []

    def add(self, role, message):
        self.history.append({"role": role, "message": message})
        with open(self.path, "w") as f:
            json.dump(self.history, f, indent=2)

    def get_history(self):
        return "\n".join([f"{h['role']}: {h['message']}" for h in self.history])
