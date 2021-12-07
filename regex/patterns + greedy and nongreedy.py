#lesson 25 udemy automate

#look for spaces in code it might be the difference between it working and not working

import re

#batRegex = re.compile(r'Bat(wo)?man')
#mo = batRegex.search('the adventures of Batman')
#print (mo.group())



#phoneRegex = re.compile(r'(\d\d-)?\d\d\d\d\d-\d\d\d\d\d\d') #area code / country can appear or not appear
#mo = phoneRegex.search('my phone num is 07484-123489. call me') #if wanted a question mark in the raw string then (r'dinner\?') , this would look for dinner?
#print (mo.group())



#* #means match 0 or more times

#batRegex = re.compile(r'Bat(wo)*man')
#mo = batRegex.search('the adventures of Batwowowowowowowowoman')
##<re.Match object; span=(18, 40), match='Batwowowowowowowowoman'> shell output  so can have 0 or more instances
#print(mo)
## again if * is in the raw string then do (r'dinner\*')

# + is one or more so it must appear once or more

haRegex = re.compile(r'(Ha){3}')   #can have a required range of {x, y} by using a ,---- for example {3, 5} would look for that specified object anywhere from 3 to 5 times---  y can also be blank and will make the upper limit infinite
ha = haRegex.search('he said "HaHaHa"')
print(ha.group())


digitRegex = re.compile(r'(\d){3,5}?') # default python matches greedy (longest possible outcome) so add ? to maake it non-greedy and go for shortest possible
di = digitRegex.search('1234567890')

print(di)


