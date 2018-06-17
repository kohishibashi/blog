from django import forms
from .models import Comment

# 通常のフォーム
class ImageUploadForm(forms.Form):
    file = forms.ImageField(label='画像ファイル')

class CommentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Comment
        fields = ('name','text')
