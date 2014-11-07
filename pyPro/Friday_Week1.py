class transaction():
    def __init__(me, amount, payee, memo):
        me.amount = amount
        me.payee = payee
        me.memo = memo

class Account:
    def __init__(me, name, balance):
        me.name = name
        me.balance = balance
        me.transactions = []
    def addTransation(me, transaction):
        me.transactions.append(transaction)
        me.balance += transaction.amount
    def printLedger(me):
        print ("LEDGER ...")
        for t in me.transactions:
            print t.amount, t.payee, t.memo

account = Account("checking", 000)
account.addTransation(transaction(3000, "LandLord", "Dec Rent"))
account.addTransation(transaction(3, "starbucks", "coffee"))
account.addTransation(transaction(100, "transfer", "From Simcha"))
account.printLedger()
savings_account = (Account("savings", 9999))
savings_account.addTransation(transaction(-1000, "Transfer", "To Checking"))
savings_account.printLedger()


