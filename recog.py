import cv2 as cv
# import cv2
# path = '/Users/marco/Documents/Desenvolvimento/Python2.7/visao_computacional/controle&relogio_v1.mp4'
# face_cascade = cv.CascadeClassifier('xmlFiles/haarcascade_frontalface_default.xml')

# cap = cv.VideoCapture('/Users/marco/Documents/Faculdade/7o.Semestre/Trabalho-CG/haarcascade/video.mp4')
# cap = cv.VideoCapture('/Users/marco/Documents/Faculdade/7o.Semestre/Trabalho-CG/Base-de-Dados/TODDYNHO.mov')


toddy_cascade = cv.CascadeClassifier('toddy/data/cascade.xml')

relogio_cascade = cv.CascadeClassifier('relogio/data/cascade.xml')
controle_cascade = cv.CascadeClassifier('controle/data/cascade.xml')
bauducco_cascade = cv.CascadeClassifier('bauducco/data/cascade.xml')
bis_cascade = cv.CascadeClassifier('bis/data/cascade.xml')
sucrilhos_cascade = cv.CascadeClassifier('sucrilhos/data/cascade.xml')
diamante_cascade = cv.CascadeClassifier('diamantenegro/Diamante/data/cascade.xml')


def test_img(path_tests):
    import os
    images = os.listdir(path_tests + '/')
    i = 0
    for img_name in images:
        print path_tests+img_name
        img = cv.imread(path_tests+img_name)
        # cv.imshow('frame', img)
        # k = cv.waitKey(30000)
        # gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        font = cv.FONT_HERSHEY_SIMPLEX
        # cap = cv.VideoCapture('/Users/marco/Documents/Faculdade/7o.Semestre/Trabalho-CG/haarcascade/video.mp4')
        # while True:
        # ret, img = cap.read()
        # img = cv.resize(img, (img.shape[1] / 4, img.shape[0] / 4))
        gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        # frame = cv.resize(gray, (956, 618))
        relogio = relogio_cascade.detectMultiScale(gray)
        # controle = controle_cascade.detectMultiScale(gray)
        bauducco = bauducco_cascade.detectMultiScale(gray)
        bis = bis_cascade.detectMultiScale(gray)
        sucrilhos = sucrilhos_cascade.detectMultiScale(gray, minNeighbors=10)
        toddy = toddy_cascade.detectMultiScale(gray, minNeighbors=15)
        diamante = diamante_cascade.detectMultiScale(gray)

        for (x, y, w, h) in toddy:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.putText(img, 'TODDYNHO', (x, y), font, 0.5, (255, 0, 0), 2, cv.LINE_AA)

        # for (x, y, w, h) in controle:
        #     cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #     cv.putText(img, 'controle', (x, y), font, 0.5, (0, 0, 255), 2, cv.LINE_AA)

        for (x, y, w, h) in relogio:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv.putText(img, 'relogio', (x, y), font, 0.5, (0, 255, 255), 2, cv.LINE_AA)

        for (x, y, w, h) in bauducco:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv.putText(img, 'bauducco', (x, y), font, 0.5, (255, 0, 255), 2, cv.LINE_AA)

        for (x, y, w, h) in bis:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv.putText(img, 'bis', (x, y), font, 0.5, (255, 255, 0), 2, cv.LINE_AA)

        for (x, y, w, h) in sucrilhos:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv.putText(img, 'sucrilhos', (x, y), font, 0.5, (255, 255, 0), 2, cv.LINE_AA)

        for (x, y, w, h) in diamante:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv.putText(img, 'diamante', (x, y), font, 0.5, (100, 205, 0), 2, cv.LINE_AA)

        cv.imshow('frame', img)
        k = cv.waitKey(30000)
        if k == 27:
            cv.destroyAllWindows()
#     break
# cap.release()
# cv.destroyAllWindows()


