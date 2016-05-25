Safe Int
=======================

Construct integer within a given range to prevent DoS attacks.

Pulling data from the Internet and feeding it to Python's builtin int function exposes you to a potential DoS attack. Python supports arbitrary precision integers. Unlike other languages like C++, Java or even Javascript which will eventually overflow, Python can represent any number you have the memory to store. For instance, in the following code::

    s = '9' * 1000000  # Generate a string with one million 9s
    i = int(s)

Python keeps on going and will stuff 10^1000000 - 1 into i after 7 seconds of CPU work and 400kb of RAM. 7 seconds during which your gevent based web server cannot perform a context switch and service other requests. A single machine running a few hundred greenlets on a cable modem would be enough to cripple a web server with APIs that accepts integers.

safeint.int is a drop-in replacement for int to help parse untrusted data coming from the Internet. You use it like this::

    import safeint


    def my_controller():
        foo = safeint.int(bottle.request.query.foo) 


By default safeint.int will raise a ValueError if your input string is too long.  The default is 10 digits, but you can raise or lower that as your application requires with the keyword parameter digits. So for example, safeint.int(foo, digits=2) limits you to numbers in the range -9 to 99 inclusive.  

safeint.int also supports a few extra parameters and features beyond what int normally supports. If you pass it None or an empty string it returns None, saving you from the hassle of writing code that looks like this:: 

    if bottle.request.query.foo is None:
        foo = None
    else:
        foo = int(bottle.request.query.foo)

Instead you can write this::

    import safeint


    foo = safe.int(bottle.request.query.foo) 

safe.int also has some syntactic sugar to save time when enforcing bounds.   Instead of writing this::

    import safeint


    foo = safeint.int(bottle.request.query.foo)
    if foo > high:
        raise ValueError(...) 
    elif foo < low:
        raise ValueError(...) 


you can just write this::

    import safeint


    foo = safeint.int(bottle.request.query.foo, low=low, high=high)


Development
-----------

Bug reports and pull requests welcome!


Acknowledgments
---------------

Peloton_ for supporting open source!

.. _Peloton: https://www.pelotoncycle.com/

Dan Sokolsky and Adam DePrince for implementing this solution!


