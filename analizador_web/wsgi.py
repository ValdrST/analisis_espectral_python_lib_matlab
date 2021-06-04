#!/usr/bin/env python
from .main import application
from waitress import serve
import logging
#logging.basicConfig(filename='/var/analizador_web.log', level=logging.DEBUG)
def wsgi():
    logging.info('Iniciado WSGI')
    serve(application, port=3000, unix_socket_perms='666', ident="analizador_web",threads=32)
