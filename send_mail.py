#Turn Access for less secure apps setting on
import smtplib 
def send_email(recipient, subject, body): 
     user,pwd=("aa.universitesi","Aa1231234")
     FROM = user 
     TO = recipient if isinstance(recipient, list) else [recipient] 
     SUBJECT = subject 
     TEXT = body 
  
     # Prepare actual message 
     message = """From: %s\nTo: %s\nSubject: %s\n\n%s 
     """ % (FROM, ", ".join(TO), SUBJECT, TEXT) 
     try: 
         server = smtplib.SMTP("smtp.gmail.com", 587) 
         server.ehlo() 
         server.starttls() 
         server.login(user, pwd) 
         server.sendmail(FROM, TO, message) 
         server.close() 
         print('successfully sent the mail') 
         
     except Exception as e: 
         print("failed to send mail") 
         print(e.with_traceback()) 
