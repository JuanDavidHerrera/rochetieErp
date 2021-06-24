from django.conf import settings

def user_profile(request):
    profile_pic = getattr(request.user,'profile_pic', None)
    if profile_pic is None or not profile_pic:
        profile_pic = f'{settings.STATIC_URL}img/user.png'
    else:
        profile_pic = profile_pic.url
    return{"user_pic": profile_pic}