from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
  """用户A发的博客"""
  title=models.CharField(max_length=50)
  # 标题
  date_added=models.DateTimeField(auto_now_add=True)
  # 编辑日期
  text=models.TextField(default="")
  # Blog内容
  owner=models.ForeignKey(User,on_delete=models.CASCADE)
  def __str__(self):
    return self.title
class Entry(models.Model):
  """用户B对此的评论"""
  topic=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
  text=models.TextField()
  date_added=models.DateTimeField(auto_now_add=True)
  owner=models.ForeignKey(User,on_delete=models.CASCADE)
  class Meta:
    verbose_name_plural='entries'
  def __str__(self):
    """返回一个表示条目的简单字符串"""
    res=self.text[:50]
    if(len(self.text)>50):res+="..."
    return res