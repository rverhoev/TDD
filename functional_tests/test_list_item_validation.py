from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home age and accidentally tries to submit
        # an empty list item. She hits Enter in the empty input box

        # The home page refreshes, and there is an error message saying
        # that lists items cannot be blank

        # She tries again with some test for the item, which now works

        # Perversely, she now decides to submit a second blank item

        # She receives a similar warning on the list page

        # And she can correct ir by filling some text in
        self.fail('wite me!')
        self.fail('Finish the test!')