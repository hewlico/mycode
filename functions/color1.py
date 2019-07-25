import crayons

print(crayons.red('Red txt'))
print('{} white {}'.format(crayons.red('red'),crayons.blue('blue')))

crayons.disable()
print('{} white {}'.format(crayons.red('red'),crayons.blue('blue')))


crayons.DISABLE_COLOR=False

print(crayons.red('red string', bold=True))
print(crayons.yellow('yellow string', bold=True))
