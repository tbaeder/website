
# Including another URLconf
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
from django.conf.urls import url, include
from django.contrib import admin

from resume.views import *
from django.views.generic import RedirectView
#
urlpatterns = [
    #url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^admin/', admin.site.urls),
    url(r'^contactme/$', contact, name="contact"),
    url(r'^projects/$', projects, name="projects"),
    url(r'^home/$', home, name="home"),
    url(r'^myresume/(?P<id>\d*)$', resume, name="resume"),
    url(r'^myresume/$', resume, name="resume"),
    url(r'^messages/$', MessageListView.as_view(), name="messages"),
    url(r'^messages/delete/$', delete_message, name="delete_message"),
    url(r'^', RedirectView.as_view(url='/home/')),
]
