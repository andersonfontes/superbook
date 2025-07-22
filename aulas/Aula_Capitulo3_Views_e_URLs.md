# Projeto Superbook – Views e URLs

---

# ✅ 1️⃣ O que são Views?

- Uma **View** é uma função ou classe que **recebe uma requisição (request)** e **retorna uma resposta (response)**.

- Pode retornar:
    - Um **HTML** (página pronta)
    - Um **JSON** (dados para uma API)
    - Ou até um simples texto (`HttpResponse`).

📌 **Fluxo básico do Django:**

```
Usuário → URL → View → Resposta
```

---

# ✅ 2️⃣ URLs no Django

O Django usa o arquivo **`urls.py`** para mapear **caminhos (rotas)** para cada view.

- O **`urls.py` principal** do projeto (`superbook/urls.py`) centraliza as rotas.
- Cada **app** (`heroes`, `posts`) pode ter seu **próprio `urls.py`**, e você conecta usando `include()`.

Exemplo no `superbook/urls.py`:

```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('heroes/', include('heroes.urls')),  # rotas do app heroes
    path('posts/', include('posts.urls')),    # rotas do app posts
]
```

---

# ✅ 3️⃣ Function-Based Views (FBVs)

As **FBVs** são **funções Python normais**.

Para começar simples, vamos criar uma view que retorna apenas um texto.

---

### Passo 1 – Criar uma FBV simples

No **`heroes/views.py`** adicione:

```python

from django.http import HttpResponse

def hello_heroes(request):
    return HttpResponse("Bem-vindo ao módulo Heroes!")

```

---

### Passo 2 – Conectar a view à URL

Crie **`heroes/urls.py`**:

```python

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_heroes, name='hello_heroes'),
]

```

**Para iniciar o servidor, rode no terminal:**
```
python manage.py runserver

```

Pronto! Se acessar **`http://127.0.0.1:8000/heroes/hello/`** você verá só o texto.

---

👉 **Explicação:**

- `HttpResponse` retorna texto puro
- Usamos `path()` para mapear a URL para a função `hello_heroes`

---

# ✅ 4️⃣ Evoluindo FBV para usar Template

Agora em vez de texto puro, vamos renderizar uma **página HTML**.

---

### Passo 1 – Criar a pasta de templates

Dentro do app `heroes`, crie:

```

heroes/
  templates/
    heroes/
      lista_herois.html
```

📄 **heroes/templates/heroes/lista_herois.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Heróis</title>
</head>
<body>
    <h1>Heróis cadastrados</h1>
    <ul>
        {% for hero in herois %}
        <li>{{ hero.codinome }} - {{ hero.poder_principal }}</li>
        {% endfor %}
    </ul>
</body>
</html>

```

---

### Passo 2 – Alterar a view para renderizar o template

No **`heroes/views.py`**:

```python
from django.shortcuts import render
from .models import Hero

def lista_herois(request):
    herois = Hero.objects.all()  # busca todos os heróis do banco
    return render(request, "heroes/lista_herois.html", {"herois": herois})

```

---

### Passo 3 – Adicionar a nova rota

No **`heroes/urls.py`**:

```python

urlpatterns = [
    path('hello/', views.hello_heroes, name='hello_heroes'),
    path('lista/', views.lista_herois, name='lista_herois'),
]

```
**Para iniciar o servidor, rode no terminal:**
```
python manage.py runserver

```

Agora acesse **`http://127.0.0.1:8000/heroes/lista/`** e você verá os heróis renderizados no HTML.

---

👉 **Explicação curta:**

- `render(request, template, contexto)` → carrega o template e passa os dados do banco.
- No HTML usamos `{% for hero in herois %}` para listar.

---

# ✅ 5️⃣ Class-Based Views (CBVs)

Agora que já temos um template pronto, vamos ver a forma **orientada a classes**.

As CBVs economizam código para operações comuns como **listar registros** ou **mostrar detalhes**.

---

### Passo 1 – Criar uma CBV

No **`heroes/views.py`** adicione:

```python
from django.views.generic import ListView
from .models import Hero

class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"
```

---

### Passo 2 – Adicionar rota para CBV

No **`heroes/urls.py`**:

```python
from .views import HeroListView

urlpatterns = [
    path('hello/', views.hello_heroes, name='hello_heroes'),
    path('lista/', views.lista_herois, name='lista_herois'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
]
```

Agora acesse **`http://127.0.0.1:8000/heroes/cbv-lista/`**.

Ele vai usar o **mesmo template** sem precisar escrever a lógica manualmente.

---

👉 **Explicação curta:**

- `ListView` já faz automaticamente:
    
    ✅ Busca todos os registros do model
    
    ✅ Passa para o template
    
- `as_view()` transforma a classe em uma view normal para o Django entender

---

# ✅ 6️⃣ Resumo visual do fluxo

```

URL → View → Template → Response
```

1. O **usuário acessa uma URL**
2. O Django mapeia para a **view correta** (FBV ou CBV)
3. A view **busca dados no banco**
4. A view **renderiza um template** (ou retorna JSON)
5. O **navegador recebe o HTML pronto**

---

# ✅ 7️⃣ Mini exercício prático

Crie no app `posts`:

- Uma **FBV** para listar posts (`lista_posts`)
- Um **template simples** para exibir a lista de posts
- E depois uma **CBV (ListView)** para fazer a mesma coisa

---

![image.png](a25907f9-005a-4236-a1a8-9c41bf0de191.png)

# ✅ O que aprendemos?

✅ Como mapear URLs para views

✅ Diferença entre FBV e CBV

✅ Como usar `render()` e templates

✅ Que CBVs economizam código quando reaproveitamos template

---