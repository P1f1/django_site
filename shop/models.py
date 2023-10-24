from django.db import models
from django.urls import reverse
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    objects = models.Manager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):

    class Status(models.TextChoices):
        SALES = 'SA', 'Sales'
        AVAILABLE = 'AV', 'Available'

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.AVAILABLE)
    objects = models.Manager()
    manufacturer = models.ForeignKey('Manufacturer',
                                     on_delete=models.CASCADE,
                                     related_name='manufacturer',)

    class Meta:
        ordering = ['status', '-stock']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.status = Product.Status.SALES

        else:
            self.status = Product.Status.AVAILABLE
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Review(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    name = models.CharField(max_length=80, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='media_rev/images', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]

    def __str__(self):
        return f'Отзыв {self.name} на {self.product}'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    email = models.EmailField()
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return f'Profile of {self.user}'
