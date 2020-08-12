weight = input ('請輸入體重')
weight = int(weight)
height = input ('請輸入身高')
height = float (height)
bmi = weight/ (height * height)
print (bmi)

if bmi < 18:
	print ('過瘦')
elif bmi >= 18 and bmi < 24:
	print ('正常')
elif bmi > 24:
	print ('過重')