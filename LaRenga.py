import pyaudio
import wave
from PIL import Image
from colorama import Fore


def larengainfo():
    print(Fore.LIGHTMAGENTA_EX+'La Renga es un grupo de hard rock argentina formado en CABA en el barrio de mataderos en 1988. Integrda por\n'
          'Gustavo Nápoli o Chizzo Nápoli como su cantante y guitarrista principal, Gabriel Igleasias o Tete como \n'
          'bajista y Jorge Iglesias o Tanque como su baterista desde sus inicios mientras que Manuel Varela se unio '
          'en\n '
          '1994. Su carrera se baso en la autogestión de la banda por los mismos integrantes y en 2002 contaban con\n'
          'su propio sello discografico\n')
def cancionesrenga():
    lista_canciones = ['Balada del diablo y la muerte', 'El terco', 'El revelde', 'Vende patria clon',
                       'El final es donde parti']
    print(lista_canciones)
    print('En esta lista hay una serie de canciones de la Renga. Por favor seleccione la que quiere escuchar')
    analizar = input('>>>')
    indice = lista_canciones.index(analizar)
    print('La cancion selccionada fue ', lista_canciones[indice], ' es eso correcto?')
    afirmar = input('>>>')
    if afirmar == 'si':
        if indice == 0:
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones '
                               r'proyeto\Renga\Albumrenga\Album0.jpeg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones '
                r'proyeto\Renga\cancion0bdm.wav')

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
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones '
                               r'proyeto\Renga\Albumrenga\Album1.jpg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Renga\cancion1t.wav')

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
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Renga\Albumrenga\Album1.jpg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Renga\cancion2r.wav')

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
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Renga\Albumrenga\Album1.jpg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Renga\cancion3vpc.wav')

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
            album = Image.open(r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Renga\Albumrenga\Album0.jpeg')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Renga\cancion4fdp.wav')

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
