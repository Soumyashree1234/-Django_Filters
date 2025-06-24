from django.shortcuts import render

# Create your views here.
#Builtin_filters
def Builtin_filters(request):
    import datetime
    d={'data':'this is a builtin filters class','dt':datetime.datetime.now,'c':5}
    return render(request,'Builtin_filters.html',d) 

#Userdefined_Filters
def Userdefined_Filters(request):
    import datetime
    d={'data':'this is a builtin filters class'}
    return render(request,'Userdefined_Filters.html',d) 
