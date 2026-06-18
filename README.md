# Onboarding DV 2026 - Grupo 5
### Algoritmo de percepção desenvolvido pelo Grupo 5 do Onboarding 2026 para a detecção de bola laranja. Para isso, utilizamos a classe "sports ball" do dataset "EfficientDet Lite0" oferecido pela Google junto com o MediaPipe.

## Instalação

### Pré-requisitos (Linguagem)

#### Para realizar o desenvolvimento na linguagem Python, deve-se preparar sua máquina para tê-lo, junto de seu gerenciador de pacotes (pip) e um ambiente virtual (com venv) para isolar a biblioteca e permitir trabalhar com versões isoladas de cada dependência.
    
#### Linux: Python já vem instalado. Resta apenas instalar o pip e o venv:
    sudo apt install python3-pip python3-venv

##### Windows: ambos já vem instalados junto com o Python. Para instalar o Python, utilize o próprio gerenciador de pacotes nativo do sistema operacional, winget. Tanto no Powershell como no CMD, rode:
    winget install Python.Python.3.11

##### MacOS: utilize o gerenciador de pacotes nativo da Apple, Homebrew, pra instalar os três requisitos de uma vez:
    brew install python@3.11

### Ambiente virtual
#### Como dito anteriormente, configura-se um ambiente virtual para isolar as versões das dependências do projeto em questão, evitando conflito ou alteração de versões na máquina como um todo.

#### 1. Vá até a pasta do projeto:
    cd (Caminho)

#### 2. Crie o ambiente virtual na pasta do projeto:
    python3 -m venv venv

#### 3. Ative o ambiente virtual:
##### Linux / MacOS:
    source venv/bin/activate
##### Windows:
###### Powershell:
    venv\Scripts\Activate.ps1
###### caso não funcione, tente:
    .\venv\Scripts\Activate.ps1
###### CMD:
    venv\Scripts\activate.bat

#### 4.  Instale as dependências especificadas no documento de planejamento**
    pip install -r requirements.txt
    
### Dependências
    | Componente | Versão    | Função |
    | ---------- | --------- | ------ |
    | Python     | 3.11      | Linguagem de programação |
    | MediaPipe  | 0.10.35   | Framework de Isolamento e detecção |
    | OpenCV     | 4.10.0.84 | Captura, pré-processamento e bounding boxes |
    | NumPy      | 1.26.4    | Representação de frames (dependência implícita) |