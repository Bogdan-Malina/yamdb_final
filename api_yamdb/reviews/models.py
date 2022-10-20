from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User


class Category(models.Model):
    name = models.CharField(
        'Имя',
        max_length=200,
    )

    slug = models.SlugField(
        'Слуг',
        unique=True
    )


class Genre(models.Model):
    name = models.CharField(
        'Имя',
        max_length=200,
    )

    slug = models.SlugField(
        'Слуг',
        unique=True
    )


class Title(models.Model):
    name = models.CharField(
        'Имя',
        max_length=200,
    )

    year = models.IntegerField(
        'Год',
        null=True,
        blank=True,
        db_index=True
    )

    description = models.CharField(
        'Описание',
        null=True,
        blank=True,
        max_length=200,
    )

    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанр'
    )

    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория'
    )


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор публикации',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(10, 'Оценка не может превышать 10'),
            MinValueValidator(1),
        ],
        verbose_name='Оценка',
    )

    class Meta:
        """
        На одно произведение пользователь
        может оставить только один отзыв.
        """
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ('author', 'title',)

        ordering = (
            '-pub_date',
        )


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пользователь',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата комментария',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = (
            '-pub_date',
        )
