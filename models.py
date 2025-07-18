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

class Post(models.Model):
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name="posts")
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.codinome}: {self.mensagem[:30]}..."

class Like(models.Model):
    heroi = models.ForeignKey(Hero, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('heroi', 'post')

    def __str__(self):
        return f"{self.heroi.codinome} curtiu {self.post.id}"

# Observação:
# Se quisermos ManyToMany automático, poderíamos usar:
# likes = models.ManyToManyField(Hero, related_name="curtidas")
# O Django criaria a tabela associativa automaticamente.
