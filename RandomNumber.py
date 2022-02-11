import random
def GuessTheNumber():
	a=random.randint(0,100)
	count=0
	print(a)
	prev=-1
	prev_diff=300
	while prev!=a:
		curr=int(input())
		count+=1
		curr_diff=abs(curr-a)
		if curr<0 or curr>100:
			print ("Out of Bounds")
		else:
			if count==1:
				if curr_diff<=10: 
					print("WARM")
				else:
					print("COLD")
			else:
				if curr_diff>prev_diff:
					print("COLDER")
				elif curr_diff==0:
					print("Hurrah You've Guessed it right and you've taken {} chances".format(count))
					return
				else:
					print("WARMER")
			prev=curr
			prev_diff=curr_diff		

GuessTheNumber()
