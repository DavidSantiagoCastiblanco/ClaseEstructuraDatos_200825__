import re

# Ejercicio para extraer direcciones IPv4

regularEx_1 = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# Indicamos que cada grupo tiene entre 1 y 3 dígitos. Además, cada uno está separado por un punto.

texto = """ El servidor de la base de datos se configuró con la IP 192.168.1.100, 
mientras que el servidor web usa 8.8.8.8 para las pruebas externas.  
Un switch viejo aún responde en 10.1.0.45, aunque ya debería estar fuera de uso.  
Alguien registró 256.300.12.999, que no corresponde a una IP válida pero quedó guardado en el log.  
El balanceador de carga opera con la dirección 172.20.0.5 para la red interna.  
Finalmente, un servicio remoto responde desde 201.45.123.77."""  

resultado = re.findall(regularEx_1, texto)
print(resultado)
