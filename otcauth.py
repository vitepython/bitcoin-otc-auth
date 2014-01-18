#!/usr/bin/env python
import httplib
import gnupg
import getpass
from Tkinter import *

secret = getpass.getpass("enter password")
path = getpass.getpass("~/path/to/youre/key/") # alternative is hardcoding or using arguments

def auth():

# Retrieve the encrypted message
        conn = httplib.HTTPConnection("bitcoin-otc.com")
        conn.request("GET", "/otps/KEY-FINGER-PRINT")
        r1 = conn.getresponse()
        print r1.status, r1.reason

        # one time OTC secretphrase
        otc = r1.read()
        conn.close()
        print otc

        # decrypt the message
        gpg = gnupg.GPG(gnupghome=path)
        decrypted_data = gpg.decrypt(otc, passphrase=secret)
        print decrypted_data

        # open a window with the decrypted message
        master = Tk()
        w = Label(master, text = decrypted_data)
        w.pack()

        # copy decrypted message to clipboard
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(decrypted_data)
        r.destroy()
        mainloop()
        
auth()
