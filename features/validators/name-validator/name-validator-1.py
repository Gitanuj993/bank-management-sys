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
