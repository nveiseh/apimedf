"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime
from django.utils import timezone

from portal.models import Poll, Choice

class PollMethodTests(TestCase):
        """
        was_published_recently() should return False for polls whose
        pub_date is in the future
        """
        def test_was_published_recently_with_future_poll(self):
            #First we create the object we expect to fail
            future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
            #Then, we test that object, to see if the object's function returns the correct value
            self.assertEqual(future_poll.was_published_recently(), False)
        
        def test_was_published_recently_old_poll(self):
            old_poll = Poll(pub_date = timezone.now() - datetime.timedelta(days=30))
            self.assertEqual(old_poll.was_published_recently(), False)
        
        def test_was_published_recently_recent(self):
            recent_poll = Poll(pub_date = timezone.now() - datetime.timedelta(hours=1))
            self.assertEqual(recent_poll.was_published_recently(), True, "HORRAY?!")
    


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
