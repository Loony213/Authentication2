from flask import Flask, send_file, jsonify
from flask_cors import CORS
from services.captcha_service import CaptchaService
import io

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir solicitudes desde cualquier origen

@app.route('/generate-captcha', methods=['GET'])
def generate_captcha():
    """Genera un captcha y lo devuelve como imagen."""
    captcha_text, captcha_image = CaptchaService.generate_captcha()
    
    # Crear un flujo de bytes para almacenar la imagen generada
    img_io = io.BytesIO()

    # En lugar de usar .save(), usamos .write() para escribir la imagen en img_io
    captcha_image.write(img_io)  # Escribir directamente en el flujo de bytes
    img_io.seek(0)  # Regresar al principio del flujo de bytes

    # Enviar la imagen como respuesta HTTP
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='captcha.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
