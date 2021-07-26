from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    context={
        "articles":[
            {
                'title':'وساطت دیوید بکام فرزندانش را نجات داد',
                'desc':'دیوید بکام، ستاره مشهور و انگلیسی با وساطت خود موضوع تخلف فرزندانش در سواحل ایتالیا را حل کرده است.',
                'img':'https://static.farakav.com/files/pictures/thumb/01593057.jpg'
            },
            {
                'title':'این عجیب ترین گل تاریخ فوتبال بود؟',
                'desc':'گلن مک آئولی، بازیکن تیم اتلون تاون یکی از عجیب ترین گل های تاریخ فوتبال را به ثمر رساند.',
                'img':'https://static2.farakav.com/files/pictures/01627080.png'
            },
            {
                'title':'لواندوفسکی: می دانم این جایزه چقدر اهمیت دارد',
                'desc':'رابرت لواندوفسکی، ستاره لهستانی بایرن مونیخ مدعی شد جایزه مرد سال فوتبال آلمان به او احساس غرور داده است.',
                'img':'https://static.farakav.com/files/pictures/thumb/01604273.jpg'
            },
            {
                'title':'کریس رونالدو به تورین بازگشت',
                'desc':'از فردا شاهد حضور کریستیانو رونالدو در تمرینات  یوونتوس برای فصل جدید خواهیم بود',
                'img':'https://static2.farakav.com/files/pictures/01627073.jpg'
            },
        ]
    }
    return render(request,"blog/home.html",context)
