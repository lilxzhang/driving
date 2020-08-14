# driving
country = input('where are you from?: ')
age = input('how old are you?: ')
age = int(age)
if country == 'canada':
	if age >= 16:
		print('you may get a drivers licenis')
	else: 
		print('sorry man not old enough')
if country == 'china':
	print('sorry for you buudy no driving for you')
if country == 'tai wan': 
	if age >= 18:
		print('you can get a drivers licenis')
	else:
		print('too young BOI')