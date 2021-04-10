import os
from distutils.core import setup


def read(*p):
    """Utility function to read files relative to the project root"""
    return open(os.path.join(os.path.dirname(__file__), *p)).read()


setup(
    name='cached_markdown_field',
    version='0.0.1',
    packages=['cached_markdown_field'],
    url='https://github.com/pehala/cached-markdown-field',
    license='MIT',
    author='Petr Hála',
    author_email='halapetr@selfnet.cz',
    description='Cached Markdown field for Django and django-markdownx',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    keywords='django cache markdown field',
    tests_require=[
        'pytest',
        'pytest-django',
        'pytest-mock',
        'django',
        'django-composite-field',
        'django-markdownx'
    ],
    install_requires=[
        'django',
        'django-composite-field',
        'django-markdownx'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
