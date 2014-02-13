django-with-asserts - Clean up your template tests
=====================================================

Make your Django HTML tests more explicit and concise - and remove their dependence on the full response cycle.

Turn this::

    resp = self.client.get(reverse('/'))
    self.assertContains(
        resp,
        '<input id="id_email" type="text" name="email" maxlength="75" value="bob@example.com>',
        html=True
    )

Into this::

    html = render_to_string('homepage.html',  {'user': {'email': 'bob@example.com'}})
    with self.assertHTML(html, 'input[name="email"]') as (elem,):
        self.assertEqual(elem.value, 'bob@example.com')


Links
------

 * Documentation for the original version: https://django-with-asserts.readthedocs.org
 * Code: https://github.com/cnk/django-with-asserts


Running tests
-------------

1. Clone the project
2. Set up a virtual environment for your testing (`virtualenv env`) and activate it (`source env/bin/activate`)
3. Install dependencies (`pip install django, lxml, cssselect`)
4. Install this code into your virtual environment (`pip install -e path/to/django_with_asserts`)
5. Set your PYTHONPATH to include the top level directory and the tests directory::

    export PROJ_ROOT=<where your code is>
    export PYTHONPATH=${PROJ_ROOT}/django-with-asserts:${PROJ_ROOT}/django-with-asserts/tests

6. From within the tests directory, run `django-admin.py test --settings=project.settings`
