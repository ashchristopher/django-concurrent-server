# django-concurrent-server #

This is a fork of James Aylett's django_concurrent_test_server. It has been updated to use
setuptools for installation allowing developers to install with package management such as
pip. 

I have also updated the package structure and command names as James made them just too darn
long. 


## Usage ##

1. Install django-concurrent-server via whatever mechanism you see fit (I suggest pip).
    _pip install -e git+git://github.com/ashchristopher/django-concurrent-server.git#egg=django-concurrent-server_
2. Add concurrent_server to your INSTALLED_APPS
3. If threads worry you, and bearing the above warning in mind, set
   CONCURRENT_THREADING = False in settings.py to use forking
4. Use ./manage.py runcserver to start a concurrent server
5. (optional) Add CONCURRENT_RANDOM_DELAY = True to your settings.py to
   introduce a small, random delay into each request; useful for finding race
   conditions. (By <http://github.com/wolever>.)
6. (option) Set RUNSERVER_DEFAULT_ADDR / RUNSERVER_DEFAULT_PORT in settings.py
   to override the defaults without having to hack the code. Useful for people
   who don't like aliases, or move things between machines a lot.


See his documentation below for relevant information about his original package.


    <http://code.djangoproject.com/ticket/3357> is a Django ticket about making the built-in dev
    server concurrent. This isn't going to happen any time soon, but one of the comments wondered
    about turning the patch in the ticket into a separate app that could be dropped in to provide a
    concurrent dev server as a new command. This is what django_concurrent_test_server does.

    Note that with the forking server, it is possible for a child process to survive when the parent
    dies; the child retains the open listen socket, so you have to find it and kill it before
    restarting the server. It should be possible to fix this, but I haven't looked into it yet; unless
    you are aware of threading problems in your code or extensions, you should probably use that for
    preference.

    Almost all the work was done by Istvan Albert, as per <http://is.gd/1h6JX> on
    <http://groups.google.com/group/django-developers/>. Additionally I've duplicated the runserver
    command from Django itself, and repackaged the whole lot.

    Given the context of the original discussion, and the presence of the patch on the Django ticket,
    I'm distributing this under the Django license with the normal "Django Software Foundation and
    individual contributors" copyright statement.

    James Aylett <http://tartarus.org/james/computers/django/>
