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
    <title>2025 MEME MODE</title>
</head>
<body style="background: #000; color: #fff; font-family: Arial; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; text-align: center; padding: 20px;">
    <h1 style="font-size: 2.5rem; margin-bottom: 20px; color: #ff6b6b; text-shadow: 0 0 10px #ff6b6b; animation: glow 2s ease-in-out infinite alternate;">2025 MEME MODE</h1>
    <div style="width: 80%; max-width: 500px; height: 300px; background: linear-gradient(45deg, #ff6b6b, #4ecdc4); border-radius: 20px; display: flex; align-items: center; justify-content: center; font-size: 3rem; font-weight: bold; color: #fff; text-shadow: 2px 2px 4px #000; margin-bottom: 30px; animation: bounce 2s infinite; box-shadow: 0 0 30px rgba(255, 255, 255, 0.3);">Funny Reaction! 😂</div>
    <p style="max-width: 400px; font-size: 1.1rem; line-height: 1.5; opacity: 0.8; margin-top: 10px;">Мем из Pinterest: забавная реакция на 2025 год. Стиль — юмор, яркие цвета, типичная funny picture. Добавь свой текст!</p>
    <div style="margin-top: 30px; font-size: 0.8rem; color: #666;">© kersky10-coder | Inspired by Pinterest</div>
    <style>
        @keyframes glow { from { text-shadow: 0 0 10px #ff6b6b; } to { text-shadow: 0 0 20px #4ecdc4; } }
        @keyframes bounce { 0%, 20%, 50%, 80%, 100% { transform: translateY(0); } 40% { transform: translateY(-20px); } 60% { transform: translateY(-10px); } }
    </style>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

