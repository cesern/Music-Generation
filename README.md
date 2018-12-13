# Generando música de piano con RNN

Generador de música de piano con RNN y TensorFlow, fork de [Music-Generation](https://github.com/tarcisio-marinho/Music-Generation), entrena utilizando archivos MIDI y genera un archivo de salida mp3.

Puedes pasar como argumento el directorio con los archivos .mid, en caso de no hacerlo usara por default los archivos del directorio _input_. También puedes pasar el nombre del archivo que se generará, si no, se llamara output.

Aunque el poder de mi equipo de computo no es nada "potente" el proceso desde procesar los archivos MIDI hasta generar el mp3 fue bastante rápido. Con 173 archivos MIDI y 200 epoch, el tiempo fue de no mas de 12 minutos.

## Resultados
#### Generado con: 
https://github.com/cesern/Music-Generation/raw/master/results/Beatles.mp3
* [Musica Random](results/random.mp3)
[lol](https://github.com/cesern/Music-Generation/raw/master/results/Beatles.mp3)
* [Música de los Beatles](results/Beatles.mp3)
* [Música Pop](results/Pop.mp3)
* [Música de Johann Sebastian Bach, 9 ejemplos](results/bach9.mp3)
* [Música de Johann Sebastian Bach, 25 ejemplos](results/bach25.mp3)
* [Música de Johann Sebastian Bach, 50 ejemplos](results/bach50.mp3)
* [Música de Johann Sebastian Bach, 173 ejemplos](results/bachMod.mp3)

```
    python main.py -d <input_path> -o name_output_file
```
Se generara un archivo de salida en formato .mp3 para que puedas escucharlo!.

### Dependencias
```
    sudo apt-get install timidity

    sudo apt-get install ffmpeg

    sudo pip install python-midi numpy msgpack tqdm tensorflow

    sudo pip install msgpack
```    
### Uso
```
    usage: main.py [-h] [-d] [-o]

    Generate Piano music.

    optional arguments:
      -h, --help         Muestra este mensaje de salida y termina.
      -d , --directory   La musica para entrenar va aqui, si no se proporciona se utilizara la del directorio input
      -o , --output      El nombre del archivo de la musica de salida, si no se proporcona generará output.mp3
```
## Conclusiones
