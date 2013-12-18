from setuptools import setup, find_packages

setup(
    name='django-concurrent-server',
    version=__import__('concurrent_server').__version__,
    description='Provides a multi-threaded (concurrent) development sever for Django.',
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Istvan Albert, James Aylett, Ash Christopher, Pablo Martin',
    author_email='ash.christopher@gmail.ca',
    url='https://github.com/ashchristopher/django-concurrent-server',
    download_url='https://github.com/ashchristopher/django-concurrent-server',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=True, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
