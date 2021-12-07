import re

PhoneNumRegex = re.compile(r'\d\d\d\d\d-\d\d\d\d\d\d') #sets up what it needs to look for
Mo = PhoneNumRegex.search('my number is 07484-115489') #.search() searches for variable set up on line 03 in string

# can use: result = re.match(r'\d\d\d\d\d-\d\d\d\d\d\d' , 'my number is 07484-115489') for the same effect

#print (Mo.group()) #searches through entire argument as no parameter has been passed inside .group()


PhoneNumRegex = re.compile(r'(\d\d\d\d\d)-(\d\d\d\d\d\d)') #sets up groups with paraenthesis
mo = PhoneNumRegex.search('My number is 07484-115489.')
print(mo.group(1))   #searches through for first group in this case: (\d\d\d\d\d)

# | is a pipe character :)

batRegex = re.compile(r'Bat(man|mobile|copter)') # pipe character makes it so it looks for any variation of subjects ie: batmobile, batcopter
MO = batRegex.search('Batmobile lost a wheel')
print(MO.group())