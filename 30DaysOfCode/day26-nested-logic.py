
act_date = input()
exp_date = input()


def compute(act_date, exp_date):
	act_day, act_month, act_year = [int(x) for x in act_date.split(' ')]
	exp_day, exp_month, exp_year = [int(x) for x in exp_date.split(' ')]


	if act_year > exp_year:
	    return 10000
	elif act_month > exp_month:
	    if act_year < exp_year:
	        return 0
	    return 500 * (act_month - exp_month)
	elif act_day > exp_day:
	    if act_month < exp_month:
	        return 0
	    return 15 * (act_day - exp_day)
	else:
	    return 0

print(compute(act_date, exp_date))
