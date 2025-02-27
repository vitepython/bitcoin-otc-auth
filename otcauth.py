#!/usr/bin/env python3

import http.client
import gnupg
import getpass
import tkinter as tk

secret = getpass.getpass("Enter password: ")
path = getpass.getpass("Enter the path to your key (default is ~/path/to/your/key/): ")

def auth():
    # Retrieve the encrypted message
    conn = http.client.HTTPConnection("bitcoin-otc.com")
    conn.request("GET", "/otps/KEY-FINGER-PRINT")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    # One time OTC secret phrase
    otc = r1.read().decode()
    conn.close()
    print(otc)

    # Decrypt the message
    gpg = gnupg.GPG(gnupghome=path)
    decrypted_data = gpg.decrypt(otc, passphrase=secret)
    print(decrypted_data)

    # Open a window with the decrypted message
    root = tk.Tk()
    w = tk.Label(root, text=str(decrypted_data))
    w.pack()

    # Copy decrypted message to clipboard
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(str(decrypted_data))
    root.destroy()
    root.mainloop()

auth()
