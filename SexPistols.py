import pyaudio
import wave
from PIL import Image
from colorama import Fore


def infopistols():
    print(Fore.RED+'Sex Pistols fue una banda de punk inglesa formada en Londres en 1975. A pesar que solo duraron 2 años \n'
          'juntos como banda, fueron los responsables de iniciar el movimiento punk en el Reino Unido he inspirar a \n'
          'los futuros artistas punk y de rock alternativo. Ellos introdujeron los cabellos que se asocian al \n'
          'anarquismo en el punk mismo, su canción God Save the Queen fue tan controversial que no solo la BBC \n'
          'prohibio su reproducción sino tambien varias radios independientes. A pesar de todo esto, son una de las \n'
          'bandas más influyentes en el mundo del punk.')

def cancionespistols():
    lista_canciones = ['Anarchy in the UK', 'God Save the Queen', 'Pretty Vacant', 'Hollyday in the Sun', 'Bodies']
    print(lista_canciones)
    print('En esta lista hay una serie de canciones de Sex Pistols disponibles. Por favor selecciona una para escuchar')
    analizar = input('>>>')
    indice = lista_canciones.index(analizar)
    print('La cancion selccionada fue ', lista_canciones[indice], ' es eso correcto?')
    afirmar = input('>>>')
    if afirmar == 'si':
        album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Pistols\ELalbumpistol\ELalbum.png')
        album.show()
        if indice == 0:
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Pistols\cancion0auk.wav')

            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)
            data = f.readframes(chunk)
            while data:
                stream.write(data)
                data = f.readframes(chunk)
        if indice == 1:
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Pistols\cancion1gsq.wav')

            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)
            data = f.readframes(chunk)
            while data:
                stream.write(data)
                data = f.readframes(chunk)
        if indice == 2:
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Pistols\cancion2pv.wav')

            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)
            data = f.readframes(chunk)
            while data:
                stream.write(data)
                data = f.readframes(chunk)
        if indice == 3:
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Pistols\cancion3hs.wav')

            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)
            data = f.readframes(chunk)
            while data:
                stream.write(data)
                data = f.readframes(chunk)
        if indice == 4:
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Pistols\cancion4b.wav')

            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True)
            data = f.readframes(chunk)
            while data:
                stream.write(data)
                data = f.readframes(chunk)
    elif afirmar == 'no':
        print('por favor repeti el proceso')
        breakpoint()
