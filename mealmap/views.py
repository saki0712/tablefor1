from django.views import generic
from .models import Category, Shop
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class IndexView(generic.ListView):
    model = Shop
    
class DetailView(generic.DetailView):
    model = Shop
    
class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Shop
    fields = ['name', 'address', 'category']
    
    # dispathメソッドをオーバーライド
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        # 投稿者名と現在のログインユーザ名が一致しなければエラーメッセージを表示
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)
    
class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Shop
    fields = ['name', 'address', 'category']
    
    # form_validメソッドで格納する値をチェック
    def form_valid(self, form):
        # ログインしているユーザ名を投稿者名として代入
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)
    
class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy('mealmap:index')
    
class CategoryCreateView(LoginRequiredMixin, generic.edit.CreateView): 
    model = Category
    template_name = 'mealmap/category_form.html'
    fields = ['name', 'author']
    success_url = reverse_lazy('mealmap:index')    