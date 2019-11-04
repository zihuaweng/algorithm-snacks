#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/logger-rate-limiter/


# Time complexity: O()
# Space complexity: O()


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.should_print = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp < self.should_print.get(message, 0):
            return False
        else:
            self.should_print[message] = timestamp + 10
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)