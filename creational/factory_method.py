"""*What is this pattern about?
The Factory Method pattern can be used to create an interface for a
method, leaving the implementation to the class that gets
instantiated.

*What does this example do?
The code shows a way to localize words in two languages: English and
Greek. "getLocalizer" is the factory method that constructs a
localizer depending on the language chosen. The localizer object will
be an instance from a different class according to the language
localized. However, the main code does not have to worry about which
localizer will be instantiated, since the method "get" will be called
in the same way independently of the language.

*Where can the pattern be used practically?
The Factory Method can be seen in the popular web framework Django:
http://django.wikispaces.asu.edu/*NEW*+Django+Design+Patterns For
example, in a contact form of a web page, the subject and the message
fields are created using the same form factory (CharField()), even
though they have different implementations according to their
purposes.

*References:
http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
https://fkromer.github.io/python-pattern-references/design/#factory-method
https://sourcemaking.com/design_patterns/factory_method

*TL;DR80
Creates objects without having to specify the exact class.
"""

# My Chinese translator
class ChineseGetter:

    def __init__(self):
        translator = dict(dog=u"狗", cat=u"猫", bear=u"熊", grass=u"草",
                          english=u"英语")
        self.trans = translator

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:

    def get(self, msgid):
        return str(msgid)


class GreekGetter(object):
    """A simple localizer a la gettext"""

    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        return self.trans.get(msgid, str(msgid))


def get_localizer(language):
    languages = dict(English=EnglishGetter, Chinese=ChineseGetter, Greek=GreekGetter)
    return languages[language]()


if __name__ == '__main__':
    # Create our localizers
    e, c, g = get_localizer("English"), get_localizer("Chinese"), get_localizer("Greek")

    for msgid in "dog parrot cat bear english".split():
        print(e.get(msgid), c.get(msgid), g.get(msgid))
