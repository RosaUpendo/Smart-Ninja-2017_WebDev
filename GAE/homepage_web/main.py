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
        result = self.render_template("home.html", params={})
        return result

class AboutHandler(BaseHandler):
    def get(self):
        result = self.render_template("about_me.html")
        return result

class ProjectsHandler(BaseHandler):
    def get(self):
        result = self.render_template("my_projects.html", params={})
        return result

class BlogHandler(BaseHandler):
    def get(self):
        result = self.render_template("blog.html")
        return result

class ContactHandler(BaseHandler):
    def get(self):
        result = self.render_template("contact.html")
        return result

class LinksHandler(BaseHandler):
    def get(self):
        result = self.render_template("links.html")
        return result

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/about_me', AboutHandler),
    webapp2.Route('/my_projects', ProjectsHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/contact', ContactHandler),
    webapp2.Route('/links', LinksHandler)

], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')


if __name__ == '__main__':

    main()
