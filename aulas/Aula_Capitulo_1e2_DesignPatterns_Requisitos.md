# Aula Porreta – Capítulos 1 e 2  
📘 **Design Patterns e Levantamento de Requisitos**

---

## 1️⃣ A origem dos Design Patterns

Muito antes de existirem linguagens de programação, arquitetos observavam que certos problemas em construções se repetiam — e com isso, começaram a registrar soluções bem-sucedidas. Essa ideia de “soluções reutilizáveis para problemas recorrentes” inspirou engenheiros de software a criar os chamados **padrões de projeto**, que ajudam a escrever código mais limpo, reutilizável e fácil de manter.

---

## 2️⃣ O que é um design pattern?

É uma **estrutura comum para resolver um problema típico** de forma elegante.  
Por exemplo:

- O **Template Method** define o esqueleto de uma operação e permite que subclasses preencham os detalhes.  
  Em Django, isso aparece nas **Generic Views**, que fornecem uma estrutura padrão para CRUDs, e você só preenche o que precisa mudar.

---

## 3️⃣ O que é código pythonico?

Código pythonico é aquele que segue os princípios de clareza, simplicidade e legibilidade. Compare:

```python
# Código pythonico: legível e direto
titulos = [livro.titulo for livro in livros if livro.disponivel]
```

Essa linha faz o mesmo que o exemplo abaixo, mas de forma mais clara:

```python
# Código verboso
titulos = []
for i in range(len(livros)):
    if livros[i].disponivel:
        titulos.append(livros[i].titulo)
```

✅ Código pythonico transmite **intenção** com menos esforço mental.

---

## 4️⃣ Antes de programar: entenda o problema

Criar um sistema começa com um bom levantamento de requisitos. Mas ao invés de planilhas frias e reuniões chatas, você pode começar de forma simples, empática e até divertida: **conversando com o usuário**.

---

## 5️⃣ Apresentando o projeto: SuperBook

Imagine que você vai criar uma rede social exclusiva para **super-heróis** e **seres extraordinários**.  
Seu primeiro entrevistado é **Acorn**, um esquilo cinza superinteligente que vive em Nova York. Veja como essa conversa pode revelar tudo que você precisa para começar a projetar:

---

### 📄 Entrevista com o esquilo Acorn

> 🐿️ Meu nome é **Acorn**. Sou um esquilo cinza que vive no Central Park, Nova York. Fiquei conhecido quando apareci numa matéria sobre super-heróis menos conhecidos. Agora estou experimentando um MacBook, acredita?

> 🧑‍💻 Estou muito animado com essa ideia de rede social. Heróis são solitários, sabe? Estão sempre na correria para salvar o mundo. Seria ótimo se a gente pudesse se conectar de forma discreta, sem revelar identidade. E o SuperBook parece ideal!

> 🎯 O que me chamou a atenção é que ele **não exige campos inúteis como “formação acadêmica” ou “cargo atual”**. Isso é ótimo! Não tenho diploma formal, e o último lugar onde trabalhei foi como espião da resistência roedora.

> 🧾 Quero um perfil simples: nome (ou codinome), poderes, localização (aproximada), e uma breve história. Nada que me comprometa, claro.

> 🧨 Também seria legal ver atualizações de outros heróis, talvez com uma opção de “curtir” ou dar um “pow!” nas postagens deles. Isso aumenta o moral!

> 📵 Só não quero notificações o tempo todo... roedores se distraem fácil. E a interface precisa ser limpa, objetiva. Nada de menus escondidos ou efeitos desnecessários.

---

## 6️⃣ O que essa entrevista revela?

- O **público-alvo** é formado por super-heróis (ou similares), que valorizam privacidade e agilidade.
- O sistema deve ser **leve**, **direto**, com **interface limpa** e sem distrações.
- Perfis personalizados com **codinome**, **poderes** e uma história.
- Posts com interação (ex: curtir, reagir com "pow").
- Uma timeline simples, sem algoritmo ou complexidade.

---

## 7️⃣ Como dividir isso em apps Django?

No Django, a recomendação é separar funcionalidades em **apps independentes e reutilizáveis**.  
Pensando no SuperBook, podemos dividir assim:

| App Django      | Função principal                            |
|------------------|---------------------------------------------|
| `usuarios`       | Cadastro, login, perfis, autenticação       |
| `posts`          | Criar, listar e reagir a postagens          |
| `reacoes`        | Curtidas, “pow!”, comentários (opcional)    |
| `timeline`       | Montar feed cronológico simples             |

Esses apps são **modulares**, ou seja, você pode reaproveitá-los em outros projetos (ex: um blog, um fórum).

---

## ✅ Boas práticas desde o início:

- Entenda o usuário antes de começar o código.
- Comece com rascunhos ou entrevistas simples.
- Separe responsabilidades em apps distintos.
- Use bibliotecas já existentes (ex: `django-allauth`, `crispy-forms`).
- Escreva código legível e com propósito.

---

## 🎓 Atividade para os alunos:

> Você foi contratado por Acorn para montar a versão beta do SuperBook.  
Crie um documento simples com:
- Campos que existirão no perfil.
- Estrutura dos posts e das reações.
- Lista dos apps Django que você criaria.
- Esboço de duas telas (pode ser à mão).

---

## ❓ Estou me baseando no livro ou inventando?

👉 **Estou me baseando na estrutura e conceitos do livro**, mas adaptei para linguagem didática de aula e adicionei contexto atualizado para Django moderno.  

✅ **Sim, o conteúdo segue o conceito do livro e o projeto SuperBook.**
