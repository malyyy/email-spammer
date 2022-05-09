import smtplib
import threading
import os

EMAIL_ADDRESS = 'your email'
EMAIL_PASSWORD = 'email password'
EMAIL_RECEIVER = input("Enter receiver email: ")
MSG = input("Enter a message which will be sent: ")
count = 0

def send_mail():
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, EMAIL_RECEIVER, MSG)
    server.quit()


def do_request(count):
    while True:
        send_mail()
        count += 1
        print(count)


threads = []
try:
    for i in range(10):
        t = threading.Thread(target=do_request(count=count))
        t.daemon = True
        threads.append(t)

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()
except KeyboardInterrupt:
    print("Program ended")
    os.system("pause")