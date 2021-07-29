from django.shortcuts import render
from .models import Post
from django.http import Http404, HttpResponseRedirect
from .forms import UpdkhbtForm
# Create your views here.


def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'pages/mydkhbt.html', Data)


def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Ui chao !! Trang này không tồn tại. Bạn kiểm tra lại đường dẫn nhé.\n Nếu có gì bất thường hãy liên hệ qua phần Contact giúp mình.")
    return render(request, 'pages/postdkhbt.html', {'post': post})


def up(request):
    form = UpdkhbtForm()
    if request.method == 'POST':
        form = UpdkhbtForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mydkhbt')
    return render(request, 'pages/updkhbt.html', {'form': form})
