print(__file__)
import os
print(os.getcwd())
from tkinter import*
from sys import version_info
if version_info.major == 2:
    import tkinter as tk
elif version_info.major == 3:
    import tkinter as tk
import random
with open('variables.txt', 'r') as file:
    lines = file.readlines()
    score = int(lines[0].strip())
    record = int(lines[1].strip())
def bon():
    global feu
    global score
    global record
    with open('variables.txt', 'r') as file:
        lines = file.readlines()
        score = int(lines[0].strip())
        record = int(lines[1].strip())
    score+=1
    if score>record:
        record=score
    with open('variables.txt', 'w') as file:
        file.write(f"{score}\n")
        file.write(f"{record}\n")
    print(f"c'est la bonne réponce, votre score est de : {score}")
    print(f"votre record est {record}")
    feu.destroy()
    v = random.randint(1, 240)
    if v == 1:
        print(afg())
    elif v == 2:
        print(afr())
    elif v == 3:
        print(alb())
    elif v == 4:
        print(alg())
    elif v == 5:
        print(al())
    elif v == 6:
        print(an())
    elif v == 7:
        print(ang())
    elif v == 8:
        print(angu())
    elif v == 9:
        print(ant())
    elif v == 10:
        print(antn())
    elif v == 11:
        print(ara())
    elif v == 12:
        print(arg())
    elif v == 13:
        print(arm())
    elif v == 14:
        print(aru())
    elif v == 15:
        print(aus())
    elif v == 16:
        print(aut())
    elif v == 17:
        print(az())
    elif v == 18:
        print(baha())
    elif v == 19:
        print(bah())
    elif v == 20:
        print(ban())
    elif v == 21:
        print(bar())
    elif v == 22:
        print(bel())
    elif v == 23:
        print(beli())
    elif v == 24:
        print(ben())
    elif v == 25:
        print(ber())
    elif v == 26:
        print(bh())
    elif v == 27:
        print(bie())
    elif v == 28:
        print(bir())
    elif v == 29:
        print(bol())
    elif v == 30:
        print(bos())
    elif v == 31:
        print(bot())
    elif v == 32:
        print(bre())
    elif v == 33:
        print(bru())
    elif v == 34:
        print(bul())
    elif v == 35:
        print(bur())
    elif v == 36:
        print(bu())
    elif v == 37:
        print(ca())
    elif v == 38:
        print(cam())
    elif v == 39:
        print(can())
    elif v == 40:
        print(cap())
    elif v == 41:
        print(ch())
    elif v == 42:
        print(chi())
    elif v == 43:
        print(chy())
    elif v == 44:
        print(col())
    elif v == 45:
        print(com())
    elif v == 46:
        print(con())
    elif v == 47:
        print(cos())
    elif v == 48:
        print(co())
    elif v == 49:
        print(cot())
    elif v == 50:
        print(cro())
    elif v == 51:
        print(cu())
    elif v == 52:
        print(dan())
    elif v == 53:
        print(dji())
    elif v == 54:
        print(dom())
    elif v == 55:
        print(eg())
    elif v == 56:
        print(em())
    elif v == 57:
        print(eq())
    elif v == 58:
        print(er())
    elif v == 59:
        print(es())
    elif v == 60:
        print(est())
    elif v == 61:
        print(efm())
    elif v == 62:
        print(eu())
    elif v == 63:
        print(et())
    elif v == 64:
        print(fi())
    elif v == 65:
        print(fin())
    elif v == 66:
        print(fra())
    elif v == 67:
        print(ga())
    elif v == 68:
        print(gam())
    elif v == 69:
        print(geo())
    elif v == 70:
        print(geos())
    elif v == 71:
        print(gh())
    elif v == 72:
        print(gib())
    elif v == 73:
        print(gr())
    elif v == 74:
        print(gre())
    elif v == 75:
        print(gro())
    elif v == 76:
        print(gu())
    elif v == 77:
        print(gua())
    elif v == 78:
        print(guat())
    elif v == 79:
        print(gui())
    elif v == 80:
        print(gue())
    elif v == 81:
        print(gub())
    elif v == 82:
        print(guy())
    elif v == 83:
        print(guyf())
    elif v == 84:
        print(ha())
    elif v == 85:
        print(h())
    elif v == 86:
        print(ho())
    elif v == 87:
        print(hon())
    elif v == 88:
        print(ich())
    elif v == 89:
        print(ima())
    elif v == 90:
        print(ino())
    elif v == 91:
        print(ial())
    elif v == 92:
        print(ica())
    elif v == 93:
        print(ico())
    elif v == 94:
        print(ick())
    elif v == 95:
        print(ife())
    elif v == 96:
        print(iml())
    elif v == 97:
        print(imn())
    elif v == 98:
        print(imh())
    elif v == 99:
        print(ip())
    elif v == 100:
        print(isa())
    elif v == 101:
        print(itc())
    elif v == 102:
        print(ivb())
    elif v == 103:
        print(ivet())
    elif v == 104:
        print(ind())
    elif v == 105:
        print(indo())
    elif v == 106:
        print(ira())
    elif v == 107:
        print(iraq())
    elif v == 108:
        print(irl())
    elif v == 109:
        print(isl())
    elif v == 110:
        print(isr())
    elif v == 111:
        print(ita())
    elif v == 112:
        print(jam())
    elif v == 113:
        print(jap())
    elif v == 114:
        print(jor())
    elif v == 115:
        print(kaz())
    elif v == 116:
        print(ken())
    elif v == 117:
        print(kir())
    elif v == 118:
        print(kiri())
    elif v == 119:
        print(kow())
    elif v == 120:
        print(lao())
    elif v == 121:
        print(lev())
    elif v == 122:
        print(les())
    elif v == 123:
        print(let())
    elif v == 124:
        print(lib())
    elif v == 125:
        print(libe())
    elif v == 126:
        print(liby())
    elif v == 127:
        print(lie())
    elif v == 128:
        print(lit())
    elif v == 129:
        print(lux())
    elif v == 130:
        print(mac())
    elif v == 131:
        print(mad())
    elif v == 132:
        print(mal())
    elif v == 133:
        print(mala())
    elif v == 134:
        print(mald())
    elif v == 135:
        print(mali())
    elif v == 136:
        print(malt())
    elif v == 137:
        print(mar())
    elif v == 138:
        print(mart())
    elif v == 139:
        print(mau())
    elif v == 140:
        print(maur())
    elif v == 141:
        print(may())
    elif v == 142:
        print(mex())
    elif v == 143:
        print(mol())
    elif v == 144:
        print(mon())
    elif v == 145:
        print(mong())
    elif v == 146:
        print(mont())
    elif v == 147:
        print(monts())
    elif v == 148:
        print(moz())
    elif v == 149:
        print(nam())
    elif v == 150:
        print(nau())
    elif v == 151:
        print(nep())
    elif v == 152:
        print(nic())
    elif v == 153:
        print(nig())
    elif v == 154:
        print(nige())
    elif v == 155:
        print(niu())
    elif v == 156:
        print(nor())
    elif v == 157:
        print(nou())
    elif v == 158:
        print(nz())
    elif v == 159:
        print(oma())
    elif v == 160:
        print(oug())
    elif v == 161:
        print(ouz())
    elif v == 162:
        print(pak())
    elif v == 163:
        print(pal())
    elif v == 164:
        print(pan())
    elif v == 165:
        print(pap())
    elif v == 166:
        print(par())
    elif v == 167:
        print(pay())
    elif v == 168:
        print(per())
    elif v == 169:
        print(phi())
    elif v == 170:
        print(pol())
    elif v == 171:
        print(poly())
    elif v == 172:
        print(por())
    elif v == 173:
        print(port())
    elif v == 174:
        print(qat())
    elif v == 175:
        print(repc())
    elif v == 176:
        print(rdm())
    elif v == 177:
        print(rdc())
    elif v == 178:
        print(rd())
    elif v == 179:
        print(rc())
    elif v == 180:
        print(rt())
    elif v == 181:
        print(reu())
    elif v == 182:
        print(rou())
    elif v == 183:
        print(rus())
    elif v == 184:
        print(rwa())
    elif v == 185:
        print(sah())
    elif v == 186:
        print(sh())
    elif v == 187:
        print(sl())
    elif v == 188:
        print(sk())
    elif v == 189:
        print(sm())
    elif v == 190:
        print(sp())
    elif v == 191:
        print(sv())
    elif v == 192:
        print(sal())
    elif v == 193:
        print(sam())
    elif v == 194:
        print(sama())
    elif v == 195:
        print(sao())
    elif v == 196:
        print(sen())
    elif v == 197:
        print(ser())
    elif v == 198:
        print(sey())
    elif v == 199:
        print(sie())
    elif v == 200:
        print(sin())
    elif v == 201:
        print(slo())
    elif v == 202:
        print(slov())
    elif v == 203:
        print(som())
    elif v == 204:
        print(sou())
    elif v == 205:
        print(sri())
    elif v == 206:
        print(sue())
    elif v == 207:
        print(sui())
    elif v == 208:
        print(sur())
    elif v == 209:
        print(jm())
    elif v == 210:
        print(esw())
    elif v == 211:
        print(syr())
    elif v == 212:
        print(tad())
    elif v == 213:
        print(tai())
    elif v == 214:
        print(tan())
    elif v == 215:
        print(tch)
    elif v == 216:
        print(taf())
    elif v == 217:
        print(tha())
    elif v == 218:
        print(tim())
    elif v == 219:
        print(tog())
    elif v == 220:
        print(ton())
    elif v == 221:
        print(tet())
    elif v == 222:
        print(tun())
    elif v == 223:
        print(tur())
    elif v == 224:
        print(turq())
    elif v == 225:
        print(tuv())
    elif v == 226:
        print(ukr())
    elif v == 227:
        print(uru())
    elif v == 228:
        print(van())
    elif v == 229:
        print(ven())
    elif v == 230:
        print(vie())
    elif v == 231:
        print(wal())
    elif v == 232:
        print(yem())
    elif v == 233:
        print(zam())
    elif v == 234:
        print(zim())
    elif v == 235:
        print(angl())
    elif v == 236:
        print(pays())
    elif v == 237:
        print(irln())
    elif v == 238:
        print(eco())
    elif v == 239:
        print(kos())
    elif v == 240:
        print(sous())
