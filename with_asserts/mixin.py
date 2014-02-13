from .context_manager import AssertHTMLContext, HTMLNotPresent


__all__ = ['AssertHTMLMixin']


class AssertHTMLMixin(object):
    def assertHTML(self, rendered_template,
                   selector=None, 
                   element_id=None,
                   expected=None,
                   msg=None):

        context = AssertHTMLContext(
            rendered_template,
            test_case=self,
            selector=selector,
            element_id=element_id,
            msg=msg
        )

        return context

    def assertNotHTML(self, *args, **kwargs):
        try:
            with self.assertHTML(*args, **kwargs) as html:
                # We found something, which is bad
                raise self.failureException(
                    'Found unexpected content: {0}'.format(html)
                )
        except HTMLNotPresent:
            # Actually this is good, the selector / element_id where not found
            # eat the assertion
            pass
