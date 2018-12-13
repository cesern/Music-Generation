# Piano Music Generation con RNN y tensorflow

Generador de música de piano basado en archivos .mid.

Puedes pasar como argumento el directorio con los archivos .mid, en caso de no hacerlo usara por default los archivos del directorio _input_. También puedes pasar el nombre del archivo que se generará, si no, se llamara output.

```
    python main.py -d <input_path> -o name_output_file
```
Se generara un archivo de salida en formato .mp3 para que puedas escucharlo!.

## Dependencias
```
    sudo apt-get install timidity

    sudo apt-get install ffmpeg

    sudo pip install python-midi numpy msgpack tqdm tensorflow

    sudo pip install msgpack
```    
# Usage
```
    usage: main.py [-h] [-d] [-o]

    Generate Piano music.

    optional arguments:
      -h, --help         show this help message and exit
      -d , --directory   the music to be trained should be inside this dir, if not
                         specified, EDEN-midi will be the input
      -o , --output      Output music as an .mp3 file, if not specified, will be
                         output.mp3
```
