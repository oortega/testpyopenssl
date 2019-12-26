import mercadopago
import ast
import json
telefono = "9981875356"
nombre = "Luis Abraham Salgado Ascencio"
email = "luissalgado9@hotmail.com"
moneda = "MXN"
id_cliente = "1694458604555838"
secret_cliente = "vAWNlGYywaLoDzyVIU0kkggv2sp1PeWj"
mp = mercadopago.MP(id_cliente, secret_cliente)
mp.sandbox_mode(True)
url_webhook = "https://3c6b0b1e.ngrok.io/webhook/mercadopago/luissolutions/"
preference = {
    "items":[
        {
            "title": "Pago de prueba open ssl",
            "quantity": 1,
            "currency_id": moneda,
            "unit_price": 10
        }
    ],
    "payer": [
        {
            "name": nombre,
            "email": email
        }
    ],
    "external_reference": "Factura de prueba open ssl",
    "notification_url": url_webhook
}
try:
    preferenceResult = mp.create_preference(preference)
except Exception as mensaje_error:
    error = ast.literal_eval(mensaje_error.value)
    mostrar_error = error['response']['message']
    print mostrar_error

print preferenceResult["response"]["id"]

try: 
    preferenceResult = mp.get_preference(preferenceResult["response"]["id"])
    preference_json = json.dumps(preferenceResult)
except Exception as error:
    error = ast.literal_eval(error.value)
    error_mercadopago = error.get('response').get('message')
    print error_mercadopago