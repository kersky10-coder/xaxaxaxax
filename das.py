from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2025 MEME</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            font-family: 'Arial', sans-serif;
            color: #fff;
            text-align: center;
            padding: 20px;
        }
        .meme-container {
            position: relative;
            width: 80%;
            max-width: 500px;
            margin-bottom: 30px;
        }
        .meme-bg {
            width: 100%;
            height: auto;
            border-radius: 20px;
            box-shadow: 0 0 30px rgba(255, 255, 255, 0.3);
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4); /* Градиент вместо фото для стиля пина */
        }
        .meme-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 2rem;
            font-weight: bold;
            color: #fff;
            text-shadow: 2px 2px 4px #000;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translate(-50%, -50%) translateY(0); }
            40% { transform: translate(-50%, -50%) translateY(-10px); }
            60% { transform: translate(-50%, -50%) translateY(-5px); }
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .description {
            max-width: 400px;
            font-size: 1.1rem;
            line-height: 1.5;
            opacity: 0.8;
        }
        .footer {
            margin-top: 30px;
            font-size: 0.8rem;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>2025 MEME MODE</h1>
    <div class="meme-container">
        <div class="meme-bg"></div>
        <div class="meme-text">Funny Reaction! 😂</div>
    </div>
    <p class="description">Мем из Pinterest: забавная реакция на 2025 год. Стиль — юмор, яркие цвета, типичная funny picture. Добавь свой текст!</p>
    <div class="footer">© kersky10-coder | Inspired by Pinterest</div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
