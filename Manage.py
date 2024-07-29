import datetime
class Manage:
    def __init__(self):
        purchases = {'month': 250, 'halfYear': 600, 'year': 1000}
        Exercisers = []
        guid1 = Guid('Yoshi', '214901134', 5, 2500)
        guid2 = Guid('Yoni', '032784738', 2, 2800)
        guid3 = Guid('Shim', '032784569', 15, 1500)
        GuidsList = [guid1, guid2, guid3]

    def GetNameOfGuid(self):
        for guid in GuidsList:
            if guid.NumOfExercisers < 10:
                guid.NumOfExercisers += 1
                return guid.GetName()

    def Payment(self, cost):
        print(f"you need to pay {cost} ILS")
        payments = input("Enter a number of payments")
        try:
            payments = int(payments)
            OnefPayment = lambda cost, payments: cost / payments
            creditCard = input("Enter credit information")
            if creditCard.isnumeric():
                AccountManager = open(file='AccountManagement.txt', mode='a', encording='utf-8')
                AccountManager.write(f"sum : {OnefPayment} from: {creditCard} payments:{payments}")
                print(f"Credit card number {creditCard} charged in the amount of {OnefPayment} ILS")
                AccountManager.close()
                return True
            else:
                return False
        except ValueError:
            print("error")
            return False

    def UserExist(self, id):
        if Exercisers == None:
            return None
        for item in Exercisers:
            if item.id == id:
                return item
        return None

    def Join(self):
        name = input("enter name")
        id = input("enter id")
        print("the package are: ")
        print(dict(purchases.items()))
        package = input("enter package")
        try:
            cost = purchases.get(package)
        except:
            print(f"error ,{e}")
        dictPackage = {package: cost}
        NameOfGuid = GetNameOfGuid()
        flag = Payment(cost)
        if flag:
            user = UserExist(id)
            if user != None:
                print(f"Your current packege end in {user.End}")
                user.Purchases = {date: dictPackage}
            else:
                exerciser = Exerciser(name, id, cost, dict(dictPackage.items()), NameOfGuid, datetime.datetime.now())
                Exercisers.append(exerciser)
                print("You have successfully joined")
        else:
            print("Unfortunately, one or more of the details you entered is incorrect")
