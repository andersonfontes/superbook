# Projeto SuperBook - Templates

---

# 1️⃣ Introdução ao sistema de templates

O Django usa um mecanismo chamado **Django Template Language (DTL)** para separar a **lógica de apresentação** da **lógica de negócio**.

- As **views** enviam **dados (contexto)** para o template.
- O **template** gera o HTML dinâmico a partir desses dados.
- Assim, o código Python não fica misturado com HTML.

📌 **Fluxo básico:**

```

View → Contexto (dados) → Template → HTML dinâmico → Navegador
```

---

# 2️⃣ Variáveis e filtros

Em um template, usamos `{{ variavel }}` para exibir valores.

Exemplo:

```html

<p>Codinome: {{ hero.codinome }}</p>
<p>Poder: {{ hero.poder_principal }}</p>

```

Podemos também **modificar a exibição** usando **filtros**:

```html

<p>Nome em maiúsculas: {{ hero.codinome|upper }}</p>
<p>Resumo da história: {{ hero.historia|truncatechars:50 }}</p>
<p>Data formatada: {{ hero.criado_em|date:"d/m/Y H:i" }}</p>

```

👉 Filtros mais comuns:

- `upper`, `lower`, `title` → alteram o texto
- `date:"formato"` → formata datas
- `default:"valor"` → exibe um valor padrão se a variável for nula

---

# 3️⃣ Tags de controle no Django Template

As **tags** permitem colocar **lógica simples** dentro dos templates HTML.

Vamos aprender com **exemplos diretos no projeto SuperBook**.

---

### 🔹 Passo 1 – Vamos editar o template `heroes/lista_herois.html`

Abra o arquivo **`heroes/templates/heroes/lista_herois.html`** (ou crie se ainda não existe).

---

- **Estrutura de repetição (`for`)**

Cole dentro do `<body>`:

```html

<ul>
{% for hero in herois %}
    <li>{{ hero.codinome }} - {{ hero.poder_principal }}</li>
{% empty %}
    <li>Nenhum herói cadastrado.</li>
{% endfor %}
</ul>

```

**O que isso faz?**

- Ele vai **percorrer a lista de heróis enviada pela View**.
- Para cada herói, mostra o `codinome` e o `poder_principal`.
- Se não houver heróis, exibe **"Nenhum herói cadastrado"**.

Agora, se você acessar `http://127.0.0.1:8000/heroes/lista/`, verá a lista.

---

- **Estrutura condicional (`if`)**

Logo abaixo do `for`, adicione **essa verificação**:

```html

{% if hero.cidade == "Nova York" %}
    <p>Este herói protege Nova York!</p>
{% else %}
    <p>Herói de outra cidade.</p>
{% endif %}

```

**O que isso faz?**

- Dentro do loop, para cada herói, ele **checa se a cidade é Nova York**.
- Mostra uma mensagem específica dependendo da cidade.

💡 **Importante:**

Isso só funciona **dentro do `{% for hero in herois %}`**, pois precisa do objeto `hero`.

---

- **Incluindo pedaços reutilizáveis**

Agora vamos criar um **menu simples** que será *incluído em várias páginas*.

1. **Crie um novo arquivo `heroes/templates/partials/menu.html`**

📄 **partials/menu.html**

```html

<nav>
  <a href="{% url 'lista_herois' %}">Heróis</a> |
  <a href="{% url 'lista_posts' %}">Posts</a>
</nav>

```

---

1. Inclua o menu no topo do `lista_herois.html`

Adicione no início do `<body>`:

```html

{% include "partials/menu.html" %}

```

✅ **O que isso faz?**

- Ele **insere automaticamente** o HTML do menu no template.
- Se o menu mudar, você só edita **um arquivo** (`menu.html`).

---

### Ordem final no `lista_herois.html`

Seu template agora ficará assim:

```html

{% include "partials/menu.html" %}

<h2>Heróis cadastrados</h2>

<ul>
{% for hero in herois %}
    <li>
        {{ hero.codinome }} - {{ hero.poder_principal }}

        {% if hero.cidade == "Nova York" %}
            <p>Este herói protege Nova York!</p>
        {% else %}
            <p>Herói de outra cidade.</p>
        {% endif %}
    </li>
{% empty %}
    <li>Nenhum herói cadastrado.</li>
{% endfor %}
</ul>

```

# 4️⃣ Herança de templates

Para evitar duplicação, criamos um **template base** com o layout padrão.

📄 **templates/base.html**

```html

<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}SuperBook{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
    <header>
        <h1>SuperBook</h1>
        {% include "partials/menu.html" %}
    </header>

    <main class="container mt-4">
        {% block content %}{% endblock %}
    </main>
</body>
</html>

```

