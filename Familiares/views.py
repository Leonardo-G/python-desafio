from pydoc import doc
from django.http import HttpResponse
from django.template import loader
from Familiares.models import Familiares;

def getFamilia(self):
    familia = Familiares.objects.all();
    
    obj = {
        "familiares": familia
    }

    plantilla = loader.get_template("familiares.html");
    documento = plantilla.render(obj);
    
    return HttpResponse(documento);