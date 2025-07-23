# YOLO-Interactive-Object-Recognition

Este projeto demonstra um sistema de **detecção de objetos em tempo real** utilizando **YOLOv8** integrado com uma interface interativa. Ao detectar objetos como *telemóveis*, *pessoas* , o sistema exibe uma **janela informativa com imagem, descrição e link adicional** sobre o item. Tudo isso é feito com base em uma **base de dados relacional MySQL**.

---

<!-- ## 📸 Demonstração

> *Um exemplo visual pode ser adicionado aqui, como um GIF curto ou imagem da aplicação em execução.* -->

---

## 🚀 Funcionalidades

- 🎯 Detecção de objetos com YOLOv8 (Ultralytics)
- 💡 Popup informativo sobre o objeto detectado
- 🔗 Link clicável com mais informações sobre o objeto
- 🖱️ Interação via eventos de mouse
- 🗃️ Armazenamento e recuperação de dados via MySQL
- 📷 Suporte a webcam local e IP

---

## 🛠️ Tecnologias utilizadas

- YOLOv8
- OpenCV
- Pillow
- MySQL


---

## 📂 Organização do projeto

- **main.py**: Lógica principal da aplicação
- **database/**: Módulos de conexão e manipulação de dados no MySQL
- **utils/**: Funções auxiliares, interações gráficas e eventos de mouse
- **YOLOWeights/**: Modelos treinados (YOLOv8 em `.pt` e `.onnx`)
- **images/**: Imagens de exemplo usadas para identificar objetos
- **font/**: Fonte usada no popup informativo
- **requirements.txt**: Bibliotecas necessárias

---

## ⚙️ Como executar o projeto


### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/YOLO-Interactive-Object-Recognition.git
cd YOLO-Interactive-Object-Recognition
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados MySQL

- Crie o banco database_detect com permissões para leitura e escrita.

- Configure as credenciais no arquivo data_database.py.

- Ao iniciar o sistema, as tabelas necessárias serão criadas automaticamente.

### 5. Execute o programa

```bash
python main.py
```

### 🧠 Lógica de funcionamento

- A webcam é ativada e cada frame é analisado por um modelo YOLOv8.

- Se um objeto pré-definido for detectado, um círculo aparece no canto da tela.

- Ao clicar no círculo, um popup animado exibe informações detalhadas sobre o objeto.

- Links informativos são clicáveis e abrem no navegador.

- Todas as detecções são registradas em banco de dados com data e hora.

### 🛡️ Segurança e boas práticas

- Certifique-se de manter suas credenciais do banco de dados fora do repositório (ex: usar .env).


### 👨‍💻 Autor

Pedro Tenório
Desenvolvedor Python | Visão Computacional | Inteligência Artificial