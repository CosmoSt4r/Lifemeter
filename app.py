from flask import Flask, abort
from utils import number_of_leap_years
from datetime import datetime, timedelta, date, tzinfo

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/<date_of_birth>')
def life_info_page(date_of_birth):

    try:
        date_of_birth = date.fromisoformat(date_of_birth)
    except ValueError:
        return abort(404)

    today = date.today()

    lived = today - date_of_birth
    ages = (lived.days - number_of_leap_years(date_of_birth)) // 365
    lived_percentage = round(lived / timedelta(days=365*78) * 100, 2)
    have_to_live = timedelta(days=365*78) - lived
    next_birthday_date = date(date_of_birth.year + ages + 1, date_of_birth.month, date_of_birth.day)
    to_next_birthday = next_birthday_date - today

    return f"You are now {ages} years old" \
        f"<br>You've born on {date_of_birth.strftime('%A')}" \
        f"<br>Lived: {lived.days} days" \
        f"<br>Have: {have_to_live.days} days" \
        f"<br>Percents: {lived_percentage}%" \
        f"<br>To next birthday: {to_next_birthday.days}"


if __name__ == '__main__':
    app.run()
