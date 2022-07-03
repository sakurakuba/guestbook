from django.db import models

# Create your models here.
STATUS_CHOICES = [('active', 'actual'), ('blocked', 'banned')]


class Book(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name='Author', default='Unknown')
    email = models.EmailField(max_length=254, null=False, blank=False, verbose_name='Email')
    content = models.TextField(max_length=3000, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, blank=False, verbose_name='Status', default=STATUS_CHOICES[0][0])

    def __str__(self):
        return f"{self.id}. {self.author}: {self.email}, {self.status}"

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
