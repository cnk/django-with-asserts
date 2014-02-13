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


