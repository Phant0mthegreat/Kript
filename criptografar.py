
import cores as c

def Kript_PGT(frase):

      tradutor=""

      if frase=='':

        return f'\n[{c.yellow}@{c.white}] Ei, Você não digitou ↑'

      else:

       for letra in frase:

        if letra in " ":

          tradutor=tradutor+"Ⅻ"

        elif letra in "a":

          tradutor=tradutor+"Ⅷ"

        elif letra in "A":

          tradutor=tradutor+"♚"

        elif letra in "b":

          tradutor=tradutor+"⚁"

        elif letra in "B":

          tradutor=tradutor+"‽"

        elif letra in "c":

          tradutor=tradutor+"₫"

        elif letra in "C":

          tradutor=tradutor+"※"

        elif letra in "d":

          tradutor=tradutor+"Ξ"

        elif letra in "D":

          tradutor=tradutor+"ℼ"

        elif letra in "e":

          tradutor=tradutor+"Λ"

        elif letra in "E":

          tradutor=tradutor+"㎑"

        elif letra in "f":

          tradutor=tradutor+"˘"

        elif letra in "F":

          tradutor=tradutor+"⁈"

        elif letra in "g":

          tradutor=tradutor+"𓁋"

        elif letra in "G":

          tradutor=tradutor+"➬"

        elif letra in "h":

          tradutor=tradutor+"⎚"

        elif letra in "H":

          tradutor=tradutor+"𓆧"

        elif letra in "i":

          tradutor=tradutor+"☯"

        elif letra in "I":

          tradutor=tradutor+"✯"

        elif letra in "j":

          tradutor=tradutor+"‼"

        elif letra in "J":

          tradutor=tradutor+"𓇛"

        elif letra in "k":

          tradutor=tradutor+"☏"

        elif letra in "K":

          tradutor=tradutor+"⎋"

        elif letra in "l":

          tradutor=tradutor+"⌖"

        elif letra in "L":

          tradutor=tradutor+"𓂀"

        elif letra in "m":

          tradutor=tradutor+"☧"

        elif letra in "M":

          tradutor=tradutor+"✜"

        elif letra in "n":

          tradutor=tradutor+"✦"

        elif letra in "N":

          tradutor=tradutor+"✸"

        elif letra in "o":

          tradutor=tradutor+"⇖"

        elif letra in "O":

          tradutor=tradutor+"⇀"

        elif letra in "p":

          tradutor=tradutor+"⊞"

        elif letra in "P":

          tradutor=tradutor+"⊛"

        elif letra in "q":

          tradutor=tradutor+"☃"

        elif letra in "Q":

          tradutor=tradutor+"☛"

        elif letra in "r":

          tradutor=tradutor+"☹"

        elif letra in "R":

          tradutor=tradutor+"✐"

        elif letra in "s":

          tradutor=tradutor+"☊"

        elif letra in "S":

          tradutor=tradutor+"✂"

        elif letra in "t":

          tradutor=tradutor+"〠"

        elif letra in "T":

          tradutor=tradutor+"☬"

        elif letra in "u":

          tradutor=tradutor+"❂"

        elif letra in "U":

          tradutor=tradutor+"❐"

        elif letra in "v":

          tradutor=tradutor+"∴"

        elif letra in "V":

          tradutor=tradutor+"₪"

        elif letra in "w":

          tradutor=tradutor+"㊦"

        elif letra in "W":

          tradutor=tradutor+"𓆰"

        elif letra in "x":

          tradutor=tradutor+"☥"

        elif letra in "X":

          tradutor=tradutor+"✒"

        elif letra in "y":

          tradutor=tradutor+"♯"

        elif letra in "Y":

          tradutor=tradutor+"⁂"

        elif letra in "z":

          tradutor=tradutor+"♗"

        elif letra in "Z":

          tradutor=tradutor+"☄"

        elif letra in "á":

          tradutor=tradutor+"♞"

        elif letra in "à":

          tradutor=tradutor+"⌥"

        elif letra in "ã":

          tradutor=tradutor+"⌦"

        elif letra in "â":

          tradutor=tradutor+"⤦"

        elif letra in "Á":

          tradutor=tradutor+"⤩"

        elif letra in "À":

          tradutor=tradutor+"☪"

        elif letra in "Ã":

          tradutor=tradutor+"♅"

        elif letra in "Â":

          tradutor=tradutor+"ლ"

        elif letra in "ê":

          tradutor=tradutor+"⌨"

        elif letra in "é":

          tradutor=tradutor+"⍂"

        elif letra in "è":

          tradutor=tradutor+"⍑"

        elif letra in "Ê":

          tradutor=tradutor+"⍸"

        elif letra in "É":

          tradutor=tradutor+"⋬"

        elif letra in "È":

          tradutor=tradutor+"〄"

        elif letra in "î":

          tradutor=tradutor+"╍"

        elif letra in "í":

          tradutor=tradutor+"◓"

        elif letra in "Î":

          tradutor=tradutor+"⑅"

        elif letra in "Í":

          tradutor=tradutor+"▪"

        elif letra in "ò":

          tradutor=tradutor+"〆"

        elif letra in "ô":

          tradutor=tradutor+"﹏"

        elif letra in "õ":

          tradutor=tradutor+"⑉"

        elif letra in "ó":

          tradutor=tradutor+"☲"

        elif letra in "Ò":

          tradutor=tradutor+"☰"

        elif letra in "Ô":

          tradutor=tradutor+"☱"

        elif letra in "Õ":

          tradutor=tradutor+"☳"

        elif letra in "Ó":

          tradutor=tradutor+"☴"

        elif letra in "ù":

          tradutor=tradutor+"☵"

        elif letra in "û":

          tradutor=tradutor+"☶"

        elif letra in "ú":

          tradutor=tradutor+"☷"

        elif letra in "Ù":

          tradutor=tradutor+"❍"

        elif letra in "Û":

          tradutor=tradutor+"☈"

        elif letra in "Ú":

          tradutor=tradutor+"♨"

        else:

          tradutor=tradutor+letra

       return f'\n[{c.yellow}÷{c.white}] Seu texto criptografado ↓\n\n[{c.yellow}>>{c.white}] {tradutor}'
