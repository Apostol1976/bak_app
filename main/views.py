from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.template.loader import get_template
from goods.models import Categories
from main.forms import ContactForm


def index(request):
    context={
        'title': 'Home - главная',
        'content': 'Пластиковые окна для Вашего дома',
        }
    return render(request, 'main/index.html', context)


def about(request):
    context={
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Наша компания – лидер в производстве и установке пластиковых окон на российском рынке. Наша миссия – создавать комфорт и уют в каждом доме, предлагая высококачественные, экологически чистые и энергоэффективные оконные конструкции. Мы используем передовые технологии и материалы, чтобы удовлетворить потребности самых требовательных клиентов. Мы ваш надежный партнер в создании комфортного и безопасного жилища. Мы предлагаем только лучшие решения для вашего дома, обеспечивая высокое качество, энергоэффективность и долговечность наших оконных конструкций. Обратитесь к нам, и мы сделаем ваш дом уютным и теплым!' 
        }
    return render(request, 'main/about.html', context)

    
def contakt(request):
    context={
        'title': 'Home - Контактная информация',
        'content': 'Контактная информация',
         'text_on_page': 'Адрес: Латвия, г. Рига, ул. Бривибас, д. 100, офис 20'
         }
    return render(request, 'main/contakt.html', context)

def montaz(request):
    context={
        'title': 'Home - Контактная информация',
        'content': 'Контактная информация',
         'text_on_page': 'Адрес: Латвия, г. Рига, ул. Бривибас, д. 100, офис 20'
         }
    return render(request, 'main/montaz.html', context)

def umdom(request):
    context={
        'title': 'Home - Контактная информация',
        'content': 'Контактная информация',
         'text_on_page': 'Адрес: Латвия, г. Рига, ул. Бривибас, д. 100, офис 20'
         }
    return render(request, 'main/umdom.html', context)

def remont(request):
    context={
        'title': 'Home - Контактная информация',
        'content': 'Контактная информация',
         'text_on_page': 'Адрес: Латвия, г. Рига, ул. Бривибас, д. 100, офис 20'
         }
    return render(request, 'main/remont.html', context)

def why(request):
    context={
        'title': 'Home - Почему мы',
        'content': 'Почему мы',
         'text_on_page': 'Наши окна обладают высокими теплоизоляционными свойствами, что позволяет существенно снизить затраты на отопление и кондиционирование.'
                                 ' Специальные стеклопакеты с энергосберегающим покрытием помогают сохранять тепло в зимний период и прохладу летом.'
                                 ' Использование современных материалов и технологий обеспечивает надежную звукоизоляцию, защищая ваш дом от шума улицы и создавая комфортную обстановку внутри.'
                                 ' Окна оборудованы современной фурнитурой и противовзломными системами, что обеспечивает высокий уровень безопасности.'
                                'Мы предлагаем различные варианты защиты, включая усиленные рамы и специальное стекло.'
         }
    return render(request, 'main/why.html', context)





def message(request):
    context={}
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'],form.cleaned_data['email'],form.cleaned_data['message'])
            context={'success': 1}
    else:
        form=ContactForm()
    context['form']=form
        
    return render(request, 'main/message.html', context)

def send_message(name, email, message):
    text = get_template('main/mesage.html')
    html = get_template('main/mesage.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = text.render(context)
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    
    
    


