class case:
	upper=[]
	lower=[]
	def __init__(self,word):
		if word.upper():
			case.upper.append(word)
		else:
			case.lower.append(word)
w1=case("DIVYAUUU")
w2=case("divyauuu")
print(case.upper)
print(case.lower)
print(w2.upper)
