from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()

class JobCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    icon = models.CharField(max_length=50, blank=True, verbose_name="Иконка")
    
    class Meta:
        verbose_name = "Категория работы"
        verbose_name_plural = "Категории работ"
    
    def __str__(self):
        return self.name

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('one_time', 'Разовая работа'),
        ('temporary', 'Временная работа'),
        ('permanent', 'Постоянная работа'),
    ]
    
    SCHEDULE_CHOICES = [
        ('full_time', 'Полный день'),
        ('part_time', 'Неполный день'),
        ('shifts', 'Сменный график'),
        ('flexible', 'Гибкий график'),
    ]
    
    PAYMENT_TYPE_CHOICES = [
        ('hourly', 'Почасовая оплата'),
        ('piecework', 'Сдельная оплата'),
        ('fixed', 'Фиксированная оплата'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название вакансии")
    description = models.TextField(verbose_name="Описание")
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs_posted', verbose_name="Работодатель")
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, verbose_name="Тип работы")
    schedule = models.CharField(max_length=20, choices=SCHEDULE_CHOICES, verbose_name="График работы")
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, verbose_name="Тип оплаты")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Зарплата")
    location = models.CharField(max_length=200, verbose_name="Местоположение")
    latitude = models.FloatField(null=True, blank=True, verbose_name="Широта")
    longitude = models.FloatField(null=True, blank=True, verbose_name="Долгота")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    
    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
    
    def __str__(self):
        return self.title

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'На рассмотрении'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
        ('completed', 'Завершено'),
    ]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications', verbose_name="Вакансия")
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications', verbose_name="Соискатель")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    applied_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    message = models.TextField(blank=True, verbose_name="Сообщение")
    
    class Meta:
        verbose_name = "Отклик на вакансию"
        verbose_name_plural = "Отклики на вакансии"
        unique_together = ('job', 'worker')
    
    def __str__(self):
        return f"{self.worker} applied for {self.job}"

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_given', verbose_name="Автор отзыва")
    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_received', verbose_name="Получатель отзыва")
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Вакансия")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оценка"
    )
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
    
    def __str__(self):
        return f"Review by {self.reviewer} for {self.reviewed_user}"