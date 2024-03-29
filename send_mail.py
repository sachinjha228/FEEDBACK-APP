import smtplib 
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'api'
    password = '27afb4831eb70186719c59b4e1618b6e'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    sender_email = "email@example.com"
    receiver_email = "sachinjhamahua@gmail.com"
    msg = MIMEText(message, 'html')
    msg['subject'] = 'Lexux Feedback'
    msg['from'] = sender_email
    msg['to'] = receiver_email

    # send mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())