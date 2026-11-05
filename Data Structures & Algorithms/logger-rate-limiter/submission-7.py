class Logger:

    def __init__(self):
        self.allowed = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.allowed:
            self.allowed[message] = timestamp
            return True

        if timestamp - self.allowed[message] >= 10:
            self.allowed[message] = timestamp
            return True

        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
