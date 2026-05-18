from pathlib import Path
import csv
#importing file 
path = Path("database/data.csv")
if not  path.exists() :
    with open(path,"w",newline="") as file :
        writer = csv.writer(file(
        writer.writerow(["Name","Phone_no","Address","Account_no"])




class Bank() :
	pass
	#def __init__(self) :
		
class User(Bank) : 
	def __init__(self) :
		pass
                		

class RegisterUser(User) :
	def __init__(self) :
		#user_data(self)
		self.user_data()
		
	def user_full_name(self) :
		while True :
			try :
				self.name = input(" Enter Your Full  Name  : ").upper()							
				for ch in self.name :
					if ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ " :
						raise Exception(" name should only contain alphabets and space")
			except Exception as e :
				print(" Enter a valid full name")
			else :
				break
		
	def user_phone_no(self) :
		
		while True :
			try :
				# phone -no input from the user
				self.phone_no = input("Enter your phone_no : ")
				# check for valid phone number 
				
				for num in self.phone_no :
					if num  not in "0123456789+ " :
						raise Exception("Enter valid phone number")
					if '+' in self.phone_no :
						if self.phone_no[0] != '+' :
							raise Exception(" '+' symbol only come before numbers ")
								
				
			except Exception as e :
				print(e)
				
			else :
				break
	
	def user_data(self) :
		# taking valid user full name
		self.user_full_name()				
		# valid phone number
		self.user_phone_no()	
			
			
	def display_user_data(self) :
		print("name is : " ,  self.name)
		print("phone no is :  ",self.phone_no)
		
		
		
		
		
if __name__ == '__main__' :
		s = RegisterUser()
		s.display_user_data()
		
		
	