def ree():
    global score
    global fau
    with open('variables.txt', 'r') as file:
        lines = file.readlines()
        score = int(lines[0].strip())
        record = int(lines[1].strip())
    score=0
    with open('variables.txt', 'w') as file:
        file.write(f"{score}\n")
        file.write(f"{record}\n")
    fau.destroy()
    v = random.randint(1, 240)
    if v == 1:
        print(afg())
    elif v == 2:
        print(afr())
    elif v == 3:
        print(alb())
    elif v == 4:
        print(alg())
    elif v == 5:
        print(al())
    elif v == 6:
        print(an())
    elif v == 7:
        print(ang())
    elif v == 8:
        print(angu())
    elif v == 9:
        print(ant())
    elif v == 10:
        print(antn())
    elif v == 11:
        print(ara())
    elif v == 12:
        print(arg())
    elif v == 13:
        print(arm())
    elif v == 14:
        print(aru())
    elif v == 15:
        print(aus())
    elif v == 16:
        print(aut())
    elif v == 17:
        print(az())
    elif v == 18:
        print(baha())
    elif v == 19:
        print(bah())
    elif v == 20:
        print(ban())
    elif v == 21:
        print(bar())
    elif v == 22:
        print(bel())
    elif v == 23:
        print(beli())
    elif v == 24:
        print(ben())
    elif v == 25:
        print(ber())
    elif v == 26:
        print(bh())
    elif v == 27:
        print(bie())
    elif v == 28:
        print(bir())
    elif v == 29:
        print(bol())
    elif v == 30:
        print(bos())
    elif v == 31:
        print(bot())
    elif v == 32:
        print(bre())
    elif v == 33:
        print(bru())
    elif v == 34:
        print(bul())
    elif v == 35:
        print(bur())
    elif v == 36:
        print(bu())
    elif v == 37:
        print(ca())
    elif v == 38:
        print(cam())
    elif v == 39:
        print(can())
    elif v == 40:
        print(cap())
    elif v == 41:
        print(ch())
    elif v == 42:
        print(chi())
    elif v == 43:
        print(chy())
    elif v == 44:
        print(col())
    elif v == 45:
        print(com())
    elif v == 46:
        print(con())
    elif v == 47:
        print(cos())
    elif v == 48:
        print(co())
    elif v == 49:
        print(cot())
    elif v == 50:
        print(cro())
    elif v == 51:
        print(cu())
    elif v == 52:
        print(dan())
    elif v == 53:
        print(dji())
    elif v == 54:
        print(dom())
    elif v == 55:
        print(eg())
    elif v == 56:
        print(em())
    elif v == 57:
        print(eq())
    elif v == 58:
        print(er())
    elif v == 59:
        print(es())
    elif v == 60:
        print(est())
    elif v == 61:
        print(efm())
    elif v == 62:
        print(eu())
    elif v == 63:
        print(et())
    elif v == 64:
        print(fi())
    elif v == 65:
        print(fin())
    elif v == 66:
        print(fra())
    elif v == 67:
        print(ga())
    elif v == 68:
        print(gam())
    elif v == 69:
        print(geo())
    elif v == 70:
        print(geos())
    elif v == 71:
        print(gh())
    elif v == 72:
        print(gib())
    elif v == 73:
        print(gr())
    elif v == 74:
        print(gre())
    elif v == 75:
        print(gro())
    elif v == 76:
        print(gu())
    elif v == 77:
        print(gua())
    elif v == 78:
        print(guat())
    elif v == 79:
        print(gui())
    elif v == 80:
        print(gue())
    elif v == 81:
        print(gub())
    elif v == 82:
        print(guy())
    elif v == 83:
        print(guyf())
    elif v == 84:
        print(ha())
    elif v == 85:
        print(h())
    elif v == 86:
        print(ho())
    elif v == 87:
        print(hon())
    elif v == 88:
        print(ich())
    elif v == 89:
        print(ima())
    elif v == 90:
        print(ino())
    elif v == 91:
        print(ial())
    elif v == 92:
        print(ica())
    elif v == 93:
        print(ico())
    elif v == 94:
        print(ick())
    elif v == 95:
        print(ife())
    elif v == 96:
        print(iml())
    elif v == 97:
        print(imn())
    elif v == 98:
        print(imh())
    elif v == 99:
        print(ip())
    elif v == 100:
        print(isa())
    elif v == 101:
        print(itc())
    elif v == 102:
        print(ivb())
    elif v == 103:
        print(ivet())
    elif v == 104:
        print(ind())
    elif v == 105:
        print(indo())
    elif v == 106:
        print(ira())
    elif v == 107:
        print(iraq())
    elif v == 108:
        print(irl())
    elif v == 109:
        print(isl())
    elif v == 110:
        print(isr())
    elif v == 111:
        print(ita())
    elif v == 112:
        print(jam())
    elif v == 113:
        print(jap())
    elif v == 114:
        print(jor())
    elif v == 115:
        print(kaz())
    elif v == 116:
        print(ken())
    elif v == 117:
        print(kir())
    elif v == 118:
        print(kiri())
    elif v == 119:
        print(kow())
    elif v == 120:
        print(lao())
    elif v == 121:
        print(lev())
    elif v == 122:
        print(les())
    elif v == 123:
        print(let())
    elif v == 124:
        print(lib())
    elif v == 125:
        print(libe())
    elif v == 126:
        print(liby())
    elif v == 127:
        print(lie())
    elif v == 128:
        print(lit())
    elif v == 129:
        print(lux())
    elif v == 130:
        print(mac())
    elif v == 131:
        print(mad())
    elif v == 132:
        print(mal())
    elif v == 133:
        print(mala())
    elif v == 134:
        print(mald())
    elif v == 135:
        print(mali())
    elif v == 136:
        print(malt())
    elif v == 137:
        print(mar())
    elif v == 138:
        print(mart())
    elif v == 139:
        print(mau())
    elif v == 140:
        print(maur())
    elif v == 141:
        print(may())
    elif v == 142:
        print(mex())
    elif v == 143:
        print(mol())
    elif v == 144:
        print(mon())
    elif v == 145:
        print(mong())
    elif v == 146:
        print(mont())
    elif v == 147:
        print(monts())
    elif v == 148:
        print(moz())
    elif v == 149:
        print(nam())
    elif v == 150:
        print(nau())
    elif v == 151:
        print(nep())
    elif v == 152:
        print(nic())
    elif v == 153:
        print(nig())
    elif v == 154:
        print(nige())
    elif v == 155:
        print(niu())
    elif v == 156:
        print(nor())
    elif v == 157:
        print(nou())
    elif v == 158:
        print(nz())
    elif v == 159:
        print(oma())
    elif v == 160:
        print(oug())
    elif v == 161:
        print(ouz())
    elif v == 162:
        print(pak())
    elif v == 163:
        print(pal())
    elif v == 164:
        print(pan())
    elif v == 165:
        print(pap())
    elif v == 166:
        print(par())
    elif v == 167:
        print(pay())
    elif v == 168:
        print(per())
    elif v == 169:
        print(phi())
    elif v == 170:
        print(pol())
    elif v == 171:
        print(poly())
    elif v == 172:
        print(por())
    elif v == 173:
        print(port())
    elif v == 174:
        print(qat())
    elif v == 175:
        print(repc())
    elif v == 176:
        print(rdm())
    elif v == 177:
        print(rdc())
    elif v == 178:
        print(rd())
    elif v == 179:
        print(rc())
    elif v == 180:
        print(rt())
    elif v == 181:
        print(reu())
    elif v == 182:
        print(rou())
    elif v == 183:
        print(rus())
    elif v == 184:
        print(rwa())
    elif v == 185:
        print(sah())
    elif v == 186:
        print(sh())
    elif v == 187:
        print(sl())
    elif v == 188:
        print(sk())
    elif v == 189:
        print(sm())
    elif v == 190:
        print(sp())
    elif v == 191:
        print(sv())
    elif v == 192:
        print(sal())
    elif v == 193:
        print(sam())
    elif v == 194:
        print(sama())
    elif v == 195:
        print(sao())
    elif v == 196:
        print(sen())
    elif v == 197:
        print(ser())
    elif v == 198:
        print(sey())
    elif v == 199:
        print(sie())
    elif v == 200:
        print(sin())
    elif v == 201:
        print(slo())
    elif v == 202:
        print(slov())
    elif v == 203:
        print(som())
    elif v == 204:
        print(sou())
    elif v == 205:
        print(sri())
    elif v == 206:
        print(sue())
    elif v == 207:
        print(sui())
    elif v == 208:
        print(sur())
    elif v == 209:
        print(jm())
    elif v == 210:
        print(esw())
    elif v == 211:
        print(syr())
    elif v == 212:
        print(tad())
    elif v == 213:
        print(tai())
    elif v == 214:
        print(tan())
    elif v == 215:
        print(tch)
    elif v == 216:
        print(taf())
    elif v == 217:
        print(tha())
    elif v == 218:
        print(tim())
    elif v == 219:
        print(tog())
    elif v == 220:
        print(ton())
    elif v == 221:
        print(tet())
    elif v == 222:
        print(tun())
    elif v == 223:
        print(tur())
    elif v == 224:
        print(turq())
    elif v == 225:
        print(tuv())
    elif v == 226:
        print(ukr())
    elif v == 227:
        print(uru())
    elif v == 228:
        print(van())
    elif v == 229:
        print(ven())
    elif v == 230:
        print(vie())
    elif v == 231:
        print(wal())
    elif v == 232:
        print(yem())
    elif v == 233:
        print(zam())
    elif v == 234:
        print(zim())
    elif v == 235:
        print(angl())
    elif v == 236:
        print(pays())
    elif v == 237:
        print(irln())
    elif v == 238:
        print(eco())
    elif v == 239:
        print(kos())
    elif v == 240:
        print(sous())
