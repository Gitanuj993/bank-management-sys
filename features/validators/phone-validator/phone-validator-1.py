


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
			
