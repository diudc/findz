from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from main import views as main_views
from account import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', account_views.register, name='register'),
    path('login/', account_views.login, name='login'),
    path('logout/', account_views.logout, name='logout'),
    path('', main_views.index, name='home'),
    path('<slug:category_slug>/', main_views.category, name='category'),
    path('<slug:category_slug>/<slug:sub_category_slug>/',
         main_views.sub_category, name='sub-category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# handler404 = main.views.not_found
