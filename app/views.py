from django.shortcuts import render

# Create your views here.
def Builtin_filters(request):
    import datetime
    d={'data':'this is a builtin filters class','dt':datetime.datetime.now,'c':5}
    return render(request,'Builtin_filters.html',d) 