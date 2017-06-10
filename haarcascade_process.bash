/usr/local/Cellar/opencv3/HEAD-2a5e12c/bin/opencv_createsamples -img 1.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1500 -bgcolor 0;

/usr/local/Cellar/opencv3/HEAD-2a5e12c/bin/opencv_createsamples -info info/info.lst -num 1500 -w 9 -h 20 -vec positives.vec;
/usr/local/Cellar/opencv3/HEAD-2a5e12c/bin/opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 2400 -numStages 10 -mode ALL -w 9 -h 20;