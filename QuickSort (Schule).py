
a = int(input("Anzahl der zu Sortierenden Zahlen: "))

dt = []

print("Anzahl:", a)

for i in range(0,a):                                    #Erstellen der zu sortierenden Liste
    dt.append(int(input("Zahl: ")))

print(dt)


def qS(dt):                                             #Liste dt wird mit ihrer Länge - 1 übergeben
    qSH(dt, 0, len(dt) - 1)


def qSH(dt, first, last):
    if first < last:

        sp = qSP(dt, first, last)                       #SplitPoint wird bestimmt durch Liste und Grenzwerten

        qSH(dt, first, sp - 1)                          #First wird wieder PP, mit verändertem last-Grenzwert
        qSH(dt, sp + 1, last)                           #rm+1 wird zum PP mit gleichen last-Grenzwert



def qSP(dt, first, last):
    pp = dt[first]
    print("Pivot Point:",pp)

    lm = first + 1
    rm = last

    print(lm)
    print(rm)

    done = False

    while not done:

        while lm <= rm and dt[lm] <= pp:                #Links und Rechts des PP wird miteinander vergliechen
            lm = lm + 1                                 #Bis und im Falle einer falschen Bedingung wird lm und rm
        while rm >= lm and dt[rm] >= pp:                #In der else-Schleife mit einander getauscht bis rm < lm
            rm = rm - 1

        if rm < lm:
            done = True

        else:
            tm = dt[lm]
            dt[lm] = dt[rm]
            dt[rm] = tm

    tm = dt[first]                                      #Sobald rm < lm, wird "first" und "rm" vertauscht
    dt[first] = dt[rm]
    dt[rm] = tm

    return rm




qS(dt)
print(dt)
