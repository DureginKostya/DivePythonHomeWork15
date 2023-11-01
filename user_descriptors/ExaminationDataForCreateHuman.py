from user_exceptions.ExceptionsForCreateHuman import InvalidIdError, InvalidNameError, InvalidAgeError


class ExaminationData:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if (self.param_name == '_last_name' or
                self.param_name == '_first_name' or
                self.param_name == '_patronymic'):
            if not isinstance(value, str) or len(value.strip()) == 0:
                raise InvalidNameError(value)
            setattr(instance, self.param_name, value)
        if self.param_name == '_age':
            if not isinstance(value, int) or value < 0:
                raise InvalidAgeError(value)
            setattr(instance, self.param_name, value)
        if self.param_name == '_id_employee':
            if not isinstance(value, int) or value < 100_000 or value > 999_999:
                raise InvalidIdError(value)
            setattr(instance, self.param_name, value)