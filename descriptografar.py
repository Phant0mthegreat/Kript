import cores as c

def Kript_PGT(frase):

      tradutor=""

      if frase=='':

        return f'\n[{c.yellow}@{c.white}] Ei, Você não digitou ↑'

      else:

       for letra in frase:

        if letra in "Ⅻ":

          tradutor=tradutor+" "

        elif letra in "Ⅷ":

          tradutor=tradutor+"a"

        elif letra in "♚":

          tradutor=tradutor+"A"

        elif letra in "⚁":

          tradutor=tradutor+"b"

        elif letra in "‽":

          tradutor=tradutor+"B"

        elif letra in "₫":

          tradutor=tradutor+"c"

        elif letra in "※":

          tradutor=tradutor+"C"

        elif letra in "Ξ":

          tradutor=tradutor+"d"

        elif letra in "ℼ":

          tradutor=tradutor+"D"

        elif letra in "Λ":

          tradutor=tradutor+"e"

        elif letra in "㎑":

          tradutor=tradutor+"E"

        elif letra in "˘":

          tradutor=tradutor+"f"

        elif letra in "⁈":

          tradutor=tradutor+"F"

        elif letra in "𓁋":

          tradutor=tradutor+"g"

        elif letra in "➬":

          tradutor=tradutor+"G"

        elif letra in "⎚":

          tradutor=tradutor+"h"

        elif letra in "𓆧":

          tradutor=tradutor+"H"

        elif letra in "☯":

          tradutor=tradutor+"i"

        elif letra in "✯":

          tradutor=tradutor+"I"

        elif letra in "‼":

          tradutor=tradutor+"j"

        elif letra in "𓇛":

          tradutor=tradutor+"J"

        elif letra in "☏":

          tradutor=tradutor+"k"

        elif letra in "⎋":

          tradutor=tradutor+"K"

        elif letra in "⌖":

          tradutor=tradutor+"l"

        elif letra in "𓂀":

          tradutor=tradutor+"K"

        elif letra in "☧":

          tradutor=tradutor+"m"

        elif letra in "✜":

          tradutor=tradutor+"M"

        elif letra in "✦":

          tradutor=tradutor+"n"

        elif letra in "✸":

          tradutor=tradutor+"N"

        elif letra in "⇖":

          tradutor=tradutor+"o"

        elif letra in "⇀":

          tradutor=tradutor+"O"

        elif letra in "⊞":

          tradutor=tradutor+"p"

        elif letra in "⊛":

          tradutor=tradutor+"P"

        elif letra in "☃":

          tradutor=tradutor+"q"

        elif letra in "☛":

          tradutor=tradutor+"Q"

        elif letra in "☹":

          tradutor=tradutor+"r"

        elif letra in "✐":

          tradutor=tradutor+"R"

        elif letra in "☊":

          tradutor=tradutor+"s"

        elif letra in "✂":

          tradutor=tradutor+"S"

        elif letra in "〠":

          tradutor=tradutor+"t"

        elif letra in "☬":

          tradutor=tradutor+"T"

        elif letra in "❂":

          tradutor=tradutor+"u"

        elif letra in "❐":

          tradutor=tradutor+"U"

        elif letra in "∴":

          tradutor=tradutor+"v"

        elif letra in "₪":

          tradutor=tradutor+"V"

        elif letra in "㊦":

          tradutor=tradutor+"w"

        elif letra in "𓆰":

          tradutor=tradutor+"W"

        elif letra in "☥":

          tradutor=tradutor+"x"

        elif letra in "✒":

          tradutor=tradutor+"X"

        elif letra in "♯":

          tradutor=tradutor+"y"

        elif letra in "⁂":

          tradutor=tradutor+"Y"

        elif letra in "♗":

          tradutor=tradutor+"z"

        elif letra in "☄":

          tradutor=tradutor+"Z"

        elif letra in "♞":

          tradutor=tradutor+"á"

        elif letra in "⌥":

          tradutor=tradutor+"à"

        elif letra in "⌦":

          tradutor=tradutor+"ã"

        elif letra in "⤦":

          tradutor=tradutor+"â"

        elif letra in "⤩":

          tradutor=tradutor+"Á"

        elif letra in "☪":

          tradutor=tradutor+"À"

        elif letra in "♅":

          tradutor=tradutor+"Ã"

        elif letra in "ლ":

          tradutor=tradutor+"Â"

        elif letra in "⌨":

          tradutor=tradutor+"ê"

        elif letra in "⍂":

          tradutor=tradutor+"é"

        elif letra in "⍑":

          tradutor=tradutor+"è"

        elif letra in "⍸":

          tradutor=tradutor+"Ê"

        elif letra in "⋬":

          tradutor=tradutor+"É"

        elif letra in "〄":

          tradutor=tradutor+"È"

        elif letra in "╍":

          tradutor=tradutor+"î"

        elif letra in "◓":

          tradutor=tradutor+"í"

        elif letra in "⑅":

          tradutor=tradutor+"Î"

        elif letra in "▪":

          tradutor=tradutor+"Í"

        elif letra in "〆":

          tradutor=tradutor+"ò"

        elif letra in "﹏":

          tradutor=tradutor+"ô"

        elif letra in "⑉":

          tradutor=tradutor+"õ"

        elif letra in "☲":

          tradutor=tradutor+"ó"

        elif letra in "☰":

          tradutor=tradutor+"Ò"

        elif letra in "☱":

          tradutor=tradutor+"Ô"

        elif letra in "☳":

          tradutor=tradutor+"Õ"

        elif letra in "☴":

          tradutor=tradutor+"Ó"

        elif letra in "☵":

          tradutor=tradutor+"ù"

        elif letra in "☶":

          tradutor=tradutor+"û"

        elif letra in "☷":

          tradutor=tradutor+"ú"

        elif letra in "❍":

          tradutor=tradutor+"Ù"

        elif letra in "☈":

          tradutor=tradutor+"Û"

        elif letra in "♨":

          tradutor=tradutor+"Ú"

        else:

          tradutor=tradutor+letra

       return f'\n[{c.yellow}÷{c.white}] Seu texto descriptografado ↓\n\n[{c.yellow}>>{c.white}] {tradutor}'
