from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    """
    we need to create a form that is going to be passed to to the template that we will create for this view
    Python classses and these classes generate HTML forms for us, and some classes already exist
    render a template that uses this form and pass our form as the context to the template
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # There are different types of messages
            # messages.debug    # messages.info     # messages.success
            # messages.warning  # messages.error
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


