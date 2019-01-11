import quandl
from datetime import date

api_key = 'V27zxJstxpUyKRzbawUR'
quandl.ApiConfig.api_key = api_key

core = {'EOD/MSFT': 'Microsoft', 'EOD/AAPL': 'Apple', 'EOD/INTC': 'Intel'}

today = date.today()
end_date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)

data = {}
def create_data():
    for key, value in core.items():
        company = value
        file_name = 'assets/' + str(company) + '.csv'
        code = key
        data = quandl.get(code, start_date="2017-01-01", end_date=end_date)
        data.to_csv(file_name)