Depois, qualquer template pode **estender** esse layout:

📄 **heroes/lista_herois.html**

```html

{% extends 'base.html' %}

{% block title %}Lista de Heróis{% endblock %}

{% block content %}
<h2>Heróis cadastrados</h2>
<ul>
{% for hero in herois %}
    <li>
        {{ hero.codinome }} - {{ hero.poder_principal }}

        {% if hero.cidade == "Nova York" %}
            <p>Este herói protege Nova York!</p>
        {% else %}
            <p>Herói de outra cidade.</p>
        {% endif %}
    </li>
{% empty %}
    <li>Nenhum herói cadastrado.</li>
{% endfor %}
</ul>
{% endblock %}

```

🔹 Entendendo algumas tags importantes
{% load static %}

Essa tag carrega o sistema de arquivos estáticos do Django, permitindo usar {% static 'caminho/arquivo.css' %} para acessar imagens, CSS ou JavaScript.

{% block content %} ... {% endblock %}

Define uma área de conteúdo dinâmico em um template que herda de outro.

No base.html, ele marca o local onde cada página filha vai inserir seu conteúdo.

{% block title %} ... {% endblock %}

Funciona do mesmo jeito, mas para definir o título da página ou outras partes personalizáveis

---

## ✅ 6️⃣ Arquivos estáticos e Bootstrap

Agora vamos melhorar o visual das páginas usando **Bootstrap 5**.

---

### 🔹 Passo 1 – Adicionar Bootstrap no `base.html`

Vamos usar o **CDN**, que é a forma mais simples (não precisa baixar arquivos).

Abra ou crie o arquivo **`templates/base.html`** e insira este conteúdo:

```html

{% load static %}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}SuperBook{% endblock %}</title>

  <!-- Bootstrap 5 CSS via CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

</head>
<body>

  <!-- Conteúdo dinâmico -->
  <main class="container mt-4">
    {% block content %}{% endblock %}
  </main>

  <!-- Bootstrap 5 JS via CDN -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

</body>
</html>

```

✅ **O que fizemos:**

- Adicionamos o **Bootstrap 5 CSS** no `<head>`
- Incluímos o **Bootstrap JS** no final do `<body>`
- Criamos um **container centralizado** para os conteúdos das páginas

---

### 🔹 Passo 2 – Adaptar a lista de heróis para usar Bootstrap

Agora vamos deixar a lista de heróis mais bonita, exibindo como **cards**.

Abra **`heroes/templates/heroes/lista_herois.html`** e substitua por:

```html

{% extends 'base.html' %}

{% block title %}Lista de Heróis{% endblock %}

{% block content %}
<h2 class="mb-4">Heróis cadastrados</h2>

<div class="row">
{% for hero in herois %}
  <div class="col-md-4">
    <div class="card mb-3">
      <div class="card-body">
        <h5 class="card-title">{{ hero.codinome }}</h5>
        <p class="card-text">{{ hero.poder_principal }}</p>
        <small class="text-muted">{{ hero.cidade }}</small>
      </div>
    </div>
  </div>
{% empty %}
  <p>Nenhum herói encontrado.</p>
{% endfor %}
</div>
{% endblock %}

```

✅ **O que mudou:**

- Adicionamos classes do Bootstrap (`row`, `col-md-4`, `card`, etc.)
- Agora cada herói aparece como um **card estilizado** automaticamente

### Resultado esperado

Ao acessar **`http://127.0.0.1:8000/heroes/lista/`**, a página já deve estar com um visual melhor, com **cards do Bootstrap** para cada herói.

---

# 5️⃣ Organização e boas práticas

- Cada app pode ter **sua pasta de templates**, exemplo:
    
    ```
    
    heroes/templates/heroes/lista_herois.html
    posts/templates/posts/lista_posts.html
    
    ```
    
- Use um **base.html** para herança
- Reaproveite componentes com `{% include %}`
- Evite lógica complexa no template – mantenha cálculos na View

---

---

# 7️⃣ Boas práticas e padrões

- Use **herança + includes** para evitar repetir HTML
- Deixe o template apenas para **exibição**, nunca para cálculos
- Para dados globais em todos os templates, use **context processors** (citamos sem aprofundar agora)

---

# Exercício Prático

1. Crie um **`base.html`** com um menu simples e carregue o Bootstrap.
2. Adapte **lista_herois.html** para estender o base e usar cards com Bootstrap.
3. Faça o mesmo para **lista_posts.html** no app posts.
4. Adicione um menu com links para “Heróis” e “Posts”.
5. Acesse as páginas para verificar se tudo funciona.
6. **Envie os prints como entrega da atividade.**