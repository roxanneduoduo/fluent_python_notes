charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print([id(people) for people in (charles, lewis)])
lewis['balance'] = 950
print(charles)
