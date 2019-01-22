import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

"""
>>> htmlize({1, 2, 3})
>>> htmlize(abs)
>>> htmlize('Heimlich & Co.\n -a game')
>>> htmlize(42)
>>> print(htmlize(['alpha', 66, {3, 2, 1}]))
"""
