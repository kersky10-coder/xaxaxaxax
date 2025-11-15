<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Шаблон Pinterest</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #f5f5f5;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
        }
        .pin-card {
            width: 100%;
            max-width: 300px;
            background: #fff;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .pin-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        .image-placeholder {
            width: 100%;
            height: 400px;
            background: #eee;
            border-bottom: 1px solid #ddd;
        }
        .content {
            padding: 16px;
        }
        .title-placeholder {
            height: 20px;
            background: #ddd;
            border-radius: 4px;
            margin-bottom: 8px;
        }
        .desc-placeholder {
            height: 16px;
            background: #eee;
            border-radius: 4px;
            margin-bottom: 12px;
        }
        .desc-placeholder.short { width: 70%; }
        .footer-placeholder {
            height: 32px;
            background: #f0f0f0;
            border-radius: 50px;
            margin-top: 8px;
        }
    </style>
</head>
<body>
    <div class="pin-card">
        <div class="image-placeholder"></div>
        <div class="content">
            <div class="title-placeholder"></div>
            <div class="desc-placeholder"></div>
            <div class="desc-placeholder short"></div>
            <div class="footer-placeholder"></div>
        </div>
    </div>
</body>
</html>
