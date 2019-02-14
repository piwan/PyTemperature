class Temperature:
    """Temperature conversion and presentation class"""

    def __init__(self, celsius=0):
        """
        Construct new Temperature
        :param celsius: temperature value in Celsius
        """
        self.celsius = celsius

    @property
    def celsius(self):
        """Temperature value in Celsius degrees"""
        return self._value

    @celsius.setter
    def celsius(self, value):
        if (value < -273):
            raise AbsoluteZeroError(value)
        else:
            self._value = value

    @property
    def fahrenheit(self):
        """Temperature value in Fahrenheit degrees"""
        return (self.celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


class AbsoluteZeroError(Exception):
    """An exception thrown when the value is below absolute zero (-273 Celsius)"""

    def __init__(self, value):
        """
        Create new exception
        :param value the value that is lower than absolute zero point
        """
        super().__init__(f'Value {value} is below absolute zero point')
