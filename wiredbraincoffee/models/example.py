from future.utils import python_2_unicode_compatible
from six import u


@python_2_unicode_compatible
class Example(object):
    def __str__(self):
        return u'banana'


print(Example())
