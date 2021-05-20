class Category:

    def __init__(self, category, amount):
      self.categroy = category 
      self.amount = amount

    #methods
    def deposit(self, amount):
      self.amount += amount
      print ("You have successfully deposited {} in {} category".format(amount, self.categroy))


    def withdraw(self, amount):
      if self.check_balance(amount):
        self.amount -= amount
      else:
        return "Transaction Failed"
    
    
    def balance(self):
     return"This is the current balance: {}".format(self.amount)


    def check_balance(self,amount):
      #this should return an boolean to check if amount is less than or greater self.amount 
      if self.amount < amount:
        print("amount is greater then {}".format(self.amount))
      else:
         print("amount is less then {}".format(self.amount))

      return True 


    def tranfer(self, amount):
      if not self.check_balance(amount):
       return "Not successful"

      self.amount -= amount
      Category.amount += amount
      return "Transfer successful"
     
instance = Category("Food", 500)
instance1 = Category("Car",400)

instance.deposit(600)
print(instance.balance())
instance.transfer(400, instance1)

