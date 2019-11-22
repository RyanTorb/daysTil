from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('cal', views.CalendarView, name='calendar'),
    path('cal/<int:offer_id>', views.CalSpecifics, name='cal_specs'),
    path('feed', views.FeedView, name='feed'),
    path('feed/<int:requests_id>', views.FeedSpecifics, name='feed_specs'),
    path('prof/<int:Profile_id>', views.ProfSpecifics, name='prof_specs'),
    path('new_profile', views.NewProfileView, name='new_profile'),
    path('', views.LoginView, name='login'),
    path('base', views.BaseView, name='base'),
    path('profile', views.ProfileDetailsView, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('request_ride/', views.RequestView, name='request'),
    path('request_ride/<int:key>', views.edit_post, name='request_edit'),
    path('offer_ride/<int:key>', views.edit_offer, name='offer_edit'),
    path('delete_ride/<int:key>', views.delete_post, name='request_delete'),
    path('delete_offer/<int:key>', views.delete_offer, name='offer_delete'),
    path('delete_signup/<int:key>', views.delete_signup, name='del_signup'),
    path('sign_up/<int:key>', views.SignUpOffer, name='signupoffer'),
    path('offer_ride/', views.OfferView, name='offer'),
    path('edit_profile', views.EditProfileView, name='edit_profile'),
    path('searchreq/', views.SearchReqResultsView, name='search_results_req'),
    path('searchoff/', views.SearchOffResultsView, name='search_results_off')
]
