from django.shortcuts import render
from django.http import HttpResponse
from .forms import QRCodeForm
import qrcode
import os 
from django.conf import settings

def generator(request):
    if request.method == 'POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            res_name=form.cleaned_data['restaurant_name']
            url=form.cleaned_data['url']
            
            print(res_name,url)
            
            #Generate QR code
            qr=qrcode.make(url)
            file_name=res_name.replace(" ","_").lower()+"_qr.png"
            file_path=os.path.join(settings.MEDIA_ROOT, file_name) #media/file_name_menu.png
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)  # Ensure media directory exists
            qr.save(file_path)
            print("Saving QR to:", file_path)
  
            #create image url
            qr_url=os.path.join(settings.MEDIA_URL, file_name)
            
            context={
                'res_name': res_name,
                'qr_url': qr_url,
                'file_name': file_name,
            }
            print("res_name\nqr_url\nfile_name")
            return render(request,'qr_result.html',context)

    else:      
        form=QRCodeForm()
        context={
            'form':form,
        }
        
        return render(request, "index.html",context)
