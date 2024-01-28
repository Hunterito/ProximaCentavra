class FourDigitYearConverter:  # класс конвертирует регулярное выражение в URL
    regex = "[0-9]{4}"

    def to_python(self, value):  # преобразование к целому числу
        return int(value)

    def to_url(self, value):
        return "%04d" % value