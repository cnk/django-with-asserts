import lxml.html


class HTMLNotPresent(AssertionError):
    # Technically, according to the unittest.TestCase.failureException
    # documentation, we should be a subclass of that assertion...
    pass


class SelectorNotFound(HTMLNotPresent):
    pass


class ElementIDNotFound(HTMLNotPresent):
    pass


class AssertHTMLContext(object):
    """Context manager for AssertHTMLMixin.assertHTML"""

    def __init__(self, rendered_template, test_case, selector, element_id, msg):
        self.rendered_template = rendered_template
        self.test_case = test_case
        self.element_id = element_id
        self.selector = selector

        #msg = self._formatMessage(msg, standardMsg)
        #raise self.failureException(msg)

    def __enter__(self):
        # Parse the  as HTML
        html = lxml.html.fromstring(self.rendered_template)
        if self.selector is not None:
            # Use cssselect to filter the elements
            elements = html.cssselect(self.selector)

            # Ensure some data exists
            if len(elements) == 0:
                raise SelectorNotFound(
                    'No selector matches found for {0}'.format(self.selector)
                )

            return elements
        if self.element_id is not None:
            try:
                return html.get_element_by_id(self.element_id)
            except KeyError:
                raise ElementIDNotFound(
                    'Element with id, {0}, not present'.format(self.element_id)
                )

        # No filtering defined, return the entire parsed HTML document
        return html

    def __exit__(self, exc_type, exc_value, tb):
        pass
