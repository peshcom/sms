#! /usr/bin/env python3
import sms

api = 'YOU_API_KEY'
phone = 'YOU_PHONE'

if __name__ == '__main__':
	__sms = sms.sms_class(api, phone)
	print("Ваш текущий баланс: ", __sms.get_balance())
	print("Кол-во бесплатных смс на сегодня: ", __sms.free_count())

	text = ''
	for i in input("Введите сообщение: "):
		if i == ' ':
			text = text + '+'
		else:
			text = text + i
	print(text)


	print("Отправка стоит: ", __sms.check_price(text))
	print("Отправка сообщения: ", __sms.send_sms(text))
	print("Ваш текущий баланс: ", __sms.get_balance())
	print("Кол-во бесплатных смс на сегодня: ", __sms.free_count())
