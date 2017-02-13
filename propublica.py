import appengine_config
import mechanize
import logging
from secrets import billing

def donate(donation_amount, tid):

	logging.info('Donating ${} for tid {}'.format(donation_amount, tid))
	
	donation_amount = str(donation_amount)

	br = mechanize.Browser(factory=mechanize.RobustFactory())
	br.addheaders = [('User-agent', '	Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36')]
	br.set_handle_robots(False)
	br.open('https://www.propublica.org/donate/')
	br.select_form('payment_form')

	prices = br.find_control('UnitPrice1')
	custom_price = mechanize.Item(prices, {'contents': donation_amount, 'value': donation_amount})
	custom_price.selected = True

	br.form['c_amount'] = donation_amount

	br.form['BillingFirstName'] = billing['first']
	br.form['BillingLastName'] = billing['last']

	if billing['email'].endswith('+{}@gmail.com'):
		br.form['BillingEmail'] = billing['email'].format(tid)
	else:
		br.form['BillingEmail'] = billing['email'].format(tid)

	br.form['CardNumber'] = billing['cc']
	br.form['ExpirationMonth'] = [billing['exp_mo']]
	br.form['ExpirationYear'] = [billing['exp_yr']]
	br.form['Cvv2'] = billing['cvv']

	br.form['BillingAddress1'] = billing['street']
	br.form['BillingCity'] = billing['city']
	br.form['BillingStateProvince'] = [billing['state']]
	br.form['BillingPostalCode'] = billing['zip']
	br.form['BillingCountryCode'] = [billing['country']]

	response = br.submit()
	if 'Thank You.' in response.read():
		logging.info('Donation success: ${} for tid {}'.format(donation_amount, tid))
		return True
	else:
		logging.warning(response.read())
		logging.warning('Donation failed: ${} for tid {}'.format(donation_amount, tid))
		return False



