from django.shortcuts import HttpResponse,render,redirect
def login(request):
    error_msg=''
    if request.method=='POST':
        email=request.POST.get('email',None)
        pwd=request.POST.get('pwd',None)
        if email=='1220264596@qq.com' and pwd=='12345678':
            return redirect('http://www.jd.com')
        else:
            error_msg='邮件或者密码错误'
    return render(request,'.\login.html',{'error':error_msg})
# Create your views here.
