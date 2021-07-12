expected_day=int(input('enter the expected day'))
return_day=int(input('enter the return_day'))
expected_month=int(input('enter the expected_month'))
return_month=int(input('enter the return_month'))
expected_year=int(input('enter the expected_year '))
return_year=int(input('enter the return_year'))
if expected_day>=return_day:
	if expected_month>=return_month:
		if expected_year>=return_year:
			print('no charge')
		else:
			print(1000*(return_year-expected_year))
	else:
	     print(500*(return_month-expected_month))
else:
      print(15*(return_day-expected_day))