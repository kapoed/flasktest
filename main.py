from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def indexx():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "</br>".join(["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                         "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"])


@app.route('/image_mars')
def image_mars():
    return "</br>".join(["<h1>Жди нас, Марс!</h1>",
                         f'''<img src="{url_for('static', filename='img/mars.jpg')}">''',
                         "Вот она какая, красная планета"])


@app.route('/im')
def im():
    return f'''<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}">    
                        <div>Вот она какая, красная планета</div>
                    </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
