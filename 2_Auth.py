# Auth
from sys import *

email_sent = False

def email_requested(response_code, message):
   print "Code requested!"
   print "Response code: " + str(response_code)
   print "Message: " + message
   global email_sent
   email_sent = True
   return 0

CALLBACKFUNCTION = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)
email_requested_func = CALLBACKFUNCTION(email_requested)

print "Please type your email: "
email = stdin.readline()

lib.modioEmailRequest(email, email_requested_func)

while email_sent:
   None

code_exchanged = False

def email_exchanged(response_code, message):

   print "Response code: " + str(response_code)
   if response_code == 200:
      print "Code exchanged!"
   else:
      print "Error exchanging code"
   print "Message: " + message
   global code_exchanged
   code_exchanged = True
   return 0

email_exchanged_func = CALLBACKFUNCTION(email_exchanged)

print "Please type the 5-digit code sent to your email: "
code = stdin.readline()

lib.modioEmailExchange(code, email_exchanged_func)

while code_exchanged:
   None
