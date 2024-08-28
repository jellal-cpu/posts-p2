from django.db import models 
from django.utils import timezone 
from postprj.common import CommonAbstract 


class Posts(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')
    title = models.CharField(max_length=255, verbose_name='Tiêu đề')
    description = models.TextField()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'
        db_table = 'posts'

    def __str__(self):
        return f"{self.id} - {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super(Posts, self).save(*args, **kwargs)
