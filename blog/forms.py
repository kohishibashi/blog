from django import forms

# 通常のフォーム
class ImageUploadForm(forms.Form):
    file = forms.ImageField(label='画像ファイル')
