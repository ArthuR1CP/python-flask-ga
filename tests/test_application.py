import unittest
from application import application
from flask import template_rendered
from contextlib import contextmanager
import re

@contextmanager
def captured_templates(application):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, application)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, application)

class Tests(unittest.TestCase):

    def test_health_endpoint(self):
        with application.test_client() as c:
            r = c.get('/health')
            self.assertTrue(b'UP' in r.data)

    def test_index(self):
        with application.test_client() as c:
            with captured_templates(application) as templates:
                r = c.get('/')
                template, context = templates[0]

                #print(template)
                self.assertEqual(re.findall(r'index.html', str(template))[0], 'index.html')
                self.assertEqual(context['greeting'], 'Artur')

    def test_rcode(self):
        with application.test_client() as c:
            r = c.get('/')
            self.assertEqual(r.status_code, 200)



if __name__ == '__main__':
    unittest.main()
