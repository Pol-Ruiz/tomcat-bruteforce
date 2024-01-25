# Descripción del script de fuerza bruta para el inicio de sesión de Apache Tomcat
El script apache-tomcat-login-bruteforce.py es una herramienta de fuerza bruta diseñada para probar la seguridad del inicio de sesión de Apache Tomcat. Se ejecuta en Python 3 y utiliza una variedad de opciones para personalizar el ataque.

# Uso
```python3 apache-tomcat-login-bruteforce.py [-h] [-H HOST] [-P {http,https}] [-m MANAGER] [-p PORT]```

# Opciones
```-h, --help```: Muestra el mensaje de ayuda y sale.

```-H HOST, --host HOST```: Especifica el nombre de host de Apache Tomcat.

```-P {http,https}, --proto {http,https}```: Permite seleccionar el protocolo a utilizar, ya sea HTTP o HTTPS.

```-m MANAGER, --manager MANAGER```: Define la ruta al Host Manager. Por defecto, es /manager/html.

```-p PORT, --port PORT```: Permite especificar el puerto. Por defecto, es 8080.


Por favor, úsalo de manera responsable y solo en sistemas para los que tienes permiso para hacerlo. La fuerza bruta puede ser ilegal en tu jurisdicción. Este script se proporciona solo con fines educativos y de prueba. No me hago responsable de su uso indebido.
