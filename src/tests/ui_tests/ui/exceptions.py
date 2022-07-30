class CustomTimeoutException(Exception):

    def __init__(self, message=''):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.__class__.__name__} while using SeleniumWebdriver \n{self.message}"


class CustomNoSuchElementException(Exception):

    def __init__(self, message=''):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.__class__.__name__} while using SeleniumWebdriver \n{self.message}"