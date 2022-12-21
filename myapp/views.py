from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.urls import reverse  
from django.contrib import messages
from django.contrib.auth import authenticate, login  as authlogin,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.signals import user_logged_out

from django.core.mail import send_mail
# Create your views here.



def home(request):
  return render(request,'home.html')


#-----------------------------------------------------------------------------------------------#
@csrf_exempt
def userprofileview(request):
  form_class =  UserProfileForm
  form = form_class
  # import pdb;pdb.set_trace()
  if request.user.is_authenticated:
    user = UserProfile.objects.get_or_create(id=request.user.id)
    if request.method == 'POST':
       form =UserProfileForm(request.POST,request.FILES)
       if form.is_valid():
        form.save()
       return HttpResponse("Your Page Succesfully created")

  return render(request, "index.html", {'form': form,'user':user})





@csrf_exempt
def update_profile(request):
    # import pdb;pdb.set_trace()
    if request.user.is_authenticated:
    
      data = UserProfile.objects.get(user=request.user.id)
      if data is not None:
        # import pdb;pdb.set_trace()
        if request.method == 'POST':
          form = UserProfileForm(request.POST, instance=request.user)
          if form.is_valid():
            form.save()
          return HttpResponse("Updated")
        else:
          form = UserProfileForm()
       
      # return render(request, 'index.html', {'form':form,'data':a})
    return render(request, 'updateprofile.html', {'form':form,'data':data})






def delete_profile(request):
  # import pdb;pdb.set_trace()
  if request.user.is_authenticated:
    if request.user is not None:
      try:

       user = UserProfile.objects.get(user=request.user.id)
       user.delete()
       return HttpResponse("your profile has been deleted")
      except:
  
       return HttpResponse("profile not exist")
  else:
    return redirect('/login/')

  




def profilelist(request):
  # import pdb;pdb.set_trace()
  if request.user.is_authenticated:
    user = UserProfile.objects.all()
    
    print(user)
    return render(request,'profilelist.html',{'user':user})
    
  else:
    return HttpResponseRedirect('/login/')








def get_profile(request):
  # import pdb;pdb.set_trace()
  if request.user.is_authenticated:
    try:
      user = UserProfile.objects.get(user=request.user.id)
    except:
      return HttpResponse('user has no profile page')

    
  else:
    return HttpResponse('invalid user')
  return render(request, 'getprofile.html', {'form': user})



#--------------------------------------------------------------------------------------------------------#
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        data = User.objects.filter(username=request.user.username)
        form =UserRegisterForm(request.POST)
        

        if form.is_valid():
          
            
          


          form.save()
          return HttpResponse('user created')
            # return redirect("/login/")
    else:
        form =UserRegisterForm()
        
    return render(request,'home.html',{"form":form})



@csrf_exempt 
def login(request):
  
  if request.method == 'POST':
    # import pdb;pdb.set_trace()
    # form = UserloginForm(request=request,data=request.POST)
    form = UserloginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
    

      user=authenticate(username=username,password=password)
      if user is not None and user.is_active:
        authlogin(request,user)
        # return redirect("/profile/")
        return redirect("/profile/")
    else:
      # return HttpResponse('enter valid data')
      # if username is None:
      #   messages.error(request, 'enter username')
      # if password is None:
      #   messages.error(request, 'enter password')
      messages.error(request, 'username or password not correct')
     
      return redirect('login')

  else:
    form =UserloginForm()

  return render(request,'home.html',{"form":form})





login_required
def change_password(request):
    import pdb;pdb.set_trace()
    if request.user.is_authenticated:
    
      if request.method == 'POST':
      # import pdb;pdb.set_trace()
      
        form = PasswordChangeForm(request.user, request.POST)
        if form is not None:
          if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            # messages.success(request, 'Your password was successfully updated!')
      return redirect('/change_password/')
      # else:  
    else:   #     return HttpResponse('Please correct the error')
      form =PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {'form': form})








def logout_view(request):
    # import pdb;pdb.set_trace()
    if request.user.is_authenticated:
      # if request.user is None:
      #   return messages.add_message(request, messages.INFO,'not logged in user')
      
      logout(request)
      return (messages.add_message(request, messages.INFO,'logged Out'))
    else:
      return redirect('/login/')
    

