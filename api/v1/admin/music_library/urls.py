from django.urls import path
from api.v1.admin.music_library import views

urlpatterns = [
    # LICENSE
    path('license/create/', views.AdminLicenseCreateView.as_view()),
    path('license/list/', views.AdminLicenseListView.as_view()),
    path('license/detail/<int:pk>/', views.AdminLicenseDetailView.as_view()),
    path('license/update/<int:pk>/', views.AdminLicenseUpdateView.as_view()),
    path('license/delete/<int:pk>/', views.AdminLicenseDeleteView.as_view()),

    # Album
    path('album/create/', views.AdminAlbumCreateView.as_view()),
    path('album/list/', views.AdminAlbumListView.as_view()),
    path('album/detail/<int:pk>/', views.AdminAlbumDetailView.as_view()),
    path('album/update/<int:pk>/', views.AdminAlbumUpdateView.as_view()),
    path('album/delete/<int:pk>/', views.AdminAlbumDeleteView.as_view()),

    # Track
    path('track/create/', views.AdminTrackCreateView.as_view()),
    path('track/list/', views.AdminTrackListView.as_view()),
    path('track/detail/<int:pk>/', views.AdminTrackDetailView.as_view()),
    path('track/update/<int:pk>/', views.AdminTrackUpdateView.as_view()),
    path('track/delete/<int:pk>/', views.AdminTrackDeleteView.as_view()),
]
