import cv2 as cv


def test_video(video = './video_test.mp4'):
    """Aplica cascade classifiers em um video"""

    # VideoWriter oara salvar os resultados
    video_result = cv.VideoWriter("result.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 5, (1280, 720))

    # Inicia os cascades classifiers
    dorflex_cascade = cv.CascadeClassifier('dorflex/data/cascade.xml')
    fabercastel_cascade = cv.CascadeClassifier('fabercastel/data/cascade.xml')
    guaravito_cascade = cv.CascadeClassifier('guaravito/data/cascade.xml')
    fanta_cascade = cv.CascadeClassifier('fanta/data/cascade.xml')
    brahma_cascade = cv.CascadeClassifier('brahma/data/cascade.xml')
    bioleve_cascade = cv.CascadeClassifier('bioleve/data/cascade.xml')
    ck_cascade = cv.CascadeClassifier('CK/data/cascade.xml')
    polenguinho_cascade = cv.CascadeClassifier('polenguinho/data/cascade.xml')
    italac_cascade = cv.CascadeClassifier('italac/data/cascade.xml')

    # Inicia leitura do video
    cap = cv.VideoCapture(video)
    font = cv.FONT_HERSHEY_SIMPLEX

    # Loop que aplicara os classificadores em todos os frames do video
    while True:
        if cap.grab():

            flag, img = cap.retrieve()
            gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

            # Busca os objetos de cada classificador no frame atual do video
            dorflex = dorflex_cascade.detectMultiScale(gray, minNeighbors=15, minSize=(30, 50))
            fabercastel = fabercastel_cascade.detectMultiScale(gray)
            fanta = fanta_cascade.detectMultiScale(gray, minNeighbors=6)
            guaravito = guaravito_cascade.detectMultiScale(gray)
            brahma = brahma_cascade.detectMultiScale(gray)
            polenguinho = polenguinho_cascade.detectMultiScale(gray, minNeighbors=7)

            # Desenha o retangulo do local onde o objeto foi encontrado junto com um label
            for (x, y, w, h) in dorflex:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.putText(img, 'dorflex', (x, y), font, 0.5, (255, 0, 0), 2, cv.LINE_AA)

            for (x, y, w, h) in fabercastel:
                cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv.putText(img, 'fabercastel', (x, y), font, 0.5, (0, 255, 0), 2, cv.LINE_AA)

            for (x, y, w, h) in fanta:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                cv.putText(img, 'fanta', (x, y), font, 0.5, (255, 0, 255), 2, cv.LINE_AA)

            for (x, y, w, h) in guaravito:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                cv.putText(img, 'guaravito', (x, y), font, 0.5, (255, 255, 0), 2, cv.LINE_AA)

            for (x, y, w, h) in brahma:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                cv.putText(img, 'brahma', (x, y), font, 0.5, (255, 255, 0), 2, cv.LINE_AA)

            for (x, y, w, h) in polenguinho:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 205, 40), 2)
                cv.putText(img, 'polenguinho', (x, y), font, 0.5, (255, 205, 40), 2, cv.LINE_AA)


            if not flag:
                continue
            else:
                try:
                    # grava o frame resultante com os retangulos
                    video_result.write(img)
                except Exception as e:
                    print e.message
                cv.imshow('resultado_RESULTADO', img)
        if cv.waitKey(30 & 0xff) == 27:
            break

test_video()