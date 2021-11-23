import re
text='To be, or not to be, that is the question'
print('Liczba samogłosek:',len((re.findall('[aeiouy]', text))))
