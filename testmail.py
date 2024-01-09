import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('okdummyemail@gmail.com', 'Dummyemail#ok123')
subject = "test python"
body = "I Love Python"
message = "subject: {}\n\n{}".format(subject, body)
listadd = ['moneyyiiss@gmail.com']

ob.sendmail('okdummyemail@gmail.com', listadd, message)  # Use your actual email
print("send mail")
ob.quit()
