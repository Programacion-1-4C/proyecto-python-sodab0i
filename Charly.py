import pyaudio
import wave
from PIL import Image
from colorama import Fore


def infocharly():
    print(Fore.BLUE+'Carlos Alberto Garcia, mejor conocido por su pseudonimo artisico como Charley Garcia es un cantautor '
          'argentino nacido el 23 de octubre de 1951 en la Ciudad Autonoma de Buenos Aires. Si bien es cierto que'
          'Charley fue parte de grandes bandas en el pasado como Sui Generis o la maquina de hacer pajaros nosotros yo'
          'me concentrare en la etapa más emblematica de su carrera que es cuando cantaba solo.')


def canciones1():
    lista_canciones1 = ['Nos siguen golpeando abajo', 'Demoliendo hoteles', 'Hablando a tu coranzon', 'Tu amor',
                        'No me dejan sair']
    print(lista_canciones1)
    analizar = input('En esta lista hay unas canciones de charley ordenadas de mayor a menor segun su popularidad.'
                     'por favor escribe la que te parece interesante\n>>>')

    indice = lista_canciones1.index(analizar)
    print('La cancion seleccionada es ', lista_canciones1[indice], ', es eso correcto?')
    afirmar = input('>>>')
    if afirmar == 'si':
        if indice == 0:
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\fotos '
                               r'album\fotoAlbumCharlynspa.jpg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\CharlyGarcíaNosSiguenPegandoAbajoAudio.wav',
                'rb')

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
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\fotos '
                               r'album\fotoalbumCharlydh.png')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\Charly García  Demoliendo Hoteles Audio.wav',
                'rb')
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
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\fotos '
                               r'album\fotoAlbumCharlyhtc.jpg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\Hablando a Tu Corazón Official Audio.wav',
                'rb')
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
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\fotos '
                               r'album\fotoAlbumCharlyta.jpg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\Tu Amor Official Audio.wav',
                'rb')
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
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\fotos '
                               r'album\fotoAlbumCharlynspa.jpg.jpg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Charly\ No Me Dejan Salir Audio.wav',
                'rb')
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
