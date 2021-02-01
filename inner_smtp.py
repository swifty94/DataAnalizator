import smtplib, ssl, socket, os, shutil, datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64
from settings import logging

class Notificator(object):
  """
  Class for reporting data once job is finished
  """
  @staticmethod
  def send_email(smtp_port, smtp_server, smtp_user, smtp_pass, receiver_email, outcome, attach=None):
    try:
      host = socket.gethostname()
      project = os.path.join(os.path.dirname(__file__))
      header = "Email from HOST: {} PROJECT: {}".format(host,project)
      message = MIMEMultipart("alternative")
      message["Subject"] = header
      message["From"] = smtp_user
      message["To"] = receiver_email
      now = datetime.datetime.now()
      timestampt = now.strftime("%Y-%m-%d-%H-%M")
      attach_file_name = f'{attach}-{timestampt}.txt'    

      # Create the plain-text and HTML version of your message
      TEXT = """
      Subject: {}

      Greetings!    \n
      Job finished. \n
      Result: {}    \n
      Log {} attached. \n
      Best Regards, \n
      AutomationAgentPy \n
      """.format(header, outcome, attach_file_name)

      HTML = """
      <!DOCTYPE html>
      <html lang="en">
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">    
      <body>
      <div> 
        <p>Greetings!</p>
        <p>Job finished.</p>
        <p>Result: {}</p>
        <p>Log {} attached</p>      
        <p>Best Regards,</p>
        <p>AutomationAgentPy</p>       
      </div>
      </body>
      </html>
      """.format(outcome, attach_file_name)    
      
      shutil.copy(attach, attach_file_name)    
      f = open(attach_file_name, 'r')
      attachment = MIMEText(f.read())
      attachment.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
      message.attach(attachment)

      # Turn these into plain/html MIMEText objects
      part1 = MIMEText(TEXT, "plain")
      part2 = MIMEText(HTML, "html")

      # Add HTML/plain-text parts to MIMEMultipart message
      # The email client will try to render the last part first
      message.attach(part1)
      message.attach(part2)
    except Exception:
      logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)

    # Create secure connection with server and send email
    try:
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
          server.login(smtp_user, smtp_pass)
          logging.info(f'{__class__.__name__ } [SMTP session ARGS: \n Server: {smtp_server} \n Sender: {smtp_user} \n Attachment: {attach_file_name} \n Receiver: {receiver_email}')
          server.sendmail(smtp_user, receiver_email, message.as_string())
          logging.info(f'{__class__.__name__ }] [Email sent ')
          server.quit()
    except Exception as e:
      logging.exception(f'{__class__.__name__ } [Exception: {e}', exc_info=1)

  @staticmethod
  def send_to_messenger():
    pass