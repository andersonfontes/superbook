# Aula Extra – Organizando Templates Globais

---

## 📝 Introdução

Antes de começarmos o **módulo de Forms**, vamos dar um passo atrás para **refatorar a estrutura dos templates** do nosso projeto **SuperBook**.

Durante a aula de Templates, **duplicamos o `base.html` e o `partials/menu.html` dentro de cada app** (heroes e posts). Isso funcionou para aprender, mas **não é uma boa prática** a longo prazo.

📌 **Por que isso é um problema?**

- Se precisarmos alterar o menu, teríamos que atualizar em **dois lugares**.
- Manter arquivos duplicados aumenta as chances de erro.

📌 **Qual o objetivo desta aula?**

- Centralizar arquivos compartilhados em **um único lugar**
- Aplicar uma **melhor prática de arquitetura** lembre-se do Design Pattern do Django: **DRY – Don’t Repeat Yourself**)
- Preparar a base para os próximos módulos (Forms, autenticação etc.).

---

## ✅ 1️⃣ Por que as pastas `templates` dos apps funcionam sem configuração?

No **settings.py**, temos:

```python

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        ...
    }
]

```

🔹 **Quando `APP_DIRS=True`**, o Django automaticamente encontra templates que estão **dentro de cada app**, como:

- `heroes/templates/heroes/lista_herois.html`
- `posts/templates/posts/lista_posts.html`

Ou seja, **não precisamos configurar manualmente** para cada app.

Porém, se quisermos ter **templates fora dos apps (globais)**, precisamos **registrar esse caminho** no `DIRS`.

---

## ✅ 2️⃣ Por que criar uma pasta `templates` global?

- Evita **duplicar arquivos** como `base.html` e `partials/menu.html`.
- Centraliza o layout e componentes comuns a todo o projeto.
- Fica mais **organizado e escalável**, principalmente em projetos grandes.

---

## ✅ 3️⃣ Nova Estrutura do Projeto

Depois da refatoração, vamos ter:

```

superbook/
    templates/
        base.html
        partials/
            menu.html

  heroes/
    templates/heroes/lista_herois.html

  posts/
    templates/posts/lista_posts.html

```

Ou seja, **um único base.html e menu.html** para todo o projeto.

---

## ✅ 4️⃣ Ajustando o settings.py

Precisamos dizer ao Django para procurar **templates globais**.

No arquivo **settings.py**:

```python

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'superbook' / 'templates'],  # <-- adicionamos a pasta global
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

✅ **Agora o Django vai procurar templates em dois lugares:**

1. Na pasta global `templates/` (porque adicionamos em `DIRS`)
2. Dentro de cada app (por causa do `APP_DIRS=True`)

---

## ✅ 5️⃣ Movendo os Arquivos

Agora vamos **mover**:

- `heroes/templates/base.html` → `templates/base.html`
- `heroes/templates/partials/menu.html` → `templates/partials/menu.html`
- (Se tiver em posts duplicado, apague ou mova também)

---

## ✅ 6️⃣ Ajustando os Templates

👉 **Boa notícia:**

Você **não precisa mudar nada** nas páginas que herdam!

Antes (já está assim):

```

{% extends 'base.html' %}
{% include 'partials/menu.html' %}

```

Depois de mover… **continua igual!**

Porque agora o Django vai encontrar o `base.html` global via `DIRS`.

---

## ✅ 7️⃣ Testando

1. Rode o servidor:
    
    ```bash
    
    python manage.py runserver
    
    ```
    
2. Acesse:
    - **`/heroes/lista/`**
    - **`/posts/lista/`**
3. Se o layout e menu aparecem normalmente → **funcionou!**

---

## ✅ 8️⃣ O que aprendemos

- **APP_DIRS=True** encontra templates dentro dos apps automaticamente.
- Para templates **globais**, é preciso registrar a pasta em `DIRS`.
- Centralizar layouts evita duplicação (padrão **DRY – Don’t Repeat Yourself**).

Agora temos uma **arquitetura melhor** para os templates, e o projeto está pronto para seguir para o módulo de **Forms**.

---

📌 **Exercício Prático**

1. Crie a pasta `templates/` na raiz do projeto.
2. Mova `base.html` e `partials/menu.html` para essa pasta.
3. Ajuste o `settings.py` adicionando `BASE_DIR / 'templates'` no `DIRS`.
4. Teste o acesso às páginas `/heroes/lista/` e `/posts/lista/`.
5. **Envie prints mostrando que o layout continua funcionando.**