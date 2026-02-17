# 🍎 Daily Diet API

Uma API RESTful desenvolvida em **Python** com **Flask** para o gerenciamento de registros de dieta diária. Este projeto permite o controle total sobre as refeições, permitindo monitorar hábitos alimentares de forma eficiente e organizada.



## 🚀 Tecnologias e Ferramentas
* **Linguagem:** Python 3.14
* **Framework:** Flask
* **Banco de Dados:** MySQL (executado via Docker)
* **ORM:** Flask-SQLAlchemy
* **Containerização:** Docker & Docker Compose

## 🛠️ Como executar o projeto

### Pré-requisitos
* **Docker** e **Docker Compose** instalados.
* Um cliente API (como **Postman** ou **Insomnia**).

### Passo a passo
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/jftigre/DiarioAlimentarAPI.git](https://github.com/jftigre/DiarioAlimentarAPI.git)
   cd DiarioAlimentarAPI
Inicie o Banco de Dados:Bashdocker-compose up -d
Isso subirá o container MySQL configurado no Docker Compose.Configure o Ambiente Virtual e Dependências:Bashpython -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
Execute a aplicação:Bashpython app.py
As tabelas do banco de dados serão criadas automaticamente na primeira execução através do db.create_all().📍 Endpoints da APIMétodoEndpointDescriçãoPOST/mealsRegistra uma nova refeiçãoGET/mealsLista todas as refeições cadastradasGET/meals/<id>Visualiza os detalhes de uma refeição específicaPUT/meals/<id>Atualiza os dados de uma refeição existenteDELETE/meals/<id>Remove uma refeição do históricoExemplo de Payload (POST /meals):JSON{
  "name": "Almoço",
  "description": "Arroz, feijão e peito de frango",
  "datetime": "2026-02-17 12:30:00",
  "is_diet": true
}
📋 Funcionalidades ImplementadasCRUD Completo: Gerenciamento total de registros de refeições.Persistência em MySQL: Dados armazenados de forma segura em banco de dados relacional via Docker.Validação de Dados: Tratamento de campos obrigatórios e tipos de dados no backend.Tratamento de Datas: Armazenamento e retorno de datas no padrão ISO 8601.