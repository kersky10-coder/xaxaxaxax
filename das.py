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
    <title>Яша и анекдот</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            height: 107vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
        }
        .container {
            background: rgba(0,0,0,0.3);
            padding: 30px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 600px;
        }
        h1 { font-size: 2.5rem; margin-bottom: 20px; }
        img {
            width: 100%;
            max-width: 500px;
            border-radius: 15px;
            margin: 20px 0;
            box-shadow: 0 5px 20px rgba(0,0,0,0.4);
        }
        p { 
            font-size: 1.2rem; 
            margin-top: 20px; 
            line-height: 1.7; 
            font-weight: 500;
        }
        em { color: #ffd700; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Весёлый Яша</h1>
        <img src="https://i.imgur.com/9vZfPqL.png" alt="Яша с анекдотом">
        <p>
            — Доктор, у меня с памятью плохо!<br>
            — А когда это началось?<br>
            <em>— Что началось?</em>
        </p>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
