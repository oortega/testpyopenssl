import mercadopago
import ast
import json
telefono = "9981875356"
nombre = "Jose Ramiro"
email = "jose-ramiro-10@outlook.com"
moneda = "MXN"
id_cliente = "" # Poner llaves
secret_cliente = # Poner llaves
mp = mercadopago.MP(id_cliente, secret_cliente)
mp.sandbox_mode(True)
url_webhook = "" # Poner webhook 
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