from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
        
urlpatterns = [
    path("", include("apps.job.urls", namespace="job")),
    path('tinymce/', include('tinymce.urls')),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("who-we-are/", TemplateView.as_view(template_name="templates/about.html"), name="who_we_are"),
    path("group-profile/", TemplateView.as_view(template_name="templates/team.html"), name="group_profile"),
    path("our-values/", TemplateView.as_view(template_name="templates/team.html"), name="our_values"),
    path("top-management/", TemplateView.as_view(template_name="templates/team.html"), name="top_management"),
    path("corporate-culture/", TemplateView.as_view(template_name="templates/team.html"), name="corporate_culture"),
    path("certification/", TemplateView.as_view(template_name="templates/team.html"), name="certification"),
    path("contact-us/", TemplateView.as_view(template_name="templates/contact.html"), name="contact_us"),
    path("current-opening/", TemplateView.as_view(template_name="templates/services-1.html"), name="current_opening"),
    path("latest-insite/", TemplateView.as_view(template_name="templates/projects.html"), name="latest_insite"),
    path("media-coverage/", TemplateView.as_view(template_name="templates/project-details.html"), name="media_coverage"),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path(settings.ADMIN_URL, admin.site.urls),
    path("users/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", include("apps.dashboard.urls", namespace="dashboard")),
    path("chatbot/", include("apps.chatbot.urls", namespace="chatbot")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("400/", default_views.bad_request, kwargs={"exception": Exception("Bad Request!")},),
        path("403/", default_views.permission_denied, kwargs={"exception": Exception("Permission Denied")},),
        path("404/", default_views.page_not_found, kwargs={"exception": Exception("Page not Found")},),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns