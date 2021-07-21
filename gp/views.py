from project.models import Rec, Imaage
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

img_height = 224
img_width = 224

#model = pickle.load(open('/home/YoussefFekry/django-projects/mysite/static/TDCMv1.1.h5', 'rb'))
#model = pd.read_hdf(r'/home/YoussefFekry/django-projects/mysite/static/TDCMv1.1.h5')
model = load_model('/home/YoussefFekry/django-projects/mysite/static/TDCMv1.1.h5')

class firstpage(CreateView):
    model = Imaage
    fields = ['imagefile']
    template_name = "project/firstPage.html"
    success_url = reverse_lazy('project:state')

def state(request):
    lastimage= Imaage.objects.order_by('-id')[0]

    testimg = '/home/YoussefFekry/django-projects/mysite/media/'+str(lastimage.imagefile)
    img = image.load_img(testimg, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x/255
    x = x.reshape(1, img_height, img_width, 3)
    predi = model.predict(x)
    label = np.argmax(predi[0])

    #as2l mohab
    label = label + 1

    recomend = Rec.objects.get(pk=label)

    ctx = {'recomend' : recomend,'myimage' : lastimage}
    return render(request, "project/recPage.html", ctx)








