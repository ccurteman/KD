from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from users import views as user_views
from knuckledragger.views import lobby, room, landing, create_npc, create_item, create_room, create_pc, create

admin.autodiscover()

urlpatterns = [
    path("", landing, name="landing"),
    # path('account/', user_views.account, name='account'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('lobby/', login_required(lobby.as_view()), name="lobby"),
    # path('register/', user_views.register, name='register'),
    # path('room/', login_required(room.as_view()), name='room'),
    # path('admin/', admin.site.urls),
    # path('create/', create, name='create'),
    # path('create/item', create_item, name="create-item"),
    # path('create/npc', create_npc, name="create-npc"),
    # path('create/room', create_room, name="create-room"),
    # path('create/pc', create_pc, name="create-pc"),
]
