marks = {
    '100' : '4',
    '95-99' : '3.75',
    '90-94' : '3.5',
    '75-89' : '3',
    '70-74' : '2.75',
    '65-69' : '2.5',
    '60-64' : '2' ,
    '50-59' : '1.75',
    '30-49' : '1.5',
    '1-29' : '1',
    '0' : '0'}

play = True
while play == True:
    grade = int(input('What was the students mark on the test?: '))
    testamount = int(input('Out of how many marks was the test?: '))
    if testamount < grade:
        print('The marks you have entered do not work. Please try again.')
        
    else:
        play = False
percentgrade = grade/testamount * 100
print ('Your student got: ',percentgrade,'%')

if percentgrade == 100:
    print('That is a : ',(marks.get('100')))
    
elif 95 <= percentgrade <=99:
    print('That is a : ',(marks.get('95-99')))
    
elif 90 <= percentgrade <=94:
    print('THat is a : ',(marks.get('90-94')))
    
elif 75 <= percentgrade <=89:
    print('That is a : ',(marks.get('75-89')))
    
elif 70 <= percentgrade <=74:
    print('That is a : ',(marks.get('70-74')))
    
elif 65 <= percentgrade <=69:
    print('That is a : ',(marks.get('65-69')))
    
elif 60 <= percentgrade <=64:
    print('That is a : ',(marks.get('60-64')))
    
elif 50 <= percentgrade <=59:
    print('That is a : ',(marks.get('50-59')))
    
elif 30 <= percentgrade <=49:
    print('That is a : ',(marks.get('30-49')))    

elif 1 <= percentgrade <=29:
    print('That is a : ',(marks.get('1-29')))
    
elif 0 <= percentgrade <=0:
    print('That is a : ',(marks.get('0')))