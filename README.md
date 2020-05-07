
Класс для работы с API сайта sms.ru
Позволяет отправлять SMS-сообщения с компьютера.

Настройки находятся в 4 и 5 строке основного файла (main.py)
- main.py // пример использования
- sms.py  // Описание класса

Usage:
```
__sms = sms.sms_class(api, phone)
__sms.send_sms(text)
```

requirements:
- requests
- json

Eng:
Class for working with the site API sms.ru
Allows you to send SMS messages from your computer.