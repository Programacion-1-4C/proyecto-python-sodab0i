from Charly import infocharly, canciones1
from ElIndio import inforedondos, cancionesredondas
from LaRenga import cancionesrenga, larengainfo
from SexPistols import infopistols, cancionespistols
from colorama import Fore


print(Fore.RED+'          _____                   _______                   _____            _____          \n'
      '         /\    \                 /::\    \                 /\    \          /\    \         \n'
      '        /::\____\               /::::\    \               /::\____\        /::\    \        \n'
      '       /:::/    /              /::::::\    \             /:::/    /       /::::\    \       \n'
      '      /:::/    /              /::::::::\    \           /:::/    /       /::::::\    \      \n'
      '     /:::/    /              /:::/  \:::\    \         /:::/    /       /:::/\:::\    \     \n'
      '    /:::/____/              /:::/    \:::\    \       /:::/    /       /:::/__\:::\    \    \n'
      '   /::::\    \             /:::/    / \:::\    \     /:::/    /       /::::\   \:::\    \   \n'
      '  /::::::\    \   _____   /:::/____/   \:::\____\   /:::/    /       /::::::\   \:::\    \  \n'
      ' /:::/\:::\    \ /\    \ |:::|    |     |:::|    | /:::/    /       /:::/\:::\   \:::\    \ \n'
      '/:::/  \:::\    /::\____\|:::|____|     |:::|    |/:::/____/       /:::/  \:::\   \:::\____\ \n'
      '\::/    \:::\  /:::/    / \:::\    \   /:::/    / \:::\    \       \::/    \:::\  /:::/    /\n'
      ' \/____/ \:::\/:::/    /   \:::\    \ /:::/    /   \:::\    \       \/____/ \:::\/:::/    / \n'
      '          \::::::/    /     \:::\    /:::/    /     \:::\    \               \::::::/    /  \n'
      '           \::::/    /       \:::\__/:::/    /       \:::\    \               \::::/    /   \n'
      '           /:::/    /         \::::::::/    /         \:::\    \              /:::/    /    \n'
      '          /:::/    /           \::::::/    /           \:::\    \            /:::/    /     \n'
      '         /:::/    /             \::::/    /             \:::\    \          /:::/    /      \n'
      '        /:::/    /               \::/____/               \:::\____\        /:::/    /       \n'
      '        \::/    /                                         \::/    /        \::/    /        \n'
      '         \/____/                                           \/____/          \/____/         \n')
print(Fore.GREEN+'Este codigo sirve para saber la discografia de Charly Garcia (1), Patricio Rey y sus Redonditos de Ricota (2)'
      ', La Renga(3), Sex Pistols(4)')
print('Por favor decime de quien queres saber con el numer que tenes al lado de cada nombre')
respuesta = input('>>>')
if respuesta == '1':
    infocharly()
    canciones1()
if respuesta == '2':
    inforedondos()
    cancionesredondas()
if respuesta == '3':
    larengainfo()
    cancionesrenga()
if respuesta == '4':
    infopistols()
    cancionespistols()
