class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        time = self.log.get(message, 0)

        if time == timestamp or time == 0:
            self.log[message] += 10
            return True
        else:
            return False

