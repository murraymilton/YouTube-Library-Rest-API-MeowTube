from django.db import models


class Comment (models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=300)
    likes = models.IntegerField()
    video_id = models.CharField(max_length=50)
    SubComment = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}, {self.text}"




