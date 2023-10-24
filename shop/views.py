from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Profile
from .forms import ReviewForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .filters import ProductFilter
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm


def product_list(request):
    products = Product.objects.filter(status=Product.Status.AVAILABLE)
    product_filter = ProductFilter(request.GET, queryset=products)

    if 'reset' in request.GET:
        return redirect('shop:product_list')

    return render(request,
                  'shop/product/list.html',
                  {'products': products,
                   'filter': product_filter})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                status=Product.Status.AVAILABLE)
    reviews = product.reviews.all()
    review_form = ReviewForm()
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'reviews': reviews,
                   'review_form': review_form,
                   'cart_product_form': cart_product_form})


@login_required
def product_review(request, product_id):
    product = get_object_or_404(Product, id=product_id, status=Product.Status.AVAILABLE)
    review = None

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.name = request.user
            review.save()

    else:
        form = ReviewForm()

    return render(request, 'shop/product/review.html',
                  {'product': product,
                   'form': form,
                   'review': review})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            try:
                # Попробуйте получить профиль пользователя, если он уже существует
                profile = Profile.objects.get(user=new_user)
            except Profile.DoesNotExist:
                # Если профиль не существует, создайте его
                profile = Profile(user=new_user, email=new_user.email)
                profile.save()

            return render(request, 'shop/account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'shop/account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            profile = profile_form.save(commit=False)
            profile.email = user.email
            profile.save()

            return redirect('shop:account')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'shop/account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def account(request):
    profile = Profile.objects.get(user=request.user)

    return render(request,
                  'shop/account/account.html',
                  {'profile': profile})
