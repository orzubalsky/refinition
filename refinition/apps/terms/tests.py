"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from datetime import *
from terms.models import *


class VersionTestCase(TestCase):
    """ test version """
    def setUp(self):
        pass

    def test_version(self):
        """
        """
        pass