"""
go_for_gold.py
=====
Translate an athlete's finishing placement (1st, 2nd and 3rd) into its Olympic medal value: 1 for gold, 2 for silver, 3 for bronze and anything else means no medal.  Do this by asking for user input.  For example:

What number should I translate into a medal?
>1
gold

What number should I translate into a medal?
>3
bronze

What number should I translate into a medal?
>23
no medal for you!

"""
medal = int(raw_input('what number should I translate into? \n'))
if (medal) < 1 or int(medal) > 3:
	print('not valid')
if (medal)==1:
	print('gold')

elif (medal)==2:
	print('silver')

elif (medal)==3:
	print('bronze')
else:
	print('no medal for you')