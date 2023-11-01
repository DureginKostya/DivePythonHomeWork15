class ExceptionsForCreateHuman(ValueError):
    pass


class InvalidNameError(ExceptionsForCreateHuman):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid name: {self.value}. Name should be a non-empty string.'


class InvalidAgeError(ExceptionsForCreateHuman):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid age: {self.value}. Age should be a positive integer.'


class InvalidIdError(ExceptionsForCreateHuman):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Invalid id: {self.value}. Id should be a 6-digit positive integer between 100000 and 999999.'
