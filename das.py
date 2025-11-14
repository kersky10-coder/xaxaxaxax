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
    <title>EGOR</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #000;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 10px;
        }
        img {
            max-width: 100%;
            max-height: 95vh;
            border-radius: 20px;
            box-shadow: 0 0 40px rgba(255, 215, 0, 0.6);
            transition: transform 0.3s;
        }
        img:hover {
            transform: scale(1.02);
        }
    </style>
</head>
<body>
    <img src="https://i.imgur.com/8QjL5vP.png" alt="EGOR">
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
