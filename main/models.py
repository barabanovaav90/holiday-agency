from django.db import models

class Service(models.Model):
    title = models.CharField("Название услуги", max_length=200)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField("Фото", upload_to='services/', blank=True, null=True)
    keywords = models.CharField("Ключевые слова", max_length=500, blank=True, help_text="Через запятую")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст новости")
    date = models.DateTimeField("Дата публикации", auto_now_add=True)
    image = models.ImageField("Фото", upload_to='news/', blank=True, null=True)
    keywords = models.CharField("Ключевые слова", max_length=500, blank=True, help_text="Через запятую")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-date']

class Portfolio(models.Model):
    title = models.CharField("Название события", max_length=200)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Фото", upload_to='portfolio/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект портфолио"
        verbose_name_plural = "Портфолио"

class ContactMessage(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата отправки", auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения обратной связи"
        ordering = ['-created_at']
