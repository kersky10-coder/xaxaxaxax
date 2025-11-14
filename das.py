from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.')

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EGOR GALLERY</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #000;
            color: #fff;
            font-family: 'Arial', sans-serif;
            padding: 20px;
            text-align: center;
        }
        h1 {
            margin: 20px 0;
            font-size: 2.5rem;
            text-shadow: 0 0 10px gold;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin: 30px 0;
        }
        img {
            max-width: 100%;
            max-height: 70vh;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.7);
            transition: all 0.3s;
            cursor: pointer;
        }
        img:hover {
            transform: scale(1.05);
            box-shadow: 0 0 50px gold;
        }
        .footer {
            margin-top: 40px;
            font-size: 0.9rem;
            color: #aaa;
        }
    </style>
</head>
<body>
    <h1>EGOR GALLERY</h1>
    <div class="gallery">
        <img src="/download.jfif" alt="EGOR 1" onerror="this.style.display='none'">
        <img src="/photo_2025-11-15_00-06-20.jpg" alt="EGOR 2" onerror="this.style.display='none'">
    </div>
    <div class="footer">© 2025 · kersky10-coder · xaxaxaxax.onrender.com</div>
</body>
</html>
    '''

# Чтобы Flask отдавал файлы из корня репозитория
@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
