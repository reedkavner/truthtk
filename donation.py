import appengine_config
import mechanize

def donate():
	br = mechanize.Browser()
	br.open('https://www.propublica.org/donate/')
	br.select_form('payment_form')

	br.form['UnitPrice1'] = ['']
	br.form['c_amount'] = '5'

	br.form['BillingFirstName'] = 'A'
	br.form['BillingFirstName'] = 'B'

	response = br.submit()

	return response.read()