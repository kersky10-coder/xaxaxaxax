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
    <title>EGOR 2025</title>
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
            overflow: hidden;
        }
        .icon-container {
            position: relative;
            width: 200px;
            height: 200px;
            margin-bottom: 30px;
        }
        .icon {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: conic-gradient(from 0deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3, #ff6b6b);
            animation: rotate 4s linear infinite, pulse 2s ease-in-out infinite alternate;
            box-shadow: 0 0 50px rgba(255, 107, 107, 0.5);
        }
        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        @keyframes pulse {
            0% { transform: scale(1); box-shadow: 0 0 20px rgba(255, 107, 107, 0.3); }
            100% { transform: scale(1.1); box-shadow: 0 0 60px rgba(78, 205, 196, 0.6); }
        }
        h1 {
            font-size: 3rem;
            text-align: center;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: glow 2s ease-in-out infinite alternate;
        }
        @keyframes glow {
            from { filter: drop-shadow(0 0 10px #ff6b6b); }
            to { filter: drop-shadow(0 0 20px #4ecdc4); }
        }
        .footer {
            position: absolute;
            bottom: 20px;
            font-size: 0.8rem;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="icon-container">
        <div class="icon"></div>
    </div>
    <h1>EGOR 2025</h1>
    <div class="footer">© kersky10-coder</div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
