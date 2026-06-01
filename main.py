# Passo 0: Imports necessários para o processo de visão computacional e delimitação das caixas de visualização (bounding boxes)

#OpenCV para captura e pré-processamento
import cv2
#NumPy, dependência implícita para representação das coordenadas enquanto parte de matrizes
import numpy as np
#MediaPipe, framework para detecção, isolamento e classificação do objeto alvo
import mediapipe as mp
from mediapipe.tasks import python 
from mediapipe.tasks.python import vision 

# Passo 1: definição das configurações de detecção e filtragem para detectar a bola de futebol, enquadrada na categoria 
# 'sports ball' abaixo
base_options = python.BaseOptions(model_asset_path = 'efficientdet_lite2.tflite') # pack com as classes de objetos identificáveis
options = vision.ObjectDetectorOptions(base_options = base_options, score_threshold = 0.1, category_allowlist = ["sports ball"])

# Passo 2: inicialização do detector MediaPipe
detector = vision.ObjectDetector.create_from_options(options)

# Passo 3: Abertura do vídeo teste (poderia ser direto da webcam também)
cap = cv2.VideoCapture("teste1.mp4")
if not cap.isOpened():
    raise RuntimeError("O vídeo não pode ser aberto")

# Passo 4: loop de detecção frame a frame
while True:
    # Leitura do frame em questão, com verificação se o frame ainda é válido ou se o vídeo já se encerrou
    ok, frame = cap.read()
    if not ok:
        break
    
    # Conversão de cores (OpenCV trabalha com BGR e MediaPipe precisa do RGB)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Criação de imagem no formato adequado para o MediaPipe com as cores em RGB
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    
    # Ação de detecção do MediaPipe
    result = detector.detect(image)
    
    # Detecção da bounding box do frame
    for detection in result.detections:
        bbox = detection.bounding_box
        xi = bbox.origin_x
        yi = bbox.origin_y
        xf = xi + bbox.width
        yf = yi + bbox.height
        
        # Desenho da bounding box
        cv2.rectangle(frame, (xi, yi), (xf, yf), (0, 255, 0), 2)
    
    # Exibição da bounding box
    cv2.imshow("Bola de Futebol", frame)
    
    # Espera 1 milissegundo e verifica se a tecla 'q' foi pressionada em caso de desejo de encerramento do programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Passo 5: Encerramento da detecção pelo OpenCV
cap.release()
cv2.destroyAllWindows()