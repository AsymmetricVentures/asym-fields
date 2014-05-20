# -*- coding: utf-8 -*-
#    Asymmetric Base Framework :: Fields
#    Copyright (C) 2013-2014  Asymmetric Ventures Inc.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
from django.conf import settings
import sys

try:
	import django #@UnusedImport
except ImportError:
	print("Error: django is required to run tests")
	sys.exit(1)

try:
	import six #@UnusedImport
except ImportError:
	print("Error: six is required to run tests")
	sys.exit(-1)


def main():
	settings.configure(
		INSTALLED_APPS = (
			'django.contrib.auth',
			'django.contrib.contenttypes',
			'django.contrib.admin',
			'django.contrib.sessions',
			'asymm_fields.tests.testapp',
			'asymm_fields'
		),
		DATABASE_ENGINE = 'django.db.backends.sqlite3',
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.sqlite3',
				'NAME': ':memory:',
			}
		},
		DEBUG = True,
		TEMPLATE_DEBUG = True,
	)
	if django.get_version() >= '1.7':
		django.setup() #@UndefinedVariable
	
	apps = ['asymm_fields']
	if django.get_version() >= '1.6':
		apps.append('asymm_fields.tests.testapp')
		apps.append('asymm_fields.tests')
	
	from django.core.management import call_command
	from django.test.utils import get_runner
	
	try:
		from django.contrib.auth import get_user_model
	except ImportError:
		USERNAME_FIELD = 'username'
	else:
		USERNAME_FIELD = get_user_model().USERNAME_FIELD
	
	class TestRunner(get_runner(settings)):
		def setup_databases(self, *args, **kwargs):
			result = super(TestRunner, self).setup_databases(*args, **kwargs)
			kwargs = {
				'interactive': False,
				'email': 'admin@example.com',
				USERNAME_FIELD: 'admin'
			}
			call_command('createsuperuser', **kwargs)
			return result
	
	failures = TestRunner(verbosity = 2, interactive = True).run_tests(apps)
	sys.exit(failures)

if __name__ == '__main__':
	main()