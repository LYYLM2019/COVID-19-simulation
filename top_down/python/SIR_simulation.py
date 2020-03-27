####################################
#simulazione secondo il sistema SIR#
####################################
import matplotlib.pyplot as pl
popolation = 60000000 #popolazione iniziale uguale a circa la popolazione italiana
s = popolation #sani
i = 1 #infetti
r = 0 #rimossi
a = 0.0724 #costante di infettività del virus
b = 0.063 #efficienza del nostro sistema sanitario
Ro = (a/b)*s
print("popolazione iniziale:" + str(popolation))
print("Ro inziale:" + str(Ro))

tempo = 0 
S_s = []
I_s = []
R_s = []
Ro_s = []
time = []

while True:
    if tempo >100:
        break
    I_prev = i
    S_prev = s
    R_prev = r
    s = s - (a*I_prev*S_prev*tempo)/popolation
    i = i + a*I_prev*S_prev*tempo/popolation - b*I_prev*tempo
    r = r + b*I_prev*tempo
    Ro = (a/b)*s
    S_s.append(s)
    I_s.append(i)
    R_s.append(r)
    Ro_s.append(Ro)
    time.append(tempo)
    pl.plot(s, tempo, color='green')
    pl.plot(i, tempo, color='red')
    pl.plot(r, tempo, color='black')
    pl.plot(Ro, tempo, color='yellow')
    print("tempo " + str(tempo))
    print("infetti:" + str(i))
    print("sani:" + str(s))
    print("rimossi:" + str(r))
    print("Ro:" + str(Ro))
    print()
    tempo = tempo + 1
pl.axis([0,tempo,0,1000000])
#pl.plot(time, S_s, color='green')
pl.plot(time, I_s, time, color='red')
#pl.plot(time, R_s, time, color='black')
#pl.plot(time, Ro_s, color='yellow')
pl.show()
