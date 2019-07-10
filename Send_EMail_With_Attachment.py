# Below code sends the attachment created in previous step in EMail
# Please edit lines 44.45.
# Update password in line 95
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "raghuparvatha@gmail.com"
toaddr = "raghu.parvatha@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Data Profile of the files we received"

# string to store the body of the mail
body = "Hi Team,

<p>Please find the scoring report attached.  If all target counts look acceptable then proceed with launching.  If something doesn't look correct please go to playMAKER and re-run the scoring to view error.</p>

<p>Regards,</p>
Raghu"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "Profiling.html"
attachment = open(r'/Users/xyxz/abc/Sales_Data_Profiling.html', "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "PASSWORD")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
