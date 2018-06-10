from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-create_at')
