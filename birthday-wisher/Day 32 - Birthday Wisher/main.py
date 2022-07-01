import smtplib
import datetime as dt
import random
import pandas as pd


MY_EMAIL = "thehappygeoscientist@gmail.com"
PASSWORD = "08happy12:"

#connection = smtplib.SMTP("smtp.gmail.com")
#connection.starttls()  # make connection secure
#connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="rosy_0894@hotmail.com", msg="Subject:Hello\n\nThis is the body of the email ")
# connection.close()

#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#
#date_of_birth = dt.datetime(year=1994, month=12, day=08, hour=17)

### ------------- Monday motivation --------------###
#now = dt.datetime.now()
#weekday = now.weekday()
#
#if weekday == 2:
#    with open("quotes.txt") as quote_file:
#        all_quotes = quote_file.readlines()
#        quote = random.choice(all_quotes)
#
#    print(quote)
#
#    with smtplib.SMTP("smtp.gmail.com") as connection:
#        connection.starttls()  # make connection secure
#        connection.login(my_email, password)
#        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Daily motivation\n\n{quote}")
#        #connection.close()
#------------------------------------------------

# -------------- birthday wish card ------------####
today = dt.datetime.now()
today_tuple = (today.month, today.day)

def create_birthday_card():
    try:
        data_birthday_dates = pd.read_csv("birthdays.csv")
        birthday_dates_dict = {(data_row['Month'], data_row['Day']): data_row for (index, data_row) in data_birthday_dates.iterrows()}

        if today_tuple in birthday_dates_dict:
            birthday_person = birthday_dates_dict[today_tuple]
            file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
            with open(file_path) as letter_file:
                contents = letter_file.read()
                contents.replace("[Name]", birthday_person["Name"])

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()  # make connection secure
                connection.login(MY_EMAIL,PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'], msg=f"Happy birthday!\n\n{contents}")

    except FileNotFoundError:
        birthday_dates_dict = {'Name': [], 'Email':[],'Month':[],'Day':[],'Year':[] }
        birthday_dates_dict_df = pd.DataFrame(data=birthday_dates_dict)
        birthday_dates_dict_df.to_csv('birthdays.csv')




create_birthday_card()

