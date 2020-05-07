#! /usr/bin/env python3
import requests
import json

class sms_class():
	api = ""
	phone = ""
	def __init__(self, api, phone):
		self.api = api
		self.phone = phone

	def check_price(self, msg):
		# Проверяет стоимость отправки сообщения
		url = 'https://sms.ru/sms/cost?api_id='+str(self.api)+'&to='+str(self.phone)+'&msg='+msg+'&json=1'
		responce = requests.get(url).text
		cost = json.loads(responce)['total_cost']
		return float(cost)

	def get_balance(self):
		# Вернет баланс на текущем аккаунте
		url = 'https://sms.ru/my/balance?api_id='+str(self.api)+'&json=1'
		responce = requests.get(url).text
		balance = json.loads(responce)['balance']
		return float(balance)

	def free_count(self):
		# Вернет кол-во оставшихся бесплатных смс на сегодняшний день
		url = 'https://sms.ru/my/free?api_id='+str(self.api)+'&json=1'
		responce = requests.get(url).text
		temp = json.loads(responce)
		if str(temp['used_today']) == 'None':
			temp['used_today'] = 0
		return int(int(temp['total_free']) - int(temp['used_today']))

	def send_sms(self, msg, no_price=0):
		url = 'https://sms.ru/sms/send?api_id='+str(self.api)+'&to='+str(self.phone)+'&msg='+msg+'&json=1'
		
		# Если требуется отправить сообщение в любом случае
		if no_price:
			text = requests.get(url).text
			return json.loads(text)['sms'][self.phone]['status']

		# Сначала смотрим на стоимость
		if self.check_price(msg) == 0:
			text = requests.get(url).text
			return json.loads(text)['sms'][self.phone]['status']
		return "Error! Стоимость отправки не нулевая!"