from pyfacy import face_clust
import os

class Clusterizacao:
    
    PASTA_COM_CLUSTERS = 'clusters'
    
    def cluster(self, de_pasta, para_pasta=PASTA_COM_CLUSTERS):
        if not os.path.exists(de_pasta):
            print('[ERRO] O caminho ' + de_pasta + ' não existe ou não foi encontrado')
            return False
        
        if not os.path.exists(para_pasta):
            os.makedirs(para_pasta)

        try:
            
            if len(os.listdir(de_pasta)) > 0:
                                
                cluster = face_clust.Face_Clust_Algorithm(de_pasta)
                cluster.load_faces()
                cluster.save_faces(para_pasta)

            else:
                print('[INFO] Não há arquivos para clusterizar')
        except:
            print('[ERRO] Ocorreu um erro ao clusterizar os arquivos da pasta ' + de_pasta)
            return False

        return True
            