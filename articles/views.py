from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Subscription
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'articles/index.html')


def about(request):
    return render(request, 'articles/about.html')

def contact(request):
    return render(request, 'articles/contact.html')

def articles(request):
    try:
        subscription = Subscription.objects.get(user=request.user, is_active=True)
        if subscription.plan == 'premium':
            articles = Article.objects.filter(is_deleted=False, is_premium=True)
    except:
        articles = Article.objects.filter(is_deleted=False, is_premium=False)
    context = {
        'articles': articles
    }
    return render(request, 'articles/articles.html', context)

def article(request, article_id):
    return render(request, 'articles/article.html')



@login_required(login_url='users:login')
def plans(request):
    return render(request, 'articles/plans.html')



@login_required(login_url='users:login')
def subscribe (request, paypal_subscription_id, plan):
    user = CustomUser.objects.get(email=request.user.email)
    full_name = user.full_name

    selected_plan = plan
    if selected_plan == 'monthly':
        price = 2.5
    else:
        price = 25
    
    subscription = Subscription.objects.create(
        user=request.user,
        plan=selected_plan,
        price=price,
        is_active=True,
        paypal_subscription_id=paypal_subscription_id
    )

    context = {
        'full_name': full_name,
        'selected_plan': selected_plan,
        'price': price
    }
    return render(request, 'users/profile.html', context)



