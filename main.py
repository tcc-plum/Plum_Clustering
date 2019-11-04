from clusterizacao import Clusterizacao
import time
import os

pasta = '../Plum_Research/frames'
clusterizar = Clusterizacao()

while True:
    arquivos = os.listdir(pasta)
    clusterizar.cluster(pasta)
    for arquivo in arquivos:
        foto = pasta + '/' + arquivo
        if os.path.isfile(foto):
            print('[INFO] Removendo o arquivo: ' + foto)
            os.remove(foto)
    time.sleep(5)
