class Buf:

    def __init__(self, type, value, duration):
        self.type = type
        self.value = value
        self.duration = duration

    def __get_type__(self):
        return  self.type

    def __get_value__(self):
        return self.value

    def __get_duration__(self):
        return self.duration

    def __set_type__(self, type):
        self.type = type

    def __set_value__(self, value):
        self.value = value

    def __set_duration__(self, duration):
        self.duration = duration
