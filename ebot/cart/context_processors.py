from .cart import Cart

#create context processors so that our cart can work on all the pages
def cart(request):
    #Return the default data from our cart
    return{'cart':Cart(request)}