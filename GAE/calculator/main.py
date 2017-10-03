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
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):

    def get(self):
        return self.render_template("calculator.html")

    def post(self):
        first_input = float(self.request.get("first"))
        second_input = float(self.request.get("second"))
        calculation = self.request.get("calculation")

        output = None

        if calculation == "+":
            output = first_input + second_input

        elif calculation == "-":
            output = first_input - second_input

        elif calculation == "*":
            output = first_input * second_input

        elif calculation == "/":
            output = first_input / second_input

        return self.render_template("calculator.html",
                                    params={"first": first_input, "second": second_input, "calculate": output})

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()