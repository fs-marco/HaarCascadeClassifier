# HaarCascadeClassifier

Passos para a criação das imagens positivas e treinamento do cascade classifier.

1. Criar as imagens positivas
  /usr/local/Cellar/opencv3/HEAD-2a5e12c/bin/opencv_createsamples -img 1.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1500;
    -img: imagem positiva utilizada de exemplo
    -bg: arquivo descritivo das imagens de backgroud. Deve conter os caminhos para as imagens de background, normalmente dentro da pasta neg
    -info: arquivo que será gerado descrevendo as imagens positivas
    -pngoutput: quando ativo define que o arquivo info será gerado na seguinte forma (nome, quantidade de objetos e posição do objeto positiva na imagem)
    -maxyangle: Rotação máxima no eixo X da imagem exemplo para criação daspositivas em radianos
    -mayyangle: Rotação máxima no eixo Y da imagem exemplo para criação daspositivas em radianos
    -mazyangle: Rotação máxima no eixo Z da imagem exemplo para criação daspositivas em radianos
    -num: quantidade de imagens a serem criadas

2. Criar o vetor "positives.vec" das imagens positivas
  /usr/local/Cellar/opencv3/HEAD-2a5e12c/bin/opencv_createsamples -info info/info.lst -num 1500 -w 9 -h 20 -vec positives.vec;
    -info: arquivo gerado no passo 1.
    -num: numeros de imagens positivas que o arquivo descreve
    -w: largura em pixels das imagens de saída
    -h: altura em pixels das imagens de saída
    -vec: vector resultante das imagens positivas
 
3. Treinar o cascade classifier
  /usr/local/Cellar/opencv3/HEAD-2a5e12c/bin/opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 2400 -numStages 10 -mode ALL -w 9 -h 20;
    -data: diretório onde serão salvos os estágios e o classificador final (xml)
    -vec: vector gerado em 2
    -bg: arquivo descritivo das imagens de backgroud. Deve conter os caminhos para as imagens de background, normalmente dentro da pasta neg
    -numPos: número de imagens positivas
    -numNeg: número de imagens negativas
    -numStages: quantidade de estágios de treinamento
    -mode: modo de treinamento
