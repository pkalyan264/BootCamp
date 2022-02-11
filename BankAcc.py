class BankAccount:
	def __init__(self,owner,bal=0):
		self.owner=owner
		if bal>=0:
			self.bal=bal
		else:
			# print ("Enter valid Balance to open the account")
			self.bal=0
		# print("Welcome to ABC Bank Mr/Ms.{}. Your current account balance is INR {}/-".format(self.owner,self.bal))

	def deposit(self,amount):
		if amount<=0:
			return False
			# return "Mr/Ms.{}, Please enter a valid amount to deposit. {} is not a valid amount ".format(self.owner,amount)
		else:
			self.bal+=amount
			# return "Thank You Mr/Ms.{}. Amount deposit successful and your current account balance is {}".format(self.owner,self.bal)
	def withdrawl(self,amount):
		if self.bal<amount:
			return False
			# return "Mr/Ms.{},Insufficient funds in the account .Your current account balance is {}".format(self.owner,self.bal)
		else:
			if amount>-0:
				self.bal-=amount
			else:
				return False
			# return "Thank You Mr/Ms.{}. Amount withdrawl successful and your current account balance is {}".format(self.owner,self.bal)
if(__name__=='__main__'):
	BankAccount("Kiran")
	amit=BankAccount("Amit")
	bacchan =BankAccount("Bacchan",500)
	bacchan.withdrawl(600)
	amit.withdrawl(200)
	amit.deposit(150)
	amit.withdrawl(200)
	amit.deposit(-10)