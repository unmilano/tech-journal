import getpass

passw = getpass.getpass() # this asks for the user's password
from pyVim.connect import SmartConnect
import ssl
s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si= SmartConnect(host="10.0.17.3", user="anthony-adm@anthony.local", pwd=passw, sslContext=s)
aboutInfo=si.content.about
print(aboutInfo)
print(aboutInfo.fullName)