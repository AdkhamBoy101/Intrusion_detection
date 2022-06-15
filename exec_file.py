import RPi.GPIO as gpio
import picamera, time, smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

HOST_MAIL = "adkhamjon101@gamil.com"
HOST_PASSWD = "your_password"
DESTINATION_ADDR = "makhmudjonovbboy@gmail.com"

mail = MIMEMultipart()

mail["From"] = HOST_MAIL
mail["To"] = DESTINATION_ADDR
mail["Subject"] = "ROOM SECURITY ALERT!!!"
body = "Someone has hust entered to your room You can see the object in the attached file"

pir = 18
high = 1
low = 0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(pir, gpio.IN)
data = ""

def sendMail(data):
    mail.attach(MIMEText(body, "plain"))
    print(data)
    dat = "%s.jpg"%data 
    print(dat)
    attachment = open(dat, 'rb')
    image = MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(HOST_MAIL, HOST_PASSWD)
    text = mail.as_string()
    server.sendmail(HOST_MAIL, DESTINATION_ADDR, text)
    server.quit()

def take_image():
    data = time.strftime("%d_%b_%Y|%H:%M:%S")
    camera.start_preview()
    time.sleep(5)
    print(data)
    camera.capture("%s.jpg"%data)
    camera.stop_preview()
    time.sleep(1)
    sendMail(data)


camera = picamera.PiCamera()
#camera.rotation=180
camera.awb_mode = "auto"
camera.brightness = 56

while 1:
    if gpio.input(pir) == 1:
        capture_image()
        while(gpio.input(pir) == 1):
            time.sleep(1)
    else:
        time.sleep(0.01)
