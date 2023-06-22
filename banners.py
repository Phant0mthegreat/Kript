from pystyle import Colorate, Colors
import banners, os, time

banner1="""      ██╗  ██╗██████╗ ██╗██████╗ ████████╗
      ██║ ██╔╝██╔══██╗██║██╔══██╗╚══██╔══╝
      █████╔╝ ██████╔╝██║██████╔╝   ██║   
      ██╔═██╗ ██╔══██╗██║██╔═══╝    ██║   
      ██║  ██╗██║  ██║██║██║        ██║   
      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                               """
def carregando():
  os.system('clear')
  print(Colorate.Vertical(Colors.red_to_yellow, '''



           ╔═════════════════════╗
           ║        Kript        ║
           ║     Carregando...   ║
           ╚═════════════════════╝
                                                               '''))
  time.sleep(3)
