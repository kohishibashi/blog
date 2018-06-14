from django.views import generic
from django.db.models import Q
from .models import Post
from .forms import ImageUploadForm
from PIL import Image
from django.shortcuts import render

class IndexView(generic.ListView):
    model = Post

    def get_queryset(self):
        queryset = Post.objects.order_by('-create_at')
        # base.html inputのnameにkeyword これを取得
        keyword = self.request.GET.get('keyword')
        #検索入力されてたなら filterはtitleだと全文一致
        if keyword:
            queryset = queryset.filter(
            Q(title__icontains=keyword)|Q(text__icontains=keyword)
            )
        return queryset

# 画像アップロード用
class UploadView(generic.FormView):
    template_name = 'blog/upload.html'
    form_class = ImageUploadForm

    def form_valid(self, form):
        # アップロードファイル本体を取得
        file = form.cleaned_data['file']
        # テスト表示
        Image.open(file).show()

        # 送ったファイルを使って表示する。外部ファイルを読みresultにいれるとよい
        context = {
            'result': "テスト",
        }
        return render(self.request, 'blog/result.html', context)
