import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import cv2
import shutil
import os

class Watcher:
    
    DIRECTORY_TO_WATCH = '../Plum_Research/frames'

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            
            face = DetectFaces()
            
            try:
                if(face.detect(event.src_path)):
                    print('Rosto detectado no arquivo - {}'.format(event.src_path))
                    shutil.move(event.src_path, 'clusters')
                else:
                    print('Nenhum rosto detectado no arquivo - {}'.format(event.src_path))
                    if os.path.isfile(event.src_path):
                        print('[INFO] Removendo o arquivo - {}'.format(event.src_path))
                        os.remove(event.src_path)
            except:
                print('[ERRO] Não foi possível mover arquivo para a clusterização')
                if os.path.isfile(event.src_path):
                    print('[INFO] Removendo o arquivo - {}'.format(event.src_path))
                    os.remove(event.src_path)

class DetectFaces:
    
    def detect(self, image):
        classificador_facial = cv2.CascadeClassifier('modelo/haarcascade_frontalface_default.xml')
        image_to_classify = cv2.imread(image)
        min_size = (image_to_classify.shape[1], image_to_classify.shape[0])
        min_frame = cv2.resize(image_to_classify, min_size)
        detected_faces = classificador_facial.detectMultiScale(min_frame)
        for face in detected_faces:
            x_axis, y_axis, width, height = [vertice for vertice in face]
            sub_face = image_to_classify[y_axis:y_axis+height, x_axis:x_axis+width]
            return True
        return False