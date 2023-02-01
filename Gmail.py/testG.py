import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class GTest:

     def GmailF(mail_from, mail_to, mail_subject,mail_body,username,password):
             try:
                mimemsg = MIMEMultipart()
                mimemsg['From']=mail_from
                mimemsg['To']=mail_to
                mimemsg['Subject']=mail_subject
                mimemsg.attach(MIMEText(mail_body, 'plain'))
                connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
                connection.starttls()
                connection.login(username,password)
                connection.send_message(mimemsg)
                print("Message sent successfully")
             except Exception as e:
                print("Failed to send message" +e)
             connection.quit()
print("========Password=========")
Password = input()

Test = GTest
Test.GmailF("jeronimoelst08@gmail.com", "ezequielcarrillo@gmail.com", "hola capo","kpo","jeronimoelst08@gmail.com",Password)

# contraseña: snvhroggmvevhuns
