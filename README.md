# testpyopenssl

Test Pyopenssl

### Clonar proyecto:
git clone git@github.com:oortega/testpyopenssl.git

### Crear Entorno:
mkvirtualenv testpyopenssl

### Entrar en el entorno
workon testpyopenssl

### Instalar Bibliotecas
pip install requests==2.22.0

pip install requests[security]==2.22.0

### Instalar Requirements
pip install -r requirements.txt

### Solucion

Se soluciono usando OpenSSL con una version actualizada de cryptography, tambien debe estar requests en la version 2.22.0

Se instalo de la siguiente manera:

pip uninstall cryptography

pip install cryptography==2.8

pip install stripe

pip install requests==2.22.0