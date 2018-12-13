import os
import miditomp3
import numpy as np
import msgpack
import midi_manipulation
import neuralnet
import sys
import merge
import argparse

parser = argparse.ArgumentParser(description='Generate Piano music.')
parser.add_argument('-d', '--directory', type = str, required = False, metavar = '',  help = 'the music to be trained should be inside this dir, if not specified, EDEN-midi will be the input')
parser.add_argument('-o', '--output', type = str, required = False, metavar = '',  help = 'Output music as an .mp3 file, if not specified, will be output.mp3')
args = parser.parse_args()


def get_files(path):
    songs = []
    for a, b, c in os.walk(path):
        for f in c:
            song = os.path.join(a, f)
            try:
                n = np.array(midi_manipulation.midiToNoteStateMatrix(song))
                songs.append(n)
            except Exception as e:
                print("error: {} on file: {}".format(e, f))
            
    return songs



if __name__ == "__main__":
    
    #directorio para los midis de entrada por default
    path = "input"
    #el nombre de la salida por default
    output = "output"
    #toma el path de la entrada si es que se proporciona
    if(args.directory):
        path = args.directory
    #toma el nombre de la salida si es que se proporciona
    if(args.output):
        output = args.output
    #obtiene las canciones en midi    
    songs = get_files(path)

    if(not os.path.isdir("generated")):
        os.mkdir("generated")

    neuralnet.menu(songs)
    #crea la cancion
    merge.menu(output)