def create_spend_chart(obj_list):
	
	withdraw_list=[]
	name_list=[]
	
	for obj in obj_list:
		name= obj.name
		name_list.append(name)
		withdraw=obj.ledger
		withdraw_amount=0
		for w in withdraw:
			amount=w["amount"]
			if(amount<0):
				withdraw_amount+=amount
			withdraw_amount=-(withdraw_amount)
		withdraw_list.append(withdraw_amount)
		
	return withdraw_list,name_list
	

class Category:
	
	def __init__(self,name):
		self.name=name
		self.ledger=[]
	
	def get_balance(self):
		balance=0
		for i in self.ledger:
			amount=i["amount"]
			balance+=amount
		return balance
		
	def check_funds(self,amount):
		balance=self.get_balance()
		if(amount<=balance):
			return True
		return False		
		
	def deposit(self,amount,description=""):
		ele={"amount": amount, "description": description}
		self.ledger.append(ele)
		
	def withdraw(self,amount,description=""):
		ele={"amount": -amount, "description": description}
		amount2=self.ledger[0]["amount"]
		if(self.check_funds(amount)):
			self.ledger.append(ele)
			return True
		return False

	def transfer(self,amount,obj):
		name=obj.name
		ele={"amount":-amount,"description":f"Transfer to {name}"}
		amount2=self.ledger[0]["amount"]
		if(self.check_funds(amount)):
			self.ledger.append(ele)
			obj.ledger.append({"amount":amount,"description":f"Transfer from {self.name}"})
			return True
		return False
		
		
	def __str__(self):
		
		title=self.name
		side_no=int((30/2)-(len(title)/2))
		left="*"*side_no
		right="*"*side_no
		
		content=""
		
		for i in self.ledger:
			des=i["description"][0:23]
			num=i["amount"]
			amu="{:.2f}".format(num)
			space=" "*(30-len(des)-len(amu))	
			text=f"{des}{space}{amu}\n"
			content+=text
		
		content+="Total: {:.2f}".format(self.get_balance())
		display=f"{left}{title}{right}\n{content}"

		return display
		
		
food = Category("Food")
entertainment =Category("Entertainment")
business =Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
 
actual = create_spend_chart([business, food, entertainment])
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

print(actual)
print("\n!!!!!!~!!!~~~~~\n")
print(expected)
print("\n!!!!!!~!!!~~~~~\n")
print(actual==expected)