#!/usr/bin/env python
import os
import random

import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class Capital:
    def __init__(self, capital, country, pic):
        self.capital = capital
        self.country = country
        self.pic = pic

def setup_data():
    accra = Capital(capital="Accra", country="Ghana", pic="/assets/accra.jpg")
    helsinki = Capital(capital="Helsinki", country="Finland", pic="/assets/helsinki.jpg")
    kiev = Capital(capital="Kiev", country="Ukraine", pic="/assets/kiev.jpg")
    belgrade = Capital(capital="Belgrade", country="Serbia", pic="/assets/belgrade.jpg")
    vientiane = Capital(capital="Vientiane", country="Laos", pic="/assets/vientiane.jpg")
    rabat = Capital(capital="Rabat", country="Morocco", pic="/assets/rabat.jpg")

    return [accra,helsinki,kiev,belgrade,vientiane,rabat]

class MainHandler(BaseHandler):
    def get(self):
        capital = setup_data()[random.randint(0, 5)]
        return self.render_template("home.html", params={"capital": capital})

class EndHandler(BaseHandler):
    def post(self):
        guess = self.request.get("guess")
        country = self.request.get("country")

        capitals = setup_data()
        for c in capitals:
            if c.country ==  country:
                if c.capital.lower() == guess.lower():
                    fin = True
                else:
                    fin = False

                return self.render_template("end.html", params={"fin":fin, "c":c})


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/end', EndHandler),
], debug=True)