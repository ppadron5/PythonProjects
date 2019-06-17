import repositorycsv

myWonderZoo = repositorycsv.getWonderZoo()

visitorName = input('Welcome to ' + str(myWonderZoo.name) + ' . What is your name: ')

while myWonderZoo.isActive:
  print('')
  print ('Your location is ' + str(myWonderZoo.currentExib.name))
  if myWonderZoo.currentExib.animalHere is None:
    print('  There Is No Animal Here')
  else:
    print(' There Is An Animal Here')
    print(' Ask:')
    print('    What Animal')
    print('    What Sound')
    print('    What Info')
  print('  Animal Options')
  print('  You can go:')
  for direction in myWonderZoo.currentExib.neighbors:
    neighborID = myWonderZoo.currentExib.neighbors[direction]
    print('   ' + direction + ' to ' + myWonderZoo.allExibs[neighborID].name)
  if myWonderZoo.currentExib.hasExit:
    print('   Exit')

  locationIsSame = True
  while locationIsSame:
    choice = input('What do you want to do ' + str(visitorName) + '?' .lower())
    if choice.lower() == 'exit' and myWonderZoo.currentExib.hasExit:
      myWonderZoo.leave()
      locationIsSame = False
    if choice in myWonderZoo.currentExib.neighbors.keys():
      newStallID = myWonderZoo.currentExib.neighbors[choice]
      myWonderZoo.goToExib(newStallID)
      locationIsSame = False
    if choice == 'What Animal':
      print(myWonderZoo.currentExib.animalHere.whatKindOfAnimal())
    if choice == 'What Sound' :
      print(myWonderZoo.currentExib.animalHere.animalSound())
    if choice == 'What Info' :
      print(myWonderZoo.currentExib.animalHere.animalInfo())


print('Good bye ' + str(visitorName) + ' please come back another day.')
