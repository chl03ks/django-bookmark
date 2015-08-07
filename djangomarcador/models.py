from django.contrib.auth.models import User
from django.db import models
from django.untils.encoding import python_2_unicode_compatible
from django.untils.timezone import now

@python_2_unicode_compatible
class Tag(models.Model):

    name = models.CharField(max_length=50, unique=True)


    class Meta:
       varbose_name = 'tag'
       varbose_name_plural = 'tags'
       ordering = ['name']
            
    def __str__(self):
        return self.name


@python_2_unicode_compatible
class BookMark(models.Model):

    url = models.URLField()
    title = models.CharField('title', max_length=225)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanFiedl('public', default=True)
    date_created = models.DateTimeField('date_created')
    date_updated = models.DateTimeField('date_updated')
    owner = models.ForeignKey(User, vernose_name='owner', 
        related_name='bookMarks')
    tags = models.ManyToManyField(Tag, blank=True)


    class Meta:
       varbose_name = 'bookmark'
       varbose_name_plural = 'bookmarks'
       ordering = ['-date_created']

    def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(BookMark, self).save(*args, **kwargs)

    