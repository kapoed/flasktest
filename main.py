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

@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" width=600>    
                        <div class="p-3 mb-2 bg-secondary text-black">Человечество вырастает из детства.</div>
                        <div class="p-3 mb-2 bg-success text-green">Человечеству мала одна планета.</div>
                        <div class="p-3 mb-2 bg-info text-cyan">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="p-3 mb-2 bg-warning text-yellow">И начнем с Марса!</div>
                        <div class="p-3 mb-2 bg-danger text-red">Присоединяйся!</div>
                    </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
