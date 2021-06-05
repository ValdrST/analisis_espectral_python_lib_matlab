from flask import Flask, request, Blueprint, jsonify, render_template
import werkzeug.utils
import base64
import os
from .Graficador import Graficador
import wave, struct


import logging
logging.basicConfig(filename='/var/analizador_web.log', level=logging.DEBUG)
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'uploads')
server_analizador = Blueprint('app', __name__, url_prefix='/')
ALLOWED_EXTENSIONS = set(['wav', 'txt'])

def is_file_allowed(filename):
  extension = os.path.splitext(filename)[1]
  if not extension:
    return False
  return extension[1:].lower() in ALLOWED_EXTENSIONS
  
def is_wav(filename):
  extension = os.path.splitext(filename)[1]
  if not extension:
    return False
  return extension[1:].lower() in set(['wav'])

def wave_to_txt(filename):
  wavefile = wave.open(filename, 'r')
  length = wavefile.getnframes()
  data = ""
  for i in range(0, length):
    wavedata = wavefile.readframes(1)
    data += str(struct.unpack("<h", wavedata)[0]/65535)
  with open(os.path.join(UPLOAD_FOLDER,"data.txt"), "w") as f:
    f.write(data)
  return os.path.join(UPLOAD_FOLDER,"data.txt")

def ensure_dir_exists(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

class Server():
  def __init__(self, name, *args, **kwargs):
    self.app = Flask(name)
    self.app.register_blueprint(server_analizador)
  
  @server_analizador.route('/')
  def index():
    logging.info("Pagina inicial")
    return render_template("index.html")

  @server_analizador.route('/obtener_datos',methods=['POST'])
  def obtener_datos():
    g = Graficador([], out_file=os.path.join(UPLOAD_FOLDER, "grafica.png"))
    response = {}
    uploaded_file = request.files['file']
    filename = werkzeug.utils.secure_filename(uploaded_file.filename)
    ensure_dir_exists(UPLOAD_FOLDER)
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    logging.info("Creando grafica con datos de "+save_path)
    uploaded_file.save(save_path)
    if is_wav(save_path):
      txt_path = wave_to_txt(save_path)
    else:
      txt_path = save_path
    g.get_data(txt_path)
    g.crear_grafica()
    with open(os.path.join(UPLOAD_FOLDER, "grafica.png"), "rb") as img_file:
      imagen = base64.b64encode(img_file.read())
    response['data'] = imagen.decode('utf-8')
    logging.info("Grafica creada")
    return jsonify(response)
