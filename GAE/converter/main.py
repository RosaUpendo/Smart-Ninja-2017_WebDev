#!/usr/bin/env python
import os
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


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("home.html")

class Converter(BaseHandler):
    def post(self):
        first = float(self.request.get("quantity"))
        convert_1 = self.request.get("inp")

        second = None
        convert_2 = None

        if convert_1 == "miles":
            second = first * 1.609
            convert_2 = "kilometers"
        elif convert_1 == "km":
            second = first * 0.621
            convert_2 = "miles"

        return self.render_template("fin.html", params={"first":first, "second":second, "con_1": convert_1, "con_2":convert_2})

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/fin', Converter),

], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')


if __name__ == '__main__':

    main()
