from django import forms
from .models import BlogPost,Entry
class TopicForm(forms.ModelForm):
  class Meta:
    model=BlogPost
    fields=['title','text']
    labels={'title':'Title',
            'text':'Text',
            }
    widgets = {
            'title': forms.Textarea(attrs={
                'rows': 1,
                'placeholder': '请输入标题…'
            }),
            'text': forms.Textarea(attrs={
                'rows': 8,
                'placeholder': '请输入正文内容（支持markdown）…'
            }),
        }
class EntryForm(forms.ModelForm):
  class Meta:
    model=Entry
    fields=['text']
    labels={'text':''}
    widgets={'text':forms.Textarea(attrs={'cols':80,
                                          'placeholder': '请输入评论内容（支持markdown）…',
                                          })}