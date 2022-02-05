# Третья задача
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """Человечество вырастает из детства.</br></br>Человечеству мала одна планета.</br></br>
    Мы сделаем обитаемыми безжизненные пока планеты.</br></br>И начнем с Марса!</br></br>Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс</h1>
                    <img src="{url_for('static', filename='data/mars.png')}" alt="здесь должна была быть картинка, но не нашлась"></br>
                    Вот она какая, красная планета!
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
