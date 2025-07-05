from flask import Flask, send_file, jsonify
from flask_cors import CORS  # Asegúrate de importar CORS
from services.captcha_service import CaptchaService
import io

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir solicitudes desde cualquier origen

@app.route('/generate-captcha', methods=['GET'])
def generate_captcha():
    """Genera un captcha y lo devuelve como imagen."""
    captcha_text, captcha_image = CaptchaService.generate_captcha()

    # Guardar la imagen en memoria
    img_io = io.BytesIO()

    # En lugar de pasar captcha_text como argumento, simplemente escribe la imagen
    captcha_image.save(img_io, 'PNG')  # Usa el método `save()` para guardar la imagen en img_io
    img_io.seek(0)  # Regresa al inicio del flujo de bytes para enviarlo como respuesta

    # Enviar la imagen como respuesta HTTP
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='captcha.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
