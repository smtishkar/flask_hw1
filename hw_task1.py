# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
#  и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cloths/')
def cloths():
    return render_template('cloths.html')


@app.route('/boots/')
def boots():
    return render_template('boots.html')


@app.route('/hats/')
def hats():
    return render_template('hats.html')


if __name__ == "__main__":
    app.run(debug=True)
