from django.shortcuts import render,HttpResponseRedirect
from .models import Item,SurfItem,Transaction
from django.http import HttpResponse


def home(req):
    cart=req.session.get('cart')
    if  cart==None:
         req.session['cart']={}
    return render(req,'product/index.html')

def allitem(req):
    if req.method=="POST":
          stock=int(req.POST.get('instock'))  # 500
          required=int(req.POST.get('req_quan')) # 550
          id=int(req.POST.get('id_product')) # 2
          print(type(stock))
          print(required)
          if required >stock:
              data=Item.objects.all()
              return render(req,'product/allitems.html',{'data':data,'msg1':'Inappropriate Choice',
                                                         'id':id}) 
          cat_id="soap"+str(id)
          cart=req.session.get('cart')#  local variable
          old=cart.get(cat_id)
          if old:
               cart[cat_id]=required+old
          else:
               cart[cat_id]=required
          req.session['cart']=cart  # assign new value
          
    
    data=Item.objects.all()
    return render(req,'product/allitems.html',{'data':data})



def surf(req):
    if req.method=="POST":
          stock=int(req.POST.get('instock'))  # 500
          required=int(req.POST.get('req_quan')) # 550
          id=int(req.POST.get('id_product')) # 2
          print(type(stock))
          print(required)
          if required >stock:
              data=SurfItem.objects.all()
              return render(req,'product/allitems.html',{'data':data,'msg1':'Inappropriate Choice',
                                                         'id':id}) 
          cat_id="surf"+str(id)
          cart=req.session.get('cart')#  local variable
          old=cart.get(cat_id)
          if old:
               cart[cat_id]=required+old
          else:
               cart[cat_id]=required
          req.session['cart']=cart  # assign new value
    data=SurfItem.objects.all()
    return render(req,'product/allitems.html',{'data':data})


def cart(req):
      data=req.session.get('cart')
      print(data)
      list_final=[]
      GT=0
      for i,j in data.items():     #{'soap2': 44, 'surf2': 5}
          if "soap" in i: # "soap22"
               id= int(i[4:])
               d1=Item.objects.get(pk=id)
               price=d1.price
               total=j*price
               lis=[d1,j,total]
               list_final.append(lis)
               GT+=total
               
          if "surf" in i: # "soap22"
               id= int(i[4:])
               d1=SurfItem.objects.get(pk=id)
               price=d1.price
               total=j*price
               lis=[d1,j,total]
               list_final.append(lis)
               GT+=total
      return render(req,'product/mycart.html',{'list_final':list_final,'GT':GT})
 
         

               #print(id)
               #print(d1)
               #print(d1.price)
               #price=Item.objects.filter(id=id).values()[0].get('price')
               #print(price)


def make_payment(req):
     if req.method=="POST":
          if req.user.is_authenticated:
               user=req.user
               data=req.session.get('cart')
               for i,j in data.items(): #{'soap2': 44, 'surf2': 5}
                    if 'soap' in i:
                         cat='soap'
                         id=int(i[4:])
                         quan=j
                         ins=Transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
                         ins.save()
                    if 'surf' in i:
                         cat='surf'
                         id=int(i[4:])
                         quan=j
                         ins=Transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
                         ins.save()
               req.session['cart']={}
               return HttpResponseRedirect("/")        


             
          else:
               return HttpResponseRedirect("/auth1/login/")
               







def filter_price(req):
    if req.method=="POST" and req.POST.get('mx') :
          mx=int(req.POST.get('mx'))  # 500
          mn=int(req.POST.get('mn'))
          data=Item.products.get_product(mx,mn)
          return render(req,'product/filter.html',{'data':data})
    if req.method=="POST": 
          stock=int(req.POST.get('instock'))  # 500
          required=int(req.POST.get('req_quan')) # 550
          id=int(req.POST.get('id_product')) # 2
          print(type(stock))
          print(required)
          if required >stock:
              data=Item.objects.all()
              return render(req,'product/filter.html',{'data':data,'msg1':'Inappropriate Choice',
                                                         'id':id}) 
          cat_id="soap"+str(id)
          cart=req.session.get('cart')#  local variable
          old=cart.get(cat_id)
          if old:
               cart[cat_id]=required+old
          else:
               cart[cat_id]=required
          req.session['cart']=cart  # assign new value
          
    
    data=Item.objects.all()
    return render(req,'product/filter.html',{'data':data})




































'''
def cart(req):
    d=req.session['cart']
    print(d)
    lis_final=[]
    grant_total=0
    for i,j in d.items():
         if 'soap' in i:
              data=Item.objects.get(pk=str(i[4:]))
              price=Item.objects.filter(pk=str(i[4:])).values()[0].get('price')
              total=j*price
              l=[data,j,total]
              grant_total+=total
              lis_final.append(l)
         if 'surf' in i:
              data=SurfItem.objects.get(pk=str(i[4:]))
              price=SurfItem.objects.filter(pk=str(i[4:])).values()[0].get('price')
              total=j*price
              l=[data,j,total]
              grant_total+=total
              lis_final.append(l)
    print(lis_final)
    print(grant_total)
    return render(req,'product/cart.html',{'GT':grant_total,'list_final':lis_final})


def payment(req):
    return render(req,'product/allitems.html')

'''