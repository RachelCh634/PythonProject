from datetime import datetime
from dateutil.relativedelta import relativedelta
class Exerciser(Person):

    def NumOfMonth(s):
        if s == 'month':
            return 1
        if s == 'halfYear':
            return 6
        if s == 'year':
            return 12

    def ReturnEndDate(date_str, num_months):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        new_date = date_obj + relativedelta(months=num_months)
        return new_date.strftime("%Y-%m-%d")


    def __init__(self, name, id, ConvenienceAmount, Packege, NameOfGuid ,date):
        super(Exerciser, self).__init__(name,id)
        self.NameOfGuid=NameOfGuid
        self.Purchases={date:Packege}
        self.ConvenienceAmount = ConvenienceAmount
        self.End=ReturnEndDate(date,NumOfMonth(Packege.keys()))









