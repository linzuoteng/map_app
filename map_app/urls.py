from django.urls import path
from . import views
from django.contrib import admin
from .views import AddressList, AddressDetail, AddressCreate, LoginView, RegisterUser, AddressUpdate, AddressDelete, MonsterInfo, random
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AddressList.as_view(), name="address"),
    path('address/<int:pk>/', AddressDetail.as_view(), name="address_detail"),
    path('create_address/', AddressCreate.as_view(), name="create_address"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="address"), name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('edit_address/<int:pk>/', AddressUpdate.as_view(), name="edit_address"),
    path('delete_address/<int:pk>/', AddressDelete.as_view(), name="delete_address"),
    path('monsterinfo_list/', MonsterInfo.as_view(), name="monsterinfo_list"),
    path('random_monster/', random),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
