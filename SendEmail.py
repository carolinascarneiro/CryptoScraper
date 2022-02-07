import smtplib

class SendEmail:

    def __init__(self, USER, PASS, data) -> None:
        self.USER = USER
        self.PASS = PASS
        self.data = data

    @staticmethod
    def send_email(USER, PASS, data):
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(USER, PASS)
        s.sendmail(USER, USER, data)
        s.quit()