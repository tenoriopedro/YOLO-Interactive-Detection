# Sistema de Deteção de Objetos com YOLOv8 e MySQL

<p align="center">
  <img src="https://github.com/tenoriopedro/YOLO-Interactive-Detection/blob/main/object_detection.gif?raw=true" alt="Demonstração do Sistema de Deteção YOLOv8" width="700"/>
</p>

---

## 🚀 Visão Geral

Este projeto é uma aplicação de **deteção de objetos em tempo real** que usa **YOLOv8** e **OpenCV**. O sistema identifica objetos via webcam e apresenta um **popup interativo** com informações (nome, descrição, link) guardadas numa **base de dados MySQL**.

A interface permite interações do rato, tornando-a uma ferramenta poderosa para demonstrações de IA, vigilância ou aplicações educacionais.

---

### 🛠️ Stack Tecnológico

* **Python 3.11**
* **Computer Vision:** YOLOv8, OpenCV, PIL (Pillow)
* **Base de Dados:** MySQL
* **Outros:** `dotenv` (para gestão de credenciais)

---

### 💡 Casos de Uso Principais

* Vigilância e monitorização inteligente em tempo real.
* Instalações interativas (ex: museus ou publicidade).
* Anotação de streams de vídeo (via captura HDMI).
* Ferramenta educacional para IA e Visão Computacional.
* Geração de *datasets* com *logs* de data/hora.

---

### ⚙️ Detalhes Técnicos e Instalação (Local)

<details>
  <summary>
    <strong>[+] Clique para expandir</strong> (Instruções de setup, Lógica de Operação, etc.)
  </summary>

  <h4>1. Como Executar</h4>

  <ol>
    <li>Clone o repositório.</li>
    <li>Crie e ative um ambiente virtual (<code>python -m venv venv</code>).</li>
    <li>Instale as dependências: <code>pip install -r requirements.txt</code></li>
    <li>
      <strong>Configure as Credenciais do MySQL:</strong>
      <ul>
        <li>Copie <code>dotenv_files/.env-example</code> para <code>dotenv_files/.env</code>.</li>
        <li>Insira a sua palavra-passe do MySQL (o utilizador precisa de permissão para <code>CREATE DATABASE</code>) no ficheiro <code>.env</code>.</li>
        <li><strong>Não é necessário criar a base de dados ou tabelas manualmente.</strong> O script trata de todo o setup na primeira execução.</li>
      </ul>
    </li>
    <li>Execute o programa: <code>python main.py</code></li>
  </ol>

  <h4>2. Lógica de Operação</h4>
  <ul>
    <li>A webcam é ativada e cada frame é analisado pelo YOLOv8.</li>
    <li>Se um objeto predefinido for detetado, um círculo aparece no ecrã.</li>
    <li>Clicar no círculo exibe um popup animado com informação da base de dados.</li>
    <li>Todas as deteções são registadas na base de dados com data/hora.</li>
  </ul>
  
  <h4>3. Adicionar Novos Objetos</h4>
  <ul>
    <li>O sistema deteta dois objetos por defeito. Para adicionar mais, use o script <code>add_object_info.py</code>.</li>
  </ul>
</details>

---

### 👨‍💻 Autor
Pedro Tenório
