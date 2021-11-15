from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),

	# user authentication
	path('register/', views.register_page, name='register'),
	path('login/', views.login_page, name='login'),
	path('logout/', views.logout_page, name='logout'),
	path('about/', views.about_page, name='about'),

	# profile and ranking
	path('profile/', views.profile_page, name='profile'),
	path('profile/settings/', views.profile_settings_page, name='profile settings'),
	path('profile/<str:qry_user>/', views.profile_page, name='profile_user'),
	path('ranking/', views.ranking_page, name='ranking'),

	 # problem
	path('problemset/', views.problemset_page, name='problemset'),
	path('problem/<int:prob_id>/', views.detail_problem, name='problem detail'),

	# blog
	path('blog/', views.blog_page, name='blog page'),
	path('blog/new/', views.create_blog_page, name='new blog'),
	path('blog/entry/<str:blog_entry>/', views.blog_entry_page, name="blog entry"),
	path('blog/entry/<str:blog_entry>/edit/', views.blog_edit_page, name="blog edit entry"),
	path('blog/entry/<str:blog_entry>/delete/', views.blog_delete_page, name="blog delete entry"),
	path('blog/entry/<str:blog_entry>/nfauthorize/', views.blog_nfauthorize_page, name="blog new feed authorize"),
	path('blog/entry/<str:blog_entry>/comment/', views.blog_comment_page, name="blog comment"),
	path('blog/entry/<str:blog_entry>/comment/<int:cmt_id>/delete/', views.delete_comment_page, name="comment delete"),
]