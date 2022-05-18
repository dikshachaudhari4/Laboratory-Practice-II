ipt = int(input(
    '''Hello!! I am your admission and scholarship assistant
    In which section do you want help you?
    1. Admission
    2. Scholarship
    '''
))

if ipt==1:
    adm = int(input(
        '''In which year are you taking admission ?
        1. First Year Engineering
        2. Direct Second Year Engineering
        '''
    ))
    quest = input(
        '''Okay...please ask your doubts. Press 0 to exit.
        '''
    )
    while quest!='0' :
        if(quest=="Which documents do I need for taking admission ?") :
            if adm==1 :
                print("You need your CET or JEE score card, 10th and 12th mark sheets, school leaving certificate and birth certificate")
            else :
                print("You need your diploma third year mark sheet, school leaving certificate and birth certificate")
        elif(quest=="When will the admission process start ?") :
            if adm==1 :
                print("15 July")
            else :
                print("15 August")
        elif(quest=="What is the deadline to fill the admission forms ?") :
            if adm==1:
                print("30 July")
            else :
                print("30 August")
        elif(quest=="Where can I get the admission related information ?") :
            print("You can visit www.pict.edu website or visit the student counter in PICT campus")
        elif(quest=="Which faculty is the incharge of the admission process ?") :
            print("Mr. Milind Phadke. contact : maphadke@pict.edu")
        quest = input("ask another doubt or press 0.")
elif ipt==2 :
    adm = int(input(
        '''To which category do you belong ?
        1. OBC/VJNT
        2. SC/ST
        3. EWS
        '''
    ))
    quest = input(
        '''Okay...please ask your doubts. Press 0 to exit.
        '''
    )
    print(quest != '0')
    while quest != '0':
        if (quest == "Which documents do I need ?"):
                print("You need your previous year mark sheet, caste certificate, caste validity certificate, income certificate and birth certificate")
        elif (quest == "When will the scholarship process start ?"):
                print("1 December")
        elif (quest == "What is the deadline to fill the scholarship forms ?"):
                print("30 March")
        elif (quest == "Where can I get the scholarship related information ?"):
            print("You can visit www.mahadbt.com website or visit the student counter in PICT campus")
        elif (quest == "Which faculty is the incharge of the scholarship process ?"):
            print("Mr. Pravin Sawant. contact : pgsawant@pict.edu")
        quest = input("ask another doubt or press 0.")
