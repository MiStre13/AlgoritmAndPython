i = int(input('Сколько пингвинов напечатать? '))
penguin_limbs = ('_~_', '(o o)', '/ V \\', '/( _ )\\', '^^ ^^')

for limb in penguin_limbs:
	print(' '.join(['{0:^7s}'.format(limb)] * i))