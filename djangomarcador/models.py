from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

@python_2_unicode_compatible
class Tag(models.Model):

    name = models.CharField(max_length=50, unique=True)


    class Meta:
       verbose_name = 'tag'
       verbose_name_plural = 'tags'
       ordering = ['name']
            
    def __str__(self):
        return self.name


class PublicBookmarkManager(models.Model):
    def get_queryset(self):
        query = super(PublicBookmarkManager, self).get_queryset()
        return query.filter(is_public=True)    


@python_2_unicode_compatible
class BookMark(models.Model):

    url = models.URLField()
    title = models.CharField('title', max_length=225)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    date_created = models.DateTimeField('date_created')
    date_updated = models.DateTimeField('date_updated')
    owner = models.ForeignKey(User, verbose_name='owner', 
        related_name='bookMarks')
    tags = models.ManyToManyField(Tag, blank=True)

    obeject = models.Manager()
    public = PublicBookmarkManager()


    class Meta:
       verbose_name = 'bookmark'
       verbose_name_plural = 'bookmarks'
       ordering = ['-date_created']

    def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(BookMark, self).save(*args, **kwargs)

    