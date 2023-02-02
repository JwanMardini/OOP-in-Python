class Dates:
    def __init__(self, date) -> None:
        self.__date = date

    def getDate(self):
        return self.__date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)
print(dateWithDash)

if (date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")
