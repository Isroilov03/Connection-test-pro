from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=150, verbose_name="Telfon Raqam", unique=True)
    avatar = models.ImageField(upload_to='user_img/')

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return self.username


class Seller(models.Model):
    user_id = models.OneToOneField(to='User', on_delete=models.CASCADE)
    account_number = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    pasport_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user_id.username


class Brand(models.Model):
    name = models.CharField(max_length=150)
    categories = models.ManyToManyField(to='Category', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    sub_category = models.ForeignKey(to="Subcategory", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sub_category.name


class Card(models.Model):
    user_id = models.ForeignKey(to='User', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    product_id = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id.username


class Saved(models.Model):
    user_id = models.ForeignKey(to='User', on_delete=models.CASCADE)
    product_id = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id.username



class Order_single_product(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    product_id = models.ForeignKey(to='Product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    branch_id = models. ForeignKey(to='Branch', on_delete=models.SET_NULL, null=True, blank=True)
    is_delivery = models.BooleanField(default=False)
    address = models.CharField(max_length=150, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    delivery_code = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    extra_phone_number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.product_id.name


class Order_by_card(models.Model):
    user_id = models.ForeignKey(to='User', on_delete=models.CASCADE)
    card_id = models.ManyToManyField(to='Card')
    branch_id = models.ForeignKey(to='Branch', on_delete=models.SET_NULL, null=True, blank=True)
    is_delivery = models. BooleanField(default=False)
    address = models.CharField(max_length=150, null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)
    delivery_code = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    extra_phone_number = models.CharField(max_length=150)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id.username


class Branch(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    product_id = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    user_id = models.ForeignKey(to='User', on_delete=models.CASCADE)
    reply_comment = models.ForeignKey(to='Comment', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id.username


class Image(models.Model):
    image = models.ImageField(upload_to='product_images/')


class Size_type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    full_name = models.CharField(max_length=150)
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE)
    seller = models.ForeignKey(to='Seller', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(to='Subcategory', on_delete=models.CASCADE)
    size_type = models.ForeignKey(to='Size_type', on_delete=models.CASCADE)
    tag = models.ManyToManyField(to='Tag')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ManyToManyField(to='Image', blank=True)
    quantity = models.IntegerField(default=0)
    is_banner = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    old_cost = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    sale_expire = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand.name








