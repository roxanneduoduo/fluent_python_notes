from functools import partial


def tag(name, *content, cls=None, **attrs):
    '''generate one or more HTML tags'''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
    
picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))
# >>> picture
print(picture.func)
print(picture.args)
print(picture.keywords)

"""
functools.partialmethod is the same with function partial, but used for method.

functools.lru_cache can do memorization
"""