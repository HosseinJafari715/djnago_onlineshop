from django.urls import path

from .views import payment_process, payment_callback, payment_callback_sandbox, payment_process_sandbox

app_name = 'payment'


urlpatterns = [
    path('process/', payment_process, name='payment_process'),
    path('callback/', payment_callback, name='payment_callback'),

    # Sandbox
    # path('process/', payment_process_sandbox, name='payment_process'),
    # path('callback/', payment_callback_sandbox, name='payment_callback'),
]

