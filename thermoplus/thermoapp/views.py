from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service_type = request.POST.get('service_type')
        message = request.POST.get('message')
        emergency = request.POST.get('emergency') == 'on'
        
        print("=" * 50)
        print("📨 درخواست جدید دریافت شد!")
        print(f"👤 نام: {name}")
        print(f"📞 تلفن: {phone}")
        print(f"📧 ایمیل: {email}") 
        print(f"🛠️ خدمات: {service_type}")
        print(f"📝 پیام: {message}")
        print(f"🚨 فوری: {emergency}")
        print("=" * 50)
        
        from django.contrib import messages
        messages.success(request, 'درخواست شما با موفقیت ثبت شد! به زودی با شما تماس می‌گیریم.')
        return redirect('thermoapp:contact')
    
    return render(request, 'contact.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)