# Projeto Superbook: Preparação do Ambiente e Início do Projeto

Antes de criarmos os Models, precisamos preparar o ambiente e iniciar o projeto Django.

---

## ✅ 0️⃣ Preparando o ambiente virtual e instalando Django

1. Crie uma pasta para o projeto 

```bash

mkdir superbook
```

1. Crie um ambiente virtual:

```bash

python -m venv venv
```

1. Ative o ambiente virtual:
- Windows:

```bash

venv\Scripts\activate
```

- Linux/Mac:

```bash

source venv/bin/activate

```

1. Instale o Django e dependências iniciais:

```bash

pip install django

```

---

## ✅ 1️⃣ Criando o projeto Django

**Dentro** da pasta do projeto, de o comando. Nao esqueça do ponto!

```bash
cd superbook

django-admin startproject superbook .
```

Isso criará a estrutura base do projeto com `manage.py` e a pasta `superbook/`.

---

## ✅ 2️⃣ Criando os apps do SuperBook

Vamos criar os apps que representam as áreas principais do sistema:

```bash

python manage.py startapp heroes
python manage.py startapp posts

```

- `heroes` → para gerenciar os perfis dos super-heróis.
- `posts` → para gerenciar as publicações.

---

## ✅ 3️⃣ Registrando os apps no settings.py

No arquivo `superbook/settings.py`, adicione os apps criados:

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps do SuperBook
    'heroes',
    'posts',
]

```

---

Pronto! Com isso, o projeto Django está criado e os apps básicos registrados.

A partir daqui, podemos definir os **Models** para representar as tabelas no banco de dados.

---

# Capítulo 3: Criação dos models

---

## 1️⃣ O que são Models no Django?

- **Models** são **classes Python** que **representam tabelas do banco de dados**.
- Cada **atributo** da classe é uma **coluna** da tabela.
- Com Django, não escrevemos SQL manualmente para tudo; usamos o **ORM (Object-Relational Mapper)**.

---

### 🧠 ORM: o que é e por que usar?

- **Traduz objetos Python em comandos SQL**.
- Permite:
    
    ✅ Criar tabelas sem escrever SQL
    
    ✅ Fazer consultas com métodos Python (`.filter()`, `.all()`)
    
    ✅ Alterar dados com facilidade (`.save()`, `.delete()`)
    

---

## 2️⃣ Relembrando relacionamentos e normalização

📌 **Normalização** é organizar o banco para **evitar redundância** e manter a **integridade dos dados**.

### **Principais relacionamentos** no Django:

- **OneToOneField (1:1)**
    
    Um registro se relaciona com exatamente um outro (ex: Perfil ⇔ Usuário).
    
- **ForeignKey (1:N)**
    
    Um registro de uma tabela pode ter **vários relacionados** em outra (ex: Usuário ⇔ Posts).
    
- **ManyToManyField (N:N)**
    
    Um registro pode se relacionar com vários e vice-versa (ex: Usuários ⇔ Grupos).
    

💡 **No banco de dados**, o N:N é resolvido com uma **tabela associativa**.

✅ **No Django**, o `ManyToManyField` **cria automaticamente** essa tabela intermediária para você, sem que você precise declarar manualmente.

👉 Se você quiser controle total, pode criar explicitamente a tabela intermediária (como fizemos com o modelo `Like`).

---

## 3️⃣ Estruturando Models do SuperBook

Vamos criar **duas entidades principais**:

- `Hero` → perfis dos super-heróis
- `Post` → publicações no feed

Depois vamos relacionar com **Likes** (que é, na prática, a tabela associativa N:N).

---

### ✅ **Passo 1: Hero**

```python

from django.db import models

class Hero(models.Model):
    codinome = models.CharField(max_length=50, unique=True)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder_principal = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    historia = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codinome

```

👉 **Explicação**:

- `CharField` → texto curto
- `TextField` → texto longo
- `auto_now_add=True` → preenche automaticamente com data de criação

---

### ✅ **Passo 2: Post**

```python

class Post(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="posts")
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.codinome}: {self.mensagem[:30]}..."

```

👉 **Explicação**:

- `ForeignKey` → relacionamento 1:N (um Herói pode ter vários Posts)
- `on_delete=models.CASCADE` → se o Herói for apagado, os posts também são

---

### ✅ **Passo 3: Likes (tabela associativa N:N)**

```python

class Like(models.Model):
    heroi = models.ForeignKey(Hero, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('heroi', 'post')

    def __str__(self):
        return f"{self.heroi.codinome} curtiu {self.post.id}"

```

👉 **Explicação**:

- Estamos criando explicitamente a **tabela associativa** para registrar quem curtiu cada post.
- O `unique_together` evita curtidas duplicadas.
- Se quiséssemos algo mais automático, poderíamos simplesmente fazer:

```python

likes = models.ManyToManyField(Hero, related_name="curtidas")

```

E o Django criaria a tabela intermediária sozinho.

---

## 4️⃣ Atualizando o banco

Depois de criar os models:

```bash

python manage.py makemigrations
python manage.py migrate

```

Isso gera as tabelas automaticamente.

---

## 5️⃣ Criando alguns dados iniciais

Podemos usar **fixtures** para popular com exemplos.

---

### ❓ O que é um fixture?

Um **fixture** é um arquivo (JSON, YAML ou XML) que contém **dados prontos** para serem carregados no banco de dados.

✅ Serve para **popular dados de teste** ou **dados obrigatórios iniciais**, sem ter que digitar manualmente.

---

### Exemplo

```json
json
CopiarEditar
[
  {
    "model": "superbook.Hero",
    "pk": 1,
    "fields": {
      "codinome": "Acorn",
      "nome_real": "Desconhecido",
      "poder_principal": "Superinteligência",
      "cidade": "Nova York",
      "historia": "Um esquilo que luta contra o crime."
    }
  },
  {
    "model": "superbook.Post",
    "pk": 1,
    "fields": {
      "autor": 1,
      "mensagem": "Bem-vindo ao SuperBook!"
    }
  }
]

```

Carregar no banco:

```bash

python manage.py loaddata initial_fixture.json

```

---

## 6️⃣ Testando no Shell

```bash

python manage.py shell

```

```python

from superbook.models import Hero, Post

h = Hero.objects.get(codinome="Acorn")
print(h.posts.all())  # Lista posts do herói

Post.objects.create(autor=h, mensagem="Nova missão no Central Park!")

```

---

## 7️⃣ O que aprendemos?

✅ Como o Django ORM mapeia **classes → tabelas**

✅ Como criar **relacionamentos 1:N e N:N**

✅ Como aplicar **normalização** de forma natural com Models

✅ Como popular o banco com **fixtures**

---

## Próximos passos

Na próxima aula veremos **Class-Based Views** para listar e criar posts desses modelos.