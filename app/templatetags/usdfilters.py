from django import template
register=template.Library()
def Swap(value):
    return value.swapcase()

def CharCheck(value,arg):
    count=0
    for a in range(len(value)):
        if value[a:len(arg)+a]==arg:
            count=count+1
    return count

def Remove(value,arg):
    return value.replace(arg,'')
register.filter('Swaping',Swap)
register.filter('CharCheck',CharCheck)
register.filter('Remove',Remove)