#-------------------------------------------------------------------------------------------------------#
# from django.contrib.auth.forms import PasswordResetForm
# from django.db.models import Q
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import BadHeaderError, send_mail
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.conf import settings

# def password_reset_request(request):

#     if request.method == "POST":
#         # import pdb;pdb.set_trace()
#         domain = request.headers['Host']
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data['email']
#             associated_users = User.objects.filter(Q(email=data))
#             # import pdb;pdb.set_trace()
#             if associated_users.exists():
#                 for user in associated_users:
#                     subject = "Password Reset Requested"
#                     # import pdb;pdb.set_trace()
#                     email_template_name = "registration/password_reset_email.html"
#                     c = {
#                         "email": user.email,
#                         'domain': domain,
#                         # 'site_name': 'Interface',
#                         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                         "user": user,
#                         'token': default_token_generator.make_token(user),
#                         # 'protocol': 'http',
#                     }
#                     print(default_token_generator.make_token(user))
#                     email = render_to_string(email_template_name, c)
#                     try:
#                         send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
#                     except BadHeaderError:
#                         return HttpResponse('Invalid header found.')
#                     return redirect("password_reset/done/")
#                     # return redirect("reset/done/")
            
#     password_reset_form = PasswordResetForm()
#     return render(request=request, template_name="registration/password_reset_form.html",
#                   context={"password_reset_form": password_reset_form})





#-------------------------------------------------------------------------------------------------------#
# @csrf_exempt
# @login_required
def create_post(request):
  form_class = PostForm 
  fm = form_class
  # import pdb;pdb.set_trace()
  if request.user.is_authenticated:
      if request.method == 'POST':
          fm = PostForm(request.POST,request.FILES)
          # import pdb;pdb.set_trace()
          if int(fm.data['user_name'])==request.user.id:
            if fm.is_valid:
             fm.save()
            return HttpResponse('post')
          else:
            return HttpResponse('invailide user')
  return render(request,'index.html', {'form':fm})
  # return render(request,'updatepost.html', {'form':fm})






def delete_post(request):
  # import pdb;pdb.set_trace()
  if request.user.is_authenticated:
    if request.user is not None:
      try:
      #  data = User.objects.filter(id=request.user.id)
       data = Post.objects.filter(user_name=request.user.id).delete()
      #  a=data.post_set.all()
      #  a.delete()
      except:
        return HttpResponse('post does not exist')
      return HttpResponse('post has been deleted')
    else:
      return HttpResponse('user does not exixst')
  else:
    return redirect('/login/')





def delete_one_post(request,id):
  if request.user.is_authenticated:
    try:
      data = Post.objects.get(id=id)
      data.delete()
    except:
      return HttpResponse('post does not exist')
    return HttpResponse('delete')
  return redirect('/login/')


#----------------------------------------------------------------------------------------------#
from django.views.generic.base import View
class MyComment(View):
   form_class = CommentForm


   def get(self, request,*args, **kwargs):
      # import pdb;pdb.set_trace()
      data = Comments.objects.all()
      return render(request, "msg.html",{'data':data})
  
    
   



def createtcomment(request):
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid:
      form.save()
   
      return HttpResponseRedirect('/home/')
  else:
      form = CommentForm() 
  return render(request,"msg.html",{'form':form})



def deletecomment(request):
  import pdb;pdb.set_trace()
  try:
   data = Comments.objects.get(id=request.user.id)
   data.delete()
   return HttpResponse('deleted')  
  except:
    return HttpResponse('not created comment yetS')
  return HttpResponse('deleted')  




#_______________________________________________________________________________________________#
def like_comment(request):
  # form=LikeCommentForm()
  form_class = LikeCommentForm 
  form = form_class 

  # import pdb;pdb.set_trace()
  data = Comment_Like.objects.filter(user=request.user.id)
  if request.method == 'POST':
    form = LikeCommentForm(request.POST)
    if form.is_valid:
      form.save()
      return HttpResponse('kuchh bhi')
      # messages.success(request,'comented')
    else:
      LikeCommentForm()
  return render(request,'comment.html',{'form':form})


