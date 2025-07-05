from flask import Flask, send_file, jsonify
from flask_cors import CORS
from services.captcha_service import CaptchaService
import io
from PIL import Image

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/generate-captcha', methods=['GET'])
def generate_captcha():
    """Genera un captcha y lo devuelve como imagen."""
    captcha_text, captcha_image = CaptchaService.generate_captcha()
    
    # Crear un flujo de bytes para almacenar la imagen generada
    img_io = io.BytesIO()

    # Usar PIL para guardar la imagen en el flujo de bytes
    captcha_image = Image.open(captcha_image)  # Abrir la imagen generada como objeto PIL
    captcha_image.save(img_io, 'PNG')  # Guardar la imagen en img_io como PNG
    img_io.seek(0)  # Mover el puntero al principio del flujo

    # Enviar la imagen como respuesta HTTP
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='captcha.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