def test_live():
    video_result = cv.VideoWriter('result.avi', cv.VideoWriter_fourcc('M','J','P','G'), 5, (1280, 720))

    # fourcc = cv.VideoWriter_fourcc(*'XVID')
    # out = cv.VideoWriter('output.avi', fourcc, 20.0, (img.shape[1], img.shape[0]))

    cap = cv.VideoCapture(0)
    while True:
        ret, img = cap.read()
        font = cv.FONT_HERSHEY_SIMPLEX
        gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        # sucrilhos = sucrilhos_cascade.detectMultiScale(gray, minNeighbors=12)
        # relogio = relogio_cascade.detectMultiScale(gray)
        # diamante = diamante_cascade.detectMultiScale(gray,  minNeighbors=8)
        # bauducco = bauducco_cascade.detectMultiScale(gray, minNeighbors=8)
        # toddy = toddy_cascade.detectMultiScale(gray, minNeighbors=15)
        controle = controle_cascade.detectMultiScale(gray, minNeighbors=15)



        for (x, y, w, h) in controle:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 100, 20), 2)
            cv.putText(img, 'controle', (x, y), font, 0.5, (255, 100, 20), 2, cv.LINE_AA)

        #
        # for (x, y, w, h) in toddy:
        #     cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #     cv.putText(img, 'TODDYNHO', (x, y), font, 0.5, (255, 0, 0), 2, cv.LINE_AA)
        #
        #
        # for (x, y, w, h) in relogio:
        #     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        #     cv.putText(img, 'relogio', (x, y), font, 0.5, (0, 255, 255), 2, cv.LINE_AA)
        #
        # for (x, y, w, h) in bauducco:
        #     cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        #     cv.putText(img, 'bauducco', (x, y), font, 0.5, (255, 0, 255), 2, cv.LINE_AA)
        #
        # for (x, y, w, h) in sucrilhos:
        #     cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        #     cv.putText(img, 'sucrilhos', (x, y), font, 0.5, (255, 255, 0), 2, cv.LINE_AA)
        #
        # for (x, y, w, h) in diamante:
        #     cv.rectangle(img, (x, y), (x + w, y + h), (155, 205, 0), 2)
        #     cv.putText(img, 'DIAMANTE', (x, y), font, 0.5, (155, 205, 0), 2, cv.LINE_AA)
        cv.imshow('img', img)

        # try:
            # print img.shape[1], img.shape[0]
            # out.write(img)
            # video_result.write(img)
        # except Exception as e:
        #     print e.message
        k = cv.waitKey(30 & 0xff)
        if k == 27:
            break
    cv.destroyAllWindows()


def test_video():
    video_result = cv.VideoWriter('result.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 5, (1280, 720))

    dorflex_cascade = cv.CascadeClassifier('dorflex/data/cascade.xml')
    fabercastel_cascade = cv.CascadeClassifier('fabercastel/data/cascade.xml')
    guaravito_cascade = cv.CascadeClassifier('guaravito/data/cascade.xml')
    fanta_cascade = cv.CascadeClassifier('fanta/data/cascade.xml')
    brahma_cascade = cv.CascadeClassifier('brahma/data/cascade.xml')
    bioleve_cascade = cv.CascadeClassifier('bioleve/data/cascade.xml')
    ck_cascade = cv.CascadeClassifier('CK/data/cascade.xml')
    polenguinho_cascade = cv.CascadeClassifier('polenguinho/data/cascade.xml')
    italac_cascade = cv.CascadeClassifier('italac/data/cascade.xml')

    cap = cv.VideoCapture("./video_test.mp4")
    font = cv.FONT_HERSHEY_SIMPLEX
    while True:
        if cap.grab():

            flag, img = cap.retrieve()
            gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

            dorflex = dorflex_cascade.detectMultiScale(gray, minNeighbors=15, minSize=(30, 50))
            fabercastel = fabercastel_cascade.detectMultiScale(gray)
            fanta = fanta_cascade.detectMultiScale(gray, minNeighbors=6)
            guaravito = guaravito_cascade.detectMultiScale(gray)
            brahma = brahma_cascade.detectMultiScale(gray)
            polenguinho = polenguinho_cascade.detectMultiScale(gray, minNeighbors=7)
            # italac = italac_cascade.detectMultiScale(gray)

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

            # for (x, y, w, h) in italac:
            #     cv.rectangle(img, (x, y), (x + w, y + h), (123, 100, 70), 2)
            #     cv.putText(img, 'italac', (x, y), font, 0.5, (230, 255, 70), 2, cv.LINE_AA)
            #     print 'italac'

            if not flag:
                continue
            else:
                try:
                    # print img.shape[1], img.shape[0]
                    video_result.write(img)
                except Exception as e:
                    print e.message
                cv.imshow('resultado_RESULTADO', img)
        if cv.waitKey(30 & 0xff) == 27:
            break

# test_img('test_images/')
# test_live()
test_video()