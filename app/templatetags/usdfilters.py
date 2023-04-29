from django import template
register=template.Library()
#this are by using the decorators
@register.filter(name='Swaping') #using filter not same as function name
def Swap(value):   #when we are using different name we need to menthon name in filter()
    return value.swapcase()

@register.filter() #usign filter same as funtion name
def CharCheck(value,arg):
    count=0
    for a in range(len(value)):
        if value[a:len(arg)+a]==arg:
            count=count+1
    return count
@register.filter()
def Remove(value,arg):
    return value.replace(arg,'')



'''
#this are the normal approach
register.filter('Swaping',Swap)
register.filter('CharCheck',CharCheck)
register.filter('Remove',Remove)'''