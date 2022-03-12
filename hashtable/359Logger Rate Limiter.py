class Logger:

    def __init__(self):
        self.hashMap={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        key=hash(message)
        if timestamp-self.hashMap.get(key,-10)>=10:
            self.hashMap[key]=timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)