import datetime

def get_days_from_today(date):

    try:
        formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.date.today()

        difference = (today - formatted_date).days
        return difference
    
    except Exception as e:
        print(e, '\nPlease enter correct date in format "YYYY-MM-DD".')





