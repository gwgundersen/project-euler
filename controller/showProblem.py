import os
import webapp2
import jinja2 

from q11.orm.gdbEntities import *
from q11.controllers.webHandlers.baseHandler import *
from q11.security.auth import *

template_path = os.path.normpath(os.path.dirname(__file__)+"../../../.."+os.environ["TEMPLATE_PATH"])
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

class ShowDashboard(BaseHandler):

    @user_required
    def get(self, **kwargs):
        userToken = self.auth.get_user_by_session()
        user = self.auth.store.user_model.get_by_auth_token(userToken['user_id'], userToken['token'])
        orm = Q11Db()
        currentUser = orm.get_user_by_email(user[0].auth_ids[0])
        if not currentUser:
            self.redirect_to('/login')

        eventCode = None
        if kwargs and kwargs['event']:
            eventCode = kwargs['event']
            ae = orm.get_event_by_code(eventCode)
            if ae:
                orm.set_active_event(currentUser.userId, ae.eventId)
            else:
                self.redirect('/event/new')
        else:
            ae = orm.get_event_by_code(currentUser.activeEvent)

        if not ae:
            self.redirect('/event/new')

        event_list = orm.get_events_for_coordinator(currentUser.userId)
        active_event_details = orm.get_event_details(ae.eventId)

        template_data = {
            "title" : "Event Details",
            "events": event_list,
            "event" : active_event_details,
            "user"  : currentUser
        }

        template = jinja_env.get_template('dashboard.tpl.html')
        self.response.write(template.render(template_data))
