# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    content = [
        {
            'title': "главное сегодня",
            'description': 'Сегодня очень холодно',
            'date': '13.12.2023'
        },
        {
            'title': "вторая новость сегодня",
            'description': 'доллар стабилен',
            'date': '14.12.2023'
        },
        {
            'title': "новости спорта",
            'description': 'футбол уже не играю, слишком много снега',
            'date': '15.12.2023'
        }
    ]

    return render_template('task7.html', context=content)



if __name__ == '__main__':
    app.run(debug=True)