from django.db import models


class Lead(models.Model):
    name = models.CharField("Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=50)
    source = models.CharField("Источник формы", max_length=50, default="hero")
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.name} ({self.phone})"


class HeroBanner(models.Model):
    image = models.ImageField("Фото", upload_to="hero/")
    is_active = models.BooleanField("Активно", default=True)

    class Meta:
        verbose_name = "Фото Hero"
        verbose_name_plural = "Фото Hero"

    def __str__(self):
        return f"Hero фото #{self.pk}"


class Product(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="products/", blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["order"]

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Фото", upload_to="projects/")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["order"]

    def __str__(self):
        return self.title