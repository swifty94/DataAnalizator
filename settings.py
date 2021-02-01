import logging.config
import logging
logging.config.fileConfig('logger.ini', disable_existing_loggers=False)

# User dependent constants to be defined here

# Define list of CSV reports to analize in format acs{number}.csv
#   E.g., you have 4 nodes, 2 acs and 2 management,thus, list will be :
#
#   ACS_CSV = ['acs1.csv','acs2.csv']
#   MNG_CSV = ['mng1.csv','mng2.csv']
#

ACS_CSV = []
MNG_CSV = []


#   SMTP settings for email notifications:
#   You can send to single and multiple recepients defined in multiple_receivers variable

smtp_enable = False
smtp_port = 465
smtp_server = ""
smtp_user = ""
smtp_pass = ""
receiver_email = ""
