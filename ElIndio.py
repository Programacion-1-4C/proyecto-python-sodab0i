import pyaudio
import wave
from PIL import Image
from colorama import Fore



def inforedondos():
    print('Patricio Rey y sus Redonditos de Ricota(conocidos tambien com los redondos)fueron un grupo musical '
          'argentino\nformado en la plata desde 1976 hasta 2004 inagurada por su excelente vocalista el Indio Solari,\n'
          ' Skay Beilison como su guitarrista, Semilla Bucciarelli como bajista, Walter Sidotti como baterista y '
          'Sergio\n Dawi como saxofonista, armonicista y pianista. Los redondos son considerados '
          'como una de las blandas más\n influyentes en la historia de la musica argentina ')


def cancionesredondas():
    lista_de_canciones = ['Un angel para tu soledad', 'Jijiji', 'Tarea Final', 'La bestia pop', 'Yo canibal']
    print(lista_de_canciones)
    analizar = input('En esta lista hay unas canciones de los Redondos ordenadas de mayor a menor segun su popularidad.'
                     'por favor escribe la que te parece interesante\n>>>')
    indice = lista_de_canciones.index(analizar)
    print('La cancion seleccionada es ', lista_de_canciones[indice], ', es eso correcto?')
    afirmar = input('>>>')
    if afirmar == 'si':
        if indice == 0:
            album = Image.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones '
                r'proyeto\Indio\Fotosalbum\Album0.jfif')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Indio'
                r'\cancion0apts.wav')

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
            album = Image.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones '
                r'proyeto\Indio\Fotosalbum\Album1.jfif')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Indio\cancion1jjj.wav')

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
            album = Image.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones '
                r'proyeto\Indio\Fotosalbum\Album2.jfif')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Indio\cancion2tf.wav')

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
            album = Image.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones '
                r'proyeto\Indio\Fotosalbum\Album3.jfif')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Indio\cancion3lbp.wav')

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
            album = Image.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones '
                r'proyeto\Indio\Fotosalbum\Album4.jfif')
            album.show()
            chunk = 1024
            f = wave.open(
                r'C:\Users\HORACIO CHIALVO\PycharmProjects\pythonProject\proyecto\canciones proyeto\Indio\cancion4yc.wav')

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
