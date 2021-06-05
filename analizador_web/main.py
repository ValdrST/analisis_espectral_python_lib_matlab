#!/usr/bin/env python
#from .shared.infraestructura import Console
from .core import Server

application = Server("analizador_web").app
def main():
  application.run(debug=True)