def faux():
    global score
    global feu
    global record
    global fau
    print(f"c'est faux  votre score était de : {score} et votre record de: {record}")
    feu.destroy()
    fau=Tk()
    fau.geometry(f"{fau.winfo_screenwidth()}x{fau.winfo_screenheight()}")
    fau.title=('faux')
    fau.configure(bg="black")
    texte=Label(fau,text=f'vous avez perdu votre score est de: {score}',bg='black',fg="white")
    texte2=Label(fau,text=f'votre record est {record}',bg="black",fg="white")
    texte3=Label(fau,text="INSTA:lopysc7",bg="black",fg="white")
    root=tk.Button(fau,text="QUITTER",command=quit, bg="black", fg='red', activebackground='cyan',width=fau.winfo_screenwidth())
    re = tk.Button(fau, text="REESSAYER", command=ree, bg="black", fg='red', activebackground='cyan', width=fau.winfo_screenwidth())
    texte.pack()
    texte2.pack()
    texte3.pack()
    re.pack()
    root.pack()
    fau.mainloop()
    exit()
def afg():
    global feu
    global score
    global record
    feu=Tk()
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.configure(bg="black")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3= Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/afghanistan.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Afghanistan", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Libye", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Kenya", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def afr():
    global feu
    global score
    global record
    feu = Tk()
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    feu.configure(bg="black")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/afrique du sud.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Djibuti", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Afrique du sud", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Erythrée", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def alb():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/albanie.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Monténegro ", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="République de Macédoine", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Albanie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def alg():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/algérie.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Shara Occidental", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Algérie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Tunisie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def al():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/allemagne.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Allemagne", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Ghana", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Belgique", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def an():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/andorre.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Roumanie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Andorre", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Moldavie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ang():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/angola.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Angola", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Libye", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Mozambique", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def angu():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/anguilla.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Montessart", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Géorgie du Sud et les Îles Sandwich du Sud", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Anguilla", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ant():
    global feu
    global score
    global record
    feu= Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/antigua-et-barbuda.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Malawi", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Antigua-et-Barbuda", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Kiribati", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def antn():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/antilles-néerlandaises.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Chili", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Panama", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Antilles Néerlandaises", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ara():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/arabie-saoudite.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Turkmenisthan", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Arabie Saoudite", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Cocos", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def arg():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/argentine.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Argentine", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Uruguay", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Honduras", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def arm():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/armenie.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Gabon", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Arménie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Lituanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def aru():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/aruba.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Iles marshall", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Nauru", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Aruba", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def aus():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/australie.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Australie", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Nouvelle-Zélande", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Cook", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def aut():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/autriche.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Liban", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Autriche", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Lettonie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def az():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/azerbadjan.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Azerbaïdjan", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Ouzbékistan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Tadjikistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def baha():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bahamas.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Comores", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Afrique du Sud", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Bahamas", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bah():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bahrein.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Bahreïn", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Qatar", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Népal", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ban():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bangladesh.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Palaos", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Bangladesh", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Japon", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bar():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/barbade.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Barbade", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Saint-Vincent et les Grenadines", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Bosnie-Herzégovine", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bel():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/belgique.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Belgique", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Allemagne", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Tchad", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def beli():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/belize.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Haïti", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guam", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Belize", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ben():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/benin.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Madagascar", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Biélorussie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Bénin", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ber():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bermudes.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Iles Pitcairn", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Malouines", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Bermudes", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bh():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bhoutan.PNG', master=feu)
    label1 = Label(feu, image=img, )
    choix1 = tk.Button(feu, text="Bhoutan", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Pays de Galles", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Népal", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bie():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bielorussie.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Madagascar", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Biélorussie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Oman", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bir():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/birmanie.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Ethiopie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Birmanie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ghana", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bol():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bolivie.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Birmanie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Ethiopie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Bolivie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bos():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bosnie-herzegovine.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Bosnie-Herzégovine ", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Barbade", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ukraine", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bot():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/botswana.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Botswana ", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Estonie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Honduras", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bre():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bresil.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Grenade ", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Portugal", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Bresil", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bru():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/brunei.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Burundi ", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Le vatican", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Brunei", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bul():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/bulgarie.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Bulgarie", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Hongrie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iran", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bur():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/burkina_faso.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Suriname", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Burkina Faso", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ethiopie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def bu():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/burundi.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Jamaïque", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Ecosse", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Burundi", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ca():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/cambodge.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Liechtenstein", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Cambodge", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Mongolie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def cam():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/cameroun.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Cameroun", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Sénégal", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ghana", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def can():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/canada.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Canada", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Pérou", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Polynésie Française", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def cap():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/cap_vert.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Nauru", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Cap-vert", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Marshall", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ch():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/chili.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Chili", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Panama", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Antilles Néerlandaises", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def chi():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/chine.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Hong Kong", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Chine", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Vietnam", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def chy():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/chypre.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Malte", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Corée du Sud", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Chypre", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def col():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/colombie.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Colombie", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Venezuela", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Equateur", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def com():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/comores.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Ile Maurice", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Bahamas", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Comores", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def con():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/corrée_du_nord.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Costa Rica", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Thailande", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Corée du Nord", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def cos():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/corée_du_sud.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Japon", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Chypre", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Corée du Sud", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def co():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file='assets/costa_rica.PNG', master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Thaïlande", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Costa Rica", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Corée du Nord", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def cot():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/cote_d'ivoire.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Côte d'Ivoire", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Irlande", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Nigéria", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def cro():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/croatie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Slovénie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Croatie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Serbie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def cu():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/cuba.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Porto Rico", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Cuba", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Vanuatu", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def dan():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/danemark.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Danemark", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Suéde", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Finlande", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def dji():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/djibuti.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Djibouti", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Afrique du Sud", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Érythrée", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def dom():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/dominique.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Dominique", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Republique Dominicaine", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Brésil", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def eg():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/egypte.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Egypte", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Yemen", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Irak", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def em():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/emirats_arabe_unis.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Jordanie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Koweït", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Emirats Arabe Unis", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def eq():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/equateur.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Venezuela", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Equateur", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Colombie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def er():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/erythrée.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Erythrée", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Vanuatu", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Djibuti", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def es():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/espagne.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Portugal", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Espagne", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Honduras", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def est():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/estonie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Estonie", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Botswana", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Lettonie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def efm():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/etats_federes_de_micronésie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Somalie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Mariannes du nord", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Etats Fédérés de Micronésie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def eu():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/etats_unis.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Libéria", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Malaisie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Etats-Unis", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def et():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ethiopie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Ethiopie", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Birmanie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ghana", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def fi():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/fidji.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Fidji", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Caïmanes", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Malouines", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def fin():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/finlande.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Danemark", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Féroé", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Finlande", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def fra():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/france.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Pays-Bas", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Russie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="France", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ga():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/gabon.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Gambie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Arménie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Gabon", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gam():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/gambie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Arménie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Gambie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Gabon", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def geo():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/géorgie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Angleterre", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Géorgie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Irlande du Nord ", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def geos():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/géorgie_du_sud_et_iles_sandwich_du_sud.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Montessart", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Anguilla", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Géorgie du Sud et les Îles Sandwich du Sud", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gh():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ghana.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Ethiopie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Birmanie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ghana", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gib():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/gibraltar.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Pologne", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Gibraltar", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Indonésie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gr():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/gréce.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Gréce", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Libéria", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Malaisie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gre():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/grenade.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Jamaique", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Grenade", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Brésil", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gro():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/groenland.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Indonésie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Groenland", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Pologne", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gu():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/guadeloupe.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="La Réunion", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guadeloupe", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guyana", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gua():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/guam.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guam", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Belize", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Haïti", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def guat():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/guatemala.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Nicaragua", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="El Salvador", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guatemala", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gui():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/guinee.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guinée", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Mali", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Tchad", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gue():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/guinee_equatorial.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guinée Equatorial", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guinée", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guinée Bissau", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def gub():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/guinee_bissau.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guinée Equatorial", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guinée Bissau", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guinée", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def guy():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/guyana.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guyane Française", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guadeloupe", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guyana", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def guyf():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/guyana_francaise.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guyana", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="La Réunion", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guyane Française", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ha():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/haiti.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Belize", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Haïti", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guam", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def h():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/honduras.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Argentine", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Honduras", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="La Réunion", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ho():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/hong-kong.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Vietnam", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Hong-Kong", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Maroc", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def hon():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/hongrie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Tadjikistan", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Bulgarie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Hongrie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ich():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ile_christmas.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Marshall", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Salomon", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ile Christmas", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ima():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ile_de_man.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Maroc", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Ile De Man", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Hong-Kong", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ino():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ile_nortfolk.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Liban", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Nigeria", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ile Nortfolk", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ial():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_aland.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Islande", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Novége", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Åland", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ica():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_caimanse.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Fidji", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Malouines", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Caïmanes", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ico():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_cocos.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Cocos", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Turkménistan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Arabie Saoudite", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ick():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_cook.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Pitcairn", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Cook", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Malouines", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ife():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_feroe.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Féroé", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Finlande", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Åland", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def iml():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_malouines.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Malouines", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Îles Turks et Caïques", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Îles Vierges Britanniques", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def imn():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_mariannes_du_nord.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Mariannes du Nord", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Somalie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Micronésie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def imh():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_marshall.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Marshall", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Nauru", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="La Réunion", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ip():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_pitcairn.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Pitcairn", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Bermudes", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="La Réunion", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def isa():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_salomon.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Salomon", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Christmas", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Gadeloupe", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def itc():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_turks_et_caiques.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Turks et Caïques", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Malouines", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Vierges Britanniques", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ivb():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_vierges_britanniques.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Vierges Britanniques", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Turks et Caïques", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Malouines", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ivet():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iles_vierges_des_etats_unis.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iles Vierges des Etats-Unis", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Samoa Américains", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Etats-Unis", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ind():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/inde.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Niger", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Laos", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Inde", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def indo():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/indonesie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Pologne", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Indonésie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Monaco", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ira():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iran.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iran", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Tadjikistan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Hongrie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def iraq():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/iraq.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Syrie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iraq", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Yemen", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def irl():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/irlande.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Nigéria", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Côte d’Ivoire", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Irlande", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def isl():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/islande.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Îles Åland", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Norvége", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Islande", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def isr():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/israel.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Israël", command=bon, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Honduras", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Maroc", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ita():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/italie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Hongrie", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Bulgarie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Italie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def jam():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/jamaique.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Ecosse", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Burundi", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Jamaïque", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def jap():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?",bg='black',fg="white")
    texte2= Label(feu,text=f"VOTRE SCORE EST DE: {score}",bg='black',fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}",bg='black',fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/japon.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Chypre", command=faux, bg="black", fg='red', activebackground='cyan', width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Corrée du Sud", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Japon", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def jor():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/jordanie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Koweit", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Jordanie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Soudan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def kaz():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/kazakhstan.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Palaos", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Kazakhstan", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Rwanda", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ken():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/kenya.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Libye", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Afghanistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Kenya", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def kir():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/kirghizistan.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Kirghizistan", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Kiribati", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Kazakhstan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def kiri():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/kiribati.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Kirghizistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Kiribati", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Antigua-et-Barbuda", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def kow():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/koweït.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Jordanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Soudan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Koweït", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def lao():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/laos.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Niger", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Laos", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Inde", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def lev():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/le_vatican.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Le Vatican", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Barbade", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Vincent-et-les Grenadines", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def les():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/lesotho.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Gambie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Sierra Leone", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Lesotho", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def let():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/lettonie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Autriche", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Lettonie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Liban", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def lib():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/liban.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Autriche", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Norfolk", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Liban", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def libe():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/liberia.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Malaisie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Etats Unis", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Libéria", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def liby():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/libye.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Libye", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Turquie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Afghanistan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def lie():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/liechtenstein.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Cambodge", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Bosnie-Herzégovine", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Liechtenstein", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def lit():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/lituanie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Lituanie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Lettonie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Gabon", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def lux():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/luxembourg.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Luxembourg", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Pays-Bas", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Russie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mac():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/macao.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Macao", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Hong-Konk", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guadeloupe", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mad():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/madagascar.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Oman", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Madagascar", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guinée-Biseau", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mal():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/malaisie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Malaisie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Liberia", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Etats-unis", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mala():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/malawi.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Malawi", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Kiribati", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Antigua et Barbuda ", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mald():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/maldives.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Maldives", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Mauritanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Pakistan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mali():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/mali.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Tchad", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Mali", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guinée", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def malt():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/malte.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Malte", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Chypre", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Suisse", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mar():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/maroc.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Israël", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Maroc", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Vietnam", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mart():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/martinique.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Saint-Pierre-et-Miquelon", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Martinique", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Mayotte", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mau():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/maurice.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Centre Afrique", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Maurice", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Gambie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def maur():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/mauritanie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Mauritanie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Pakistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Maldives", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def may():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/mayotte.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Mayotte", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Martinique", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Pierre-et-Miquelon", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mex():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/mexique.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Mexique", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Italie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guatemala", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mol():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/moldavie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Moldavie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Roumanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Andorre", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mon():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/monaco.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Pologne", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Indonésie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Monaco", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mong():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/mongolie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Vietnam", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Cambodge", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Mongolie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def mont():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/montenegro.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Albanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="République de Macédoine", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Monténégro", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def monts():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/montessart.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Montserrat", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Géorgie du Sud et les Îles Sandwich du Sud", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Anguilla", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def moz():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/mozambique.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Mozambique", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Zimbabwe", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Comores", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nam():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/namibie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Namibie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="République Démocratique du Congo ", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Kitts-et-Nevis", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nau():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/nauru.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Aruba", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Nauru", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Îles Marshall", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nep():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/nepal.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Pakistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Bouthan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Népal", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nic():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/nicaragua.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="El Salvador", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Nicaragua", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guatemala", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nig():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/niger.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Inde", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Niger", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Nigeria", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nige():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/nigeria.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Cote d'Ivoire", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Niger", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Nigeria", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def niu():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/niue.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Bermudes", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Niué", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Nouvelle Calédonie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nor():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/norvege.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Îles Åland", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="îles Féroé", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Norvège", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nou():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/nouvelle_caledonie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Gambie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Niué", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Nouvelle-Calédonie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def nz():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/nouvelle_zelande.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Îles Cook", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Nouvelle-Zélande", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Australie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def oma():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/oman.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Madagascar", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Oman", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Biélorussie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def oug():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ouganda.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Maurice", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Ouganda", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="République Centreafrique", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ouz():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ouzbekistan.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Turkménistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Azerbaïdjan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ouzbekistan", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def pak():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/pakistan.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Turkménistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Tunisie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Pakistan", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def pal():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/palaos.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Saint-Lucie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Palaos", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Kazakhstan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def pan():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/panama.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Panama", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Chili", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="République Dominicaine", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def pap():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/papouasie-nouvelle-guinee.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Papouasie-Nouvelle-Guinée", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guinée", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guinée-Bissau", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def par():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/paraguay.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Paraguay", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Pays-Bas", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Uruguay", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def pay():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/pays-bas.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Paraguay", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Pays-Bas", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Luxembourg", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def per():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/perou.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Polynésie Française", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Canada", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Pérou", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def phi():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/philippines.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Tchéquie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Afrique du Sud", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Philippines", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def pol():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/pologne.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Indonésie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Monaco", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Pologne", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def poly():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/polynesie_francaise.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Pérou", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Canada", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Polynésie Française", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def por():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/porto_rico.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Vanuatu", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Cuba", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Porto Rico", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def port():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/portugal.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Espagne", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Portugal", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Brésil", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def qat():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/qatar.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Bahreïn", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Népal", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Qatar", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def repc():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/republique_centreafricaine.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="République Centrafricaine", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Maurice", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Gabon", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def rdm():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/republique_de_macedoine.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="République de Macédoine", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Albanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Monténégro", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def rdc():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/republique_democratique_du_congo.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="République Démocratique du Congo", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="République du Congo", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Kitts-et-Nevis", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def rd():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/republique_dominicaine.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Panama", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Dominique", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="République Dominicaine", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def rc():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/republique_du_congo.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="République Démocratique du Congo", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="République du Congo", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Kitts-et-Nevis", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def rt():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/republique_tcheque.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Philippines", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="République Tchèque", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Vanuatu", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def reu():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/reunion.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guyane Française", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Martinique", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Réunion", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def rou():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/roumanie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Tchad", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Roumanie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Moldavie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def rus():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/russie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Russie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Pays-Bas", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Luxembourg", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def rwa():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/rwanda.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Rwanda", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Palaos", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Lucie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sah():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/sahara_occidental.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Jordanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Sahara Occidental", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Algérie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sh():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/saint_hélène.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Sainte-Hélène", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Montserrat", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Îles Malouines", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sl():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/saint_lucie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Rwanda", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Palaos", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Sainte-Lucie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sk():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/Saint-Kitts-et-Nevis.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Trinité et Tobago", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="République Démocratique du Congo", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Kitts-et-Nevis", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sm():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/saint-marin.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Palaos", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Saint Marin", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Chypre", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sp():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/saint-pierre-et-miquelon.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guadeloupe", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Mayotte", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Pierre-et-Miquelon", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sv():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/saint-vincent_et_les_grenadines.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Saint-Vincent-et-les Grenadines", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Barbade", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Le Vatican", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sal():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/salvador.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Nicaragua", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guatemala", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Salvador", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sam():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/samoa.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Samoa", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Samoa Américain", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Taiwan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sama():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/samoa_américaines.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Samoa Américaines", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Samoa", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Vierges des Etats-Unis", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sao():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/sao_tomé_et_principe.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Guinée Biseau", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Sao Tomé-et-Principe", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Guinée équatoriale", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sen():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/senegal.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Sénégal", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Cameroun", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ghana", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ser():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/serbie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Slovénie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Serbie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="slovaquie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sey():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/seychelles.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Maurice", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Seychelles", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Marshall", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sie():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/sierra_leone.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Gambie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Lesotho", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Sierra Leone", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sin():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/singapour.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Indonésie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Singapour", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Pologne", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def slo():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/slovaquie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Serbie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Slovénie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Slovaquie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def slov():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/slovenie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Serbie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Slovaquie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Slovénie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def som():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/somalie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Somalie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="États Fédérés de Micronésie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Îles Mariannes du Nord", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sou():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/soudan.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Soudan du sud", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Soudan", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Jordanie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sri():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/sri_lanka.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Sri Lanka", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Bouthan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Népal", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sue():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/suede.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Finlande", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Suède", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Danemark", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sui():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/suisse.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Suisse", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Tonga", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Danemark", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sur():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/suriname.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Birmanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Burkina Faso ", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Suriname", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def jm():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/svalbard._jan_mayen.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Islande", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Féroé", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Svalbard Jan Mayen", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def esw():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/swaziland.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Eswatini", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Lesotho", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Sierra Leone", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def syr():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/syrie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iraq", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Syrie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Yemen", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tad():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/tadjikistan.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Tadjikistan", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iran", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Hongrie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tai():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/taiwan.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Samoa", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Hong Kong", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Taïwan", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tan():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/tanzanie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Tanzanie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="République du Congo", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Kitts-et-Nevis", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tch():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/tchad.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Roumanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Tchad", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Moldavie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def taf():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/terres_australes_francaises.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Terres Australes Françaises", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="France", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Polynésie Française", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tha():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/thailande.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Corrée du Nord", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Costa Rica", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Thaïlande", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tim():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/timor_oriental.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Timor Oriental", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guyana", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Vanuatu", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tog():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/togo.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Ghana", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Guinée-Bisseau", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Togo", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ton():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/tonga.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Tonga", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Suisse", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Malte", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tet():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/trinite_et_tobago.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Trinité-et-Tobago", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Tanzanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Saint-Kitts-et-Nevis", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tun():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/tunisie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Tunisie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Turquie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Libye", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tur():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/turkmenistan.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Pakistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Turkménistan", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ouzbékistan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def turq():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/turquie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Pakistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Turquie", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Tunisie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def tuv():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/tuvalu.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Fidji", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Iles Cook", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Tuvalu", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ukr():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ukraine.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Colombie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Ukraine", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Bosnie-Herzégovine", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def uru():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/uruguay.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Paraguay", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Argentine", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Uruguay", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def van():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/vanuatu.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Érythrée", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Afrique du Sud", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Vanuatu", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def ven():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/venezuela.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Équateur", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Venezuela", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Colombie", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def vie():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/vietnam.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Hong Kong", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Maroc", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Viet Nam", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def wal():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/wallis_et_futuna.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Wallis et Futuna", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="France", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Terres Australes Françaises", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def yem():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/yemen.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iraq", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Syrie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Yémen", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def zam():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/zambie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Turkménistan", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Zimbabwe", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Zambie", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def zim():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/zambie.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Comores", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Zimbabwe", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Mozambique", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def angl():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/angleterre.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Angleterre", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Géorgie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Irlande du Nord", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def pays():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/pays_de_galles.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Hongrie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Pays de Galles", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Bouthan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def irln():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/irlande_du_nord.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Iralnde du Nord", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Géorgie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Angleterre", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def eco():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/ecosse.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Burundi", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Jamaïque", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Ecosse", command=bon, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def kos():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/kosovo.PNG", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Cap-vert", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Kosovo", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Iles Cook", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
