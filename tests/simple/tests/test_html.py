from django.template.loader import render_to_string
from django.test import TestCase
from with_asserts.case import TestCase as HTMLTestCase
from with_asserts.mixin import AssertHTMLMixin

import lxml.html


class AssertHTMLMixinTest(TestCase, AssertHTMLMixin):
    def test_document(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertHTML(rendered) as html:
            self.assertIsInstance(html, lxml.html.HtmlElement)
            self.assertEqual('Selector Test', html.find('head/title').text)

    def test_selector_class(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertHTML(rendered, '.product') as elems:
            self.assertEqual(2, len(elems))
            self.assertEqual('Subpage 3', elems[0].text)
            self.assertEqual('Subpage 4', elems[1].text)

    def test_destructuring(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertHTML(rendered, '.product') as (li1, li2):
            self.assertEqual('Subpage 3', li1.text)
            self.assertEqual('Subpage 4', li2.text)

    def test_selector_id(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertHTML(rendered, '#example-div') as (elem,):
            self.assertIsInstance(elem, lxml.html.HtmlElement)

            self.assertEqual('Example Div By ID', elem.text)

    def test_selector_attribute(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertHTML(rendered, 'input[name="email"]') as (elem,):
            self.assertEqual('test@example.com', elem.value)

    def test_selector_not_present(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertRaises(AssertionError) as cm:
            with self.assertHTML(rendered, '.not-real'):
                # should not be executed
                raise Exception()

        self.assertEqual(
            'No selector matches found for .not-real',
            str(cm.exception)
        )

    def test_element_id(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertHTML(rendered, element_id='example-div') as elem:
            self.assertEqual('Example Div By ID', elem.text)

    def test_element_id_not_present(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertRaises(AssertionError) as cm:
            with self.assertHTML(rendered, element_id='not-real'):
                # should not be executed
                raise Exception()

        self.assertEqual(
            'Element with id, not-real, not present',
            str(cm.exception)
        )

    # def test_expected_attrs(self):
    #     resp = self.client.get('/template/selectors/')

    #     self.assertHTML(resp, 'input[name="email"]', expected_attrs={
    #     })


class AssertNotHTMLTest(TestCase, AssertHTMLMixin):
    def test_not_present(self):
        rendered = render_to_string('tests/selectors.html')

        self.assertNotHTML(rendered, '.not-real')

    def test_present(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertRaises(AssertionError):
            self.assertNotHTML(rendered, '.product')


class HTMLTestCaseTest(HTMLTestCase):
    def test_assert_not_html(self):
        rendered = render_to_string('tests/selectors.html')

        self.assertNotHTML(rendered, '.not-real')

    def test_assert_html(self):
        rendered = render_to_string('tests/selectors.html')

        with self.assertHTML(rendered) as html:
            self.assertIsInstance(html, lxml.html.HtmlElement)
            self.assertEqual('Selector Test', html.find('head/title').text)

# TODO:
# expected_tag
# expected_attrs
