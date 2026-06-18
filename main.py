# Passo 0: Imports necessários para o processo de visão computacional e delimitação das caixas de visualização (bounding boxes)

# OpenCV para captura e pré-processamento
import cv2
# NumPy, dependência implícita para representação das coordenadas enquanto parte de matrizes
import numpy as np
# Import para cálculo de quantidade de frames por segundo
import time
# MediaPipe, framework para detecção, isolamento e classificação do objeto alvo
import mediapipe as mp
from mediapipe.tasks import python 
from mediapipe.tasks.python import vision 

# Passo 1: definição das configurações de detecção e filtragem para detectar a bola de futebol, enquadrada na categoria 
# 'sports ball' abaixo
base_options = python.BaseOptions(model_asset_path = 'efficientdet_lite0.tflite') # pack com as classes de objetos identificáveis
options = vision.ObjectDetectorOptions(base_options = base_options, score_threshold = 0.1, category_allowlist = ["sports ball"])

# Passo 2: inicialização do detector MediaPipe
detector = vision.ObjectDetector.create_from_options(options)

# Passo 3: Abertura do(a) vídeo teste/webcam
cap = cv2.VideoCapture("videosFinais/contra_luz.mp4")
# OBS: para usar a webcam -> cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("O(a) vídeo/câmera não pode ser aberto(a)")

# Passo 4: loop de detecção frame a frame
tempo_anterior = time.time()
while True:
    # Leitura do frame em questão, com verificação se o frame ainda é válido ou se o vídeo já se encerrou
    ok, frame = cap.read()
    if not ok:
        break
    
    # Redimensionamento para aumento de FPS
    frame = cv2.resize(frame, (1280, 720))
    
    # Conversão de cores (OpenCV trabalha com BGR e MediaPipe precisa do RGB)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Criação de imagem no formato adequado para o MediaPipe com as cores em RGB
    imagem = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    
    # Ação de detecção do MediaPipe
    resultado = detector.detect(imagem)

    # Print de fps do video
    tempo_atual = time.time()
    fps = 1 / (tempo_atual - tempo_anterior)
    tempo_anterior = tempo_atual

    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    
    # Detecção da bounding box do frame
    if resultado.detections:
        for detection in resultado.detections:
            bbox = detection.bounding_box
            xi = bbox.origin_x
            yi = bbox.origin_y
            xf = xi + bbox.width
            yf = yi + bbox.height
            largura = bbox.width   
            altura = bbox.height
            centro_x = xi + largura // 2
            centro_y = yi + altura // 2
            
            
            # Desenho da bounding box

            # Aqui, primeiramente pegamos a categoria e confiabilidade do objeto detectado
            categoria = detection.categories[0].category_name
            confianca = detection.categories[0].score
            # Após isso, exibimos a categoria, sua confiabilidade e a bounding box propriamente dita
            cv2.putText(frame, f"{categoria}; confianca: {confianca:.2f}", (bbox.origin_x, bbox.origin_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            cv2.rectangle(frame, (xi, yi), (xf, yf), (255, 0, 0), 2)
            cv2.circle(frame,(centro_x, centro_y),5,(0, 0, 255),-1)
    
    # Exibição da bounding box
    cv2.imshow("Bola Laranja", frame)
    
    # Espera 1 milissegundo e verifica se a tecla 'q' foi pressionada em caso de desejo de encerramento do programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Passo 5: Encerramento da detecção pelo OpenCV
cap.release()
cv2.destroyAllWindows()