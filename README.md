# Aula Capítulo 3 - Models

Este exemplo mostra como criar Models para o projeto SuperBook.

## Como rodar

1. Crie e ative o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Crie o banco e rode as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Carregue os dados iniciais (fixtures):
```bash
python manage.py loaddata initial_fixture.json
```

> Fixtures são arquivos JSON com dados iniciais para popular o banco automaticamente.

5. Rode o servidor:
```bash
python manage.py runserver
```

Acesse http://127.0.0.1:8000

Usuário admin/admin (se criado no futuro).
