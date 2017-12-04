import codecs
import re

dumpa = 'Spotify-Account1.txt'
dumpb = '000webhost.com.txt'

totallines = 0
validacc = 0
invalidacc = 0
gatheredacca = 0
gatheredaccb = 0

dumpamem = []
dumpbmem = []

matched = []
unmatched = []

re_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')

print (' ')
print ('DATA BREACH CROSS-REFERENCE TOOL')
print (' ')
print ('FILE A (TO USE): '+dumpa)
print ('FILE B (TO CROSS-REFERENCE): '+dumpb)
print (' ')
print ('!!! Depending on the file size(s), this might take a while. !!!')
print (' ')
print ('Extracting email(s) from '+dumpa+' ...')

# DUMP A
with codecs.open(dumpa,'r',encoding='utf8') as fh_in:    
    for linea in fh_in:
        match_lista = re_pattern.findall(linea)
        if match_lista:
            dumpamem.append(match_lista[0])
            gatheredacca += 1

print (str(gatheredacca)+' email(s) loaded !')
print ('Extracting email(s) from '+dumpb+' ...')

# DUMP B
with codecs.open(dumpb,'r',encoding='utf8') as f:
    for lineb in f:
        match_listb = re_pattern.findall(lineb)
        if match_listb:
            dumpbmem.append(match_listb[0])
            gatheredaccb += 1
print (str(gatheredaccb)+' email(s) loaded !')
print ('Verifying ...')

# REF STAGE
for dumpadat in dumpamem:
    if dumpadat in dumpbmem:
        matched.append(dumpadat)
        validacc += 1
    else:
        unmatched.append(dumpadat)
        invalidacc += 1

print (' ')
print ('Valid account(s): '+str(validacc))
print ('Invalid account(s): '+str(invalidacc))

# TODO: duplicate check -- duplicates currently go under "invalid" account(s)
