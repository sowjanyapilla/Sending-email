#Sending mail  
import smtplib
my_email="pillasowjanya07@gmail.com" #sender mail
password ="Sowji@143"
connection=smtplib.SMTP("smtp.gmail.com",587)#establishing connection
connection.starttls() #establishing TLS connection for security
connection.login(user=my_email,password=password ) #login
connection.sendmail(from_addr=my_email,to_addrs="sowjanya@gmail.com",msg="hiiiii")
print("mail sent")
connection.close()
