from flask import Flask, abort, render_template
from utils import number_of_leap_years
from datetime import datetime, timedelta, date, tzinfo

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/<date_of_birth>/')
def life_info_page(date_of_birth):

    try:
        date_of_birth = date.fromisoformat(date_of_birth)
    except ValueError:
        return abort(404)

    today = date.today()
    life_info = {'date_of_birth': date_of_birth}
    if today.day == date_of_birth.day and today.month == date_of_birth.month:
        life_info['today_is_birthday'] = True
        print('yes')
    else:
        life_info['today_is_birthday'] = False

    lived = today - date_of_birth
    life_info['lived_days'] = lived.days

    ages = (lived.days - number_of_leap_years(date_of_birth)) // 365
    life_info['ages'] = ages

    lived_percentage = round(lived / timedelta(days=365*78) * 100, 2)
    life_info['lived_percentage'] = lived_percentage

    left = timedelta(days=365*78) - lived
    life_info['left_days'] = left.days

    next_birthday_date = date(date_of_birth.year + ages + 1, date_of_birth.month, date_of_birth.day)
    to_next_birthday = next_birthday_date - today
    life_info['to_next_birthday'] = to_next_birthday.days

    print(date.today() + timedelta(days=243))

    return render_template('life_info.html', life_info=life_info)


if __name__ == '__main__':
    app.run()
