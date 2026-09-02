from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="notes", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class Bookmark(models.Model):
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.url