def sous():
    global feu
    global score
    global record
    feu = Tk()
    feu.configure(bg="black")
    feu.geometry(f"{feu.winfo_screenwidth()}x{feu.winfo_screenheight()}")
    feu.title("DREAPEAU")
    texte = Label(feu, text="QUEL EST LE PAYS DE CE DRAPEAU?", bg='black', fg="white")
    texte2 = Label(feu, text=f"VOTRE SCORE EST DE: {score}", bg='black', fg="white")
    texte3 = Label(feu, text=f"VOTRE RECORD EST {record}", bg='black', fg="white")
    texte4 = Label(feu, text="INSTA:lopysc7", bg="black", fg="white")
    img = PhotoImage(file="assets/soudan_du_sud.png", master=feu)
    label1 = Label(feu, image=img)
    choix1 = tk.Button(feu, text="Jordanie", command=faux, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix2 = tk.Button(feu, text="Soudan du Sud", command=bon, bg="black", fg='red', activebackground='cyan',width=feu.winfo_screenwidth())
    choix3 = tk.Button(feu, text="Soudan", command=faux, bg="black", fg='red',activebackground='cyan', width=feu.winfo_screenwidth())
    texte.pack()
    label1.pack()
    texte2.pack()
    texte3.pack()
    texte4.pack()
    choix1.pack()
    choix2.pack()
    choix3.pack()
    feu.mainloop()
v = random.randint(1,240)
if v == 1:
    print(afg())
elif v == 2:
     print(afr())
elif v == 3:
    print(alb())
elif v == 4:
    print(alg())
elif v == 5:
    print(al())
elif v == 6:
    print(an())
elif v == 7:
    print(ang())
elif v == 8:
    print(angu())
elif v == 9:
    print(ant())
elif v == 10:
    print(antn())
elif v == 11:
    print(ara())
elif v == 12:
    print(arg())
elif v == 13:
    print(arm())
elif v == 14:
    print(aru())
elif v == 15:
    print(aus())
elif v == 16:
    print(aut())
elif v == 17:
    print(az())
elif v == 18:
    print(baha())
elif v == 19:
    print(bah())
elif v == 20:
    print(ban())
elif v == 21:
    print(bar())
elif v == 22:
    print(bel())
elif v == 23:
    print(beli())
elif v == 24:
    print(ben())
elif v == 25:
    print(ber())
elif v == 26:
    print(bh())
elif v == 27:
    print(bie())
elif v == 28:
    print(bir())
elif v == 29:
    print(bol())
elif v == 30:
    print(bos())
elif v == 31:
    print(bot())
elif v == 32:
    print(bre())
elif v == 33:
    print(bru())
elif v == 34:
    print(bul())
elif v == 35:
    print(bur())
elif v == 36:
    print(bu())
elif v == 37:
    print(ca())
elif v == 38:
    print(cam())
elif v == 39:
    print(can())
elif v == 40:
    print(cap())
elif v == 41:
    print(ch())
elif v == 42:
    print(chi())
elif v == 43:
    print(chy())
elif v == 44:
    print(col())
elif v == 45:
    print(com())
elif v == 46:
    print(con())
elif v == 47:
    print(cos())
elif v == 48:
    print(co())
elif v == 49:
    print(cot())
elif v == 50:
    print(cro())
elif v == 51:
    print(cu())
elif v == 52:
    print(dan())
elif v == 53:
    print(dji())
elif v == 54:
    print(dom())
elif v == 55:
    print(eg())
elif v == 56:
    print(em())
elif v == 57:
    print(eq())
elif v == 58:
    print(er())
elif v == 59:
    print(es())
elif v == 60:
    print(est())
elif v == 61:
    print(efm())
elif v == 62:
    print(eu())
elif v == 63:
    print(et())
elif v == 64:
    print(fi())
elif v == 65:
    print(fin())
elif v == 66:
    print(fra())
elif v==67:
    print(ga())
elif v==68:
    print(gam())
elif v==69:
    print(geo())
elif v==70:
    print(geos())
elif v==71:
    print(gh())
elif v==72:
    print(gib())
elif v==73:
    print(gr())
elif v==74:
    print(gre())
elif v==75:
    print(gro())
elif v==76:
    print(gu())
elif v==77:
    print(gua())
elif v==78:
    print(guat())
elif v==79:
    print(gui())
elif v==80:
    print(gue())
elif v==81:
    print(gub())
elif v==82:
    print(guy())
elif v==83:
    print(guyf())
elif v==84:
    print(ha())
elif v==85:
    print(h())
elif v==86:
    print(ho())
elif v==87:
    print(hon())
elif v==88:
    print(ich())
elif v==89:
    print(ima())
elif v==90:
    print(ino())
elif v==91:
    print(ial())
elif v==92:
    print(ica())
elif v==93:
    print(ico())
elif v==94:
    print(ick())
elif v==95:
    print(ife())
elif v==96:
    print(iml())
elif v==97:
    print(imn())
elif v==98:
    print(imh())
elif v==99:
    print(ip())
elif v==100:
    print(isa())
elif v==101:
    print(itc())
elif v==102:
    print(ivb())
elif v==103:
    print(ivet())
elif v==104:
    print(ind())
elif v==105:
    print(indo())
elif v==106:
    print(ira())
elif v==107:
    print(iraq())
elif v==108:
    print(irl())
elif v==109:
    print(isl())
elif v==110:
    print(isr())
elif v==111:
    print(ita())
elif v==112:
    print(jam())
elif v==113:
    print(jap())
elif v==114:
    print(jor())
elif v==115:
    print(kaz())
elif v==116:
    print(ken())
elif v==117:
    print(kir())
elif v==118:
    print(kiri())
elif v==119:
    print(kow())
elif v==120:
    print(lao())
elif v==121:
    print(lev())
elif v==122:
    print(les())
elif v==123:
    print(let())
elif v==124:
    print(lib())
elif v==125:
    print(libe())
elif v==126:
    print(liby())
elif v==127:
    print(lie())
elif v==128:
    print(lit())
elif v==129:
    print(lux())
elif v==130:
    print(mac())
elif v==131:
    print(mad())
elif v==132:
    print(mal())
elif v==133:
    print(mala())
elif v==134:
    print(mald())
elif v==135:
    print(mali())
elif v==136:
    print(malt())
elif v==137:
    print(mar())
elif v==138:
    print(mart())
elif v==139:
    print(mau())
elif v==140:
    print(maur())
elif v==141:
    print(may())
elif v==142:
    print(mex())
elif v==143:
    print(mol())
elif v==144:
    print(mon())
elif v==145:
    print(mong())
elif v==146:
    print(mont())
elif v==147:
    print(monts())
elif v==148:
    print(moz())
elif v==149:
    print(nam())
elif v==150:
    print(nau())
elif v==151:
    print(nep())
elif v==152:
    print(nic())
elif v==153:
    print(nig())
elif v==154:
    print(nige())
elif v==155:
    print(niu())
elif v==156:
    print(nor())
elif v==157:
    print(nou())
elif v==158:
    print(nz())
elif v==159:
    print(oma())
elif v==160:
    print(oug())
elif v==161:
    print(ouz())
elif v==162:
    print(pak())
elif v==163:
    print(pal())
elif v==164:
    print(pan())
elif v==165:
    print(pap())
elif v==166:
    print(par())
elif v==167:
    print(pay())
elif v==168:
    print(per())
elif v==169:
    print(phi())
elif v==170:
    print(pol())
elif v==171:
    print(poly())
elif v==172:
    print(por())
elif v==173:
    print(port())
elif v==174:
    print(qat())
elif v==175:
    print(repc())
elif v==176:
    print(rdm())
elif v==177:
    print(rdc())
elif v==178:
    print(rd())
elif v==179:
    print(rc())
elif v==180:
    print(rt())
elif v==181:
    print(reu())
elif v==182:
    print(rou())
elif v==183:
    print(rus())
elif v==184:
    print(rwa())
elif v==185:
    print(sah())
elif v==186:
    print(sh())
elif v==187:
    print(sl())
elif v==188:
    print(sk())
elif v==189:
    print(sm())
elif v==190:
    print(sp())
elif v==191:
    print(sv())
elif v==192:
    print(sal())
elif v==193:
    print(sam())
elif v==194:
    print(sama())
elif v==195:
    print(sao())
elif v==196:
    print(sen())
elif v==197:
    print(ser())
elif v==198:
    print(sey())
elif v==199:
    print(sie())
elif v==200:
    print(sin())
elif v==201:
    print(slo())
elif v==202:
    print(slov())
elif v==203:
    print(som())
elif v==204:
    print(sou())
elif v==205:
    print(sri())
elif v==206:
    print(sue())
elif v==207:
    print(sui())
elif v==208:
    print(sur())
elif v==209:
    print(jm())
elif v==210:
    print(esw())
elif v==211:
    print(syr())
elif v==212:
    print(tad())
elif v==213:
    print(tai())
elif v==214:
    print(tan())
elif v==215:
    print(tch)
elif v==216:
    print(taf())
elif v==217:
    print(tha())
elif v==218:
    print(tim())
elif v==219:
    print(tog())
elif v==220:
    print(ton())
elif v==221:
    print(tet())
elif v==222:
    print(tun())
elif v==223:
    print(tur())
elif v==224:
    print(turq())
elif v==225:
    print(tuv())
elif v==226:
    print(ukr())
elif v==227:
    print(uru())
elif v==228:
    print(van())
elif v==229:
    print(ven())
elif v==230:
    print(vie())
elif v==231:
    print(wal())
elif v==232:
    print(yem())
elif v==233:
    print(zam())
elif v==234:
    print(zim())
elif v==235:
    print(angl())
elif v==236:
    print(pays())
elif v==237:
    print(irln())
elif v==238:
    print(eco())
elif v==239:
    print(kos())
elif v==240:
    print(sous())