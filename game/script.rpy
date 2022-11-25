# JSTART

# DEFINING CHARACTERS

define e = Character("Eileen",image ="eileen")
define e1 = Character("Eileen",image="eileen_happ")
define l = Character("Lucy",image ="lucy",color = "#0000cc")
define ld = Character("Lucy",image ="lucy_doubt",color = "#0000cc")
define la = Character("Lucy",image ="lucy_angry",color = "#0000cc")

label start:
    scene pic
    pause
    show eileen:
            xalign 10                                        # LEFT SIDE
            yalign 10
    e "Hello everyone , Welcome you all for today's Class"
    scene pic                                      # AGAIN CREATING NEW SCREEN
    show  eileen_happ:                             # TO SHOW NEW CHARACTER
        xalign 10
        yalign 10
    e1 "Let's start our class"
    scene pic1
    with irisout                           # Type of SCREEN CHANGING[ BOX ]
    show  eileen:
        xalign 10
        yalign 10
    e "Ok,Now let's start with {size=+10} MATHEMATICS {/size}"    # SIZE of WORD
    e "Ms.Lucy will teach you MATHEMATICS "
    with slideawayleft                       # Type of SCREEN CHANGING[ WIPING ]
    show  lucy:
        xalign 1.0                                        # RIGHT SIDE
        yalign 1.0
    l "Good morning Ms.Eileen can i takeover my class"
    show  eileen:
        xalign 0
        yalign 10
    e "Sure mam ,Thank you students we will continue our class after MATHEMATICS"
    scene pic1
    show  lucy:
        xalign 0                                           # LEFT SIDE
        yalign 10
    l "OK, Let's start our class"
    l "As a recap of previous class "

    define flashbulb = Fade(0.2,0.0,0.8,color = "#fff")
                                                    # SCREEN CHANGING EFFECT
    scene pic1
    show  lucy_doubt:
        xalign 0
        yalign 10
    ld " Answer this question "
    with flashbulb
    ld " What is {size=+10} 7 x 8 = {/size}"
    $ s = renpy.input("Enter your name :")               # INPUT FROM USER
    if s == "":
        " Hi [s]"                      # [s] is the INPUT we got from the user
label question:
    menu:
        "54":                                         # MAKING CHOICES
            jump Option_1
        "56":
            jump Option_2                        # Again labeling the options
                                                 # to get the desired output
label Option_1:
    scene pic1
    show lucy_angry:
        xalign 0
        yalign 10
    play sound "audio/star_wrong.mp3"                # SOUND EFFECT
    la " No,it's wrong ,try again [s]"
    jump question                      # CREATING ACTION as a LOOP to make user
                                       # to SELECT the CORRECT OPTION
label Option_2:
    scene pic1
    show lucy:
        xalign 0
        yalign 10
    play sound "audio/star_correct.mp3"
    l " Correct, Very Good [s]"
    jump after_choice                      # AFTER Correct option is chosen
                                        # We again create a label to continue
                                          # after the Options section
label after_choice:
    scene pic1
    show lucy:                   # { w } refers to " WAIT TAG "
        xalign 0                 # waits for a click to move to the next slide
        yalign 10
    l "Let us continue our class {w},today we are going to learn "

    #transform topright:
        #xalign 1.0             Also Y alignment is just
        #yalign 1.0             Above the text box

    image asde_a = "asde_a.png"
    image asde_b = "asde_b.png"
    image asde_c = "asde_c.png"
    image asde_d = "asde_d.png"                 # DEFINING the IMAGES
    image asde_e = "asde_e.png"
    image asde_f = "asde_f.png"
    image asde_g = "asde_g.png"

    l " Ascending & Descending Order"               # Mentioned as:
    show asde_b at topright                       # show IMAGE at POSITION
    l " Ascending & Descending Order"          # Here , POSITION = topright
    hide asde_b
    show asde_a at topright
    l "ASCENDING ORDER : Arrangement of numbers from SMALLEST to BIGGEST "
    show asde_a at topright
    l "DESCENDING ORDER : Arrangement of numbers from BIGGEST to SMALLEST "
    show asde_a at topright
    hide asde_a
    show asde_c at topright
    l "Let's see some example"
    hide asde_c                       # HIDE removes the image from the SCREEN
    show asde_d at topright
    l "In 1st example we are going to arrange it in {w}ascending order"
    l "In these numbers which is the smallest & greatest number ?"
    with flashbulb
    hide asde_d
label question1:
    menu:
        "13,18":
            jump Option_11
        "5,13":
            jump Option_12
        "5,40":
            jump Option_13
                                                # SAME FORMAT FOLLOWS
label Option_11:
    scene pic1
    show lucy_angry:
        xalign 0
        yalign 10
    play sound "audio/star_wrong.mp3"
    la " No,it's wrong ,try again [s]"
    jump question1

label Option_12:
    scene pic1
    show lucy_doubt:
        xalign 0
        yalign 10
    play sound "audio/star_wrong.mp3"
    ld " It's wrong ,think twice and try again [s]"
    jump question1

label Option_13:
    scene pic1
    show lucy:
        xalign 0
        yalign 10
    play sound "audio/star_correct.mp3"
    l " Correct, Very Good [s]"
    jump after_choice1
                                                # SAME FORMAT FOLLOWS
label after_choice1:
    scene pic1
    show lucy:
        xalign 0
        yalign 10
    show asde_e at topright
    l "Ok,Let's continue arranging them and{w} we get the order as "
    show asde_e at topright
    hide asde_e
    show asde_f at topright
    l "As,we did in the 1st question we want to find the smallest & greatest number in 2nd question"
    show asde_f at topright
    l "Where  50 is Greatest number & 8 is Smallest number "
    hide asde_f
    show asde_g at topright
    l "And now , we arrange them from greater to smaller one and we get the order as"
    show asde_g at topright
    hide asde_g
    l "That's all for this class , now Ms.Eileen will continue "
    l " Thank you students "
    hide lucy
    with slideawayright
    scene pic2
    show eileen_happ:
        xalign 0
        yalign 1.0
    e1 " Hai friends , i hope you enjoyed this class "
    scene pic2
    show eileen:
        xalign 0
        yalign 1.0
    e "Let's see one last question as a recap of what we learned today"

    image last_q = "last_q.png"
    show last_q at topright
    e " Which is the correct option for ascending order ? "
    hide eileen
    hide last_q
label question2:
    menu:
        "8407,5071,8306,9554":                   # SAME FORMAT FOLLOWS
            jump Option_21
        "5071,8306,8407,9554":
            jump Option_22
        "9554,8407,8306,5071":
            jump Option_23

label Option_21:
    scene pic2
    show eileen:
        xalign 0
        yalign 10
    play sound "audio/star_wrong.mp3"
    e " No,it's wrong [s],try again "
    jump question2

label Option_22:
    scene pic2
    show eileen_happ:
        xalign 0
        yalign 10
    play sound "audio/star_correct.mp3"
    e1 " Correct, Very Good [s]"
    jump after_choice2

label Option_23:                                 # SAME FORMAT FOLLOWS
    scene pic2
    show eileen:
        xalign 0
        yalign 10
    play sound "audio/star_wrong.mp3"
    ld " It's wrong ,think once and try again [s]"
    jump question2

label after_choice2:
    scene pic
    show eileen_happ:
        xalign 0
        yalign 10
    e1" Once again , Thank you all for finishing this lesson"
    scene pic3
    pause
return
# JEND
