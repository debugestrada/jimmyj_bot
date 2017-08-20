import requests
from bs4 import BeautifulSoup as bs
import random

#Worst bot i've ever created. 

session = requests.session()

def get_sizes_in_stock():
	global session
	endpoint = 'http://www.jimmyjazz.com/mens/footwear/nike-pocketknife-dm-sneaker/898033-001?color=Black'
	response = session.get(endpoint)

	soup = bs(response.text, 'html.parser')
	div = soup.find("div", {"class": "box_wrapper"})
	all_sizes = div.find_all("a")
	print ('Checking for sizes in stock...')

	sizes_instock = []
	for size in all_sizes:
		if "piunavailable" not in size["class"]:
			size_id = size['id']
			sizes_instock.append(size_id.split("_")[1])

	return sizes_instock

def add_to_cart():
	global session
	sizes_instock = get_sizes_in_stock()
	size_chosen = random.choice(sizes_instock)
	endpoint = 'http://www.jimmyjazz.com/cart-request/cart/add/%s/1'%(size_chosen)
	print ('Adding desired size to cart...')
	response = session.get(endpoint)
	
	return '"success":1' in response.text


def checkout():
	global session
	endpoint0 = 'https://www.jimmyjazz.com/cart/checkout'
	response0 = session.get(endpoint0)
	soup = bs(response0.text, 'html.parser')
	
	inputs = soup.find_all('input',{'name':'form_build_id'})
	form_build_id = inputs[1]["value"]

	endpoint1 = 'https://www.jimmyjazz.com/cart/checkout'
  
#Don't do this....Never hard code your info lol
	
  payload1 = {
		"billing_email":" ",
		"billing_email_confirm":" ",
		"billing_phone":" ",
		"email_opt_in":"1",
		"shipping_first_name":" ",
		"shipping_last_name":" ",
		"shipping_address1":" ",
		"shipping_address2":" ",
		"shipping_city":" ",
		"shipping_state":" ",
		"shipping_zip":" ",
		"shipping_method":"0",
		"signature_required":"1",
		"billing_same_as_shipping":"1",
		"billing_first_name":" ",
		"billing_last_name":" ",
		"billing_country":"US",
		"billing_address1":" ",
		"billing_address2":" ",
		"billing_city":" ",
		"billing_state":" ",
		"billing_zip":" ",
		"cc_type":"Visa",
		"cc_number":" ",
		"cc_exp_month":" ",
		"cc_exp_year":" ",
		"cc_cvv":" ",
		"gc_num":" ",
		"form_build_id": form_build_id,
		"form_id":"cart_checkout_form",
	}
  
	print ('Attempting to checkout...')
	response1 = session.post(endpoint1, data=payload1)

if __name__ == '__main__':
	add_to_cart()
	checkout()
	
