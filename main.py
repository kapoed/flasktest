from flask import Flask, url_for, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', list=list,
                           list_prof=['Строитель', 'Инженер по терраформированию', 'Метеоролог', 'Оператор марсохода',
                                      'Инженер жизнеобеспечения', 'Астрогеолог', 'Экзобиолог',
                                      'Специалист по радиационной защите'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    return render_template('distribution.html',
                           crew=['Владимир Ленин', 'Брэд Питт', 'Жак Фреско', 'Артём Дзюба', 'Дуэйн Джонсон',
                                 'Павел Пламенев'])

@app.route('/table/<gender>/<int:age>')
def table(gender, age):
    return render_template('table.html', gender=gender, age=age)


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
                        <title>Колонизация</title>
                    </head>
                    <body>
                        <h1 class=r>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" width=600>    
                        <div class="p-3 mb-2 bg-secondary text-black">Человечество вырастает из детства.</div>
                        <div class="p-3 mb-2 bg-success text-green">Человечеству мала одна планета.</div>
                        <div class="p-3 mb-2 bg-info text-cyan">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="p-3 mb-2 bg-warning text-yellow">И начнем с Марса!</div>
                        <div class="p-3 mb-2 bg-danger text-red">Присоединяйся!</div>
                    </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
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
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1 align=center>Анкета претендента</h1>
                                <h2 align=center>на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="text" placeholder="Введите фамилию" name="second_name">
                                        <input type="text" class="form-control" id="text" placeholder="Введите имя" name="first_name">
                                        </br>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее неполное</option>
                                              <option>Среднее полное</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                         <label class="form-check-label" for="acceptRules">Какие у вас есть профессии?</label>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="profession1">
                                            <label class="form-check-label" for="acceptRules">Строитель</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="profession2">
                                            <label class="form-check-label" for="acceptRules">Инженер по терраформированию</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="profession3">
                                            <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="profession4">
                                            <label class="form-check-label" for="acceptRules">Оператор марсохода</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="profession5">
                                            <label class="form-check-label" for="acceptRules">Инженер жизнеобеспечения</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="profession6">
                                            <label class="form-check-label" for="acceptRules">Астрогеолог</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="profession7">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="profession8">
                                            <label class="form-check-label" for="acceptRules">Специалист по радиационной защите</label>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['second_name'])
        print(request.form['first_name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['profession1'])
        print(request.form['profession2'])
        print(request.form['profession3'])
        print(request.form['profession4'])
        print(request.form['profession5'])
        print(request.form['profession6'])
        print(request.form['profession7'])
        print(request.form['profession8'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                    </head>
                    <body>
                        <h1>Моё предложение: {planet_name}</h1> 
                        <h3>Эта планета близка к земле;</h3> 
                        <div class="p-3 mb-2 bg-secondary text-black">Она круглая</div>
                        <div class="p-3 mb-2 bg-success text-green">На ней есть {planet_name}иане</div>
                        <div class="p-3 mb-2 bg-info text-cyan">На неё светит солнце</div>
                        <div class="p-3 mb-2 bg-warning text-yellow">Наконец, она просто красива!</div>
                    </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                    </head>
                    <body>
                        <h1>Результаты отбора</h1> 
                        <h3>Претендента {nickname} на участие в миссии:</h3> 
                        <div class="p-3 mb-2 bg-success text-white">Поздравляем ваш рейтинг после {level} этапа отбора</div>
                        <div class="p-3 mb-2 bg-success text-white">cоставляет {rating}!</div>
                        <div class="p-3 mb-2 bg-info text-cyan">Желаем удачи!</div>
                    </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
