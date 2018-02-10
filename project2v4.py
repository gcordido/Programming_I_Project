#Import all functions from graphics, time and winsound libraries.D
from graphics import *
from time import *
from winsound import *

#Define CreateText function
def CreateText(win, text, x, y, color, font, style, size):
    #Creates a text, parameters for text to be written, coordinates, color,
    #font, style and size.
    tempText = Text(Point(x,y), text)
    tempText.setTextColor(color)
    tempText.setFace(font)
    tempText.setStyle(style)
    tempText.setSize(size)
    #returns the text that will be drawn
    return tempText
#Define mainMenu function
def mainMenu(win):
    #Declare and initialize variables
    ch = 0
    start = scores = exit1 = ""
    #Draw an image background.
    imgBackground = Image(Point(5,5), "bg1.png")
    imgBackground.draw(win)
    #Draw the different buttons for the Main Menu, "Play", "High Scores" and "Exit"
    button1 = Polygon(Point(1.5, 8), Point(4.5,8), Point(5,7.5), Point(4.5,7), Point(1.5,7), Point(1,7.5))
    button1.setFill('black')
    button1.setOutline('white')
    button1.setWidth(2)
    button1.draw(win)

    button2 = button1.clone()
    button2.move(0,-3)
    button2.draw(win)

    button3 = button2.clone()
    button3.move(0,-3)
    button3.draw(win)
    #Create the texxt for each button.        
    start = CreateText(win, "Play", 3, 7.5, 'white', 'helvetica', 'bold', 16)
    start.draw(win)

    scores = CreateText(win, "High Scores", 3, 4.5, 'white', 'helvetica', 'bold', 16)
    scores.draw(win)

    exit1 = CreateText(win, "Exit", 3, 1.5, 'white', 'helvetica', 'bold', 16)
    exit1.draw(win)
    #Draws the WWTBAM logo at a side.
    imgLogo = Image(Point(8.5,7), "logo.png")
    imgLogo.draw(win)
    #Loop to obtain the variable ch, which will be returned and be understood as a choice in the main function.
    while ch == 0:
        #Obtain the click in order to obtain the user's choice
        p1 = win.getMouse()
        if p1.getX() >= 1.5 and p1.getY() >= 7 and p1.getX() <= 5 and p1.getY() <= 8:
            button1.setFill('orange')
            sleep(0.25)
            ch = 1 

        elif p1.getX() >= 1.5 and p1.getY() >= 4 and p1.getX() <= 4.5 and p1.getY() <= 5:
            button2.setFill('orange')
            sleep(0.25)
            ch = 2

        elif p1.getX() >= 1.5 and p1.getY() >= 1 and p1.getX() <= 4.5 and p1.getY() <= 2:
            button3.setFill('orange')
            sleep(0.25)
            ch = 3

        else:
            ch = 0
    
    return ch
#Define Interface function.
def Interface(win):
    #Declare and initialize variables
    choice = 0
    #Draws an image background.
    imgBackground = Image(Point(5,5), "bg1.png")
    imgBackground.draw(win)
    #Draws the question table, along with the lines for a smoother design of the interface.
    questiontemp = Polygon(Point(3,9), Point(7,9), Point(8,7), Point(7,5), Point(3,5), Point(2,7))
    questiontemp.setFill("black")
    questiontemp.setOutline("white")
    questiontemp.setWidth(2)
    questiontemp.draw(win)
    questionline1 = Line(Point(0,7), Point(2,7))
    questionline1.setOutline("white")
    questionline1.setWidth(2)
    questionline1.draw(win)
    questionline2 = questionline1.clone()
    questionline2.move(8,0)
    questionline2.draw(win)

    linechoice1 = Line(Point(0,3.5), Point(0.5,3.5))
    linechoice1.setOutline("white")
    linechoice1.setWidth(2)
    linechoice1.draw(win)

    linechoice2 = linechoice1.clone()
    linechoice2.move(9.5,0)
    linechoice2.draw(win)

    linechoice3 = linechoice2.clone()
    linechoice3.move(0,-2)
    linechoice3.draw(win)

    linechoice4 = linechoice3.clone()
    linechoice4.move(-9.5,0)
    linechoice4.draw(win)

    linechoice5 = Line(Point(4.5,3.5), Point(5.5,3.5))
    linechoice5.setOutline("white")
    linechoice5.setWidth(2)
    linechoice5.draw(win)

    linechoice6 = linechoice5.clone()
    linechoice6.move(0,-2)
    linechoice6.draw(win)
    #Draws the WWTBAM logo at a side.
    imgLogo = Image(Point(9,8.5), "logo.png")
    imgLogo.draw(win)
#Define QuestionFormat function.
def QuestionFormat(win, q, x, y):
    #Creates the text for the question, with said question and coordinates as parameters.
    q = CreateText(win, q, x, y,'white', 'helvetica', 'bold', 14)
    #Returns the question text.
    return q
#Define the Answer function.
def Answer(win, a, x, y):
    #Creates the text for the answer options, with the answer and coordinates as parameters.
    a = CreateText(win, a, x, y,'white', 'helvetica', 'bold', 12)
    #Returns the answer text
    return a

#Define QuestionPaste function
def QuestionPaste(win, q, option1, option2, option3, option4):
    #Creates and draws the question text, and each of answers' text, utilizing the QuestionFormat and
    #Answer functions.
    question1 = QuestionFormat(win, q, 5, 7)
    question1.draw(win)
    sleep(1)
    ans1 = Answer(win, option1, 2.5, 3.5)
    ans1.draw(win)
    sleep(1)
    ans2 = Answer(win, option2, 7.5, 3.5)
    ans2.draw(win)
    sleep(1)
    ans3 = Answer(win, option3, 2.5, 1.5)
    ans3.draw(win)
    sleep(1)
    ans4 = Answer(win, option4, 7.5, 1.5)
    ans4.draw(win)
#Define Click function.
def Click(win):
    #Declare and initialize variables
    a = 0
    #Gets the Mouse clicks for each of the answer buttons.
    p1 = win.getMouse()
    if p1.getX() >= 1 and p1.getY() >= 3 and p1.getX() <= 4 and p1.getY() <= 4.5 :
        a = 1

    if p1.getX() >= 6 and p1.getY() >= 3 and p1.getX() <= 9 and p1.getY() <= 4.5 :
        a = 2

    if p1.getX() >= 1 and p1.getY() >= 1 and p1.getX() <= 4 and p1.getY() <= 2.5 :
        a = 3

    if p1.getX() >= 6 and p1.getY() >= 1 and p1.getX() <= 9 and p1.getY() <= 2.5 :
        a = 4
    #Returns the answer choice.   
    return a
#Define HiScoreTable function.
def HiScoresTable(win, score, hiscore, a):
    #Declare and initialize variables
    b = 0
    #Draws an image background
    imgBackground = Image(Point(5,5), "bg1.png")
    imgBackground.draw(win)
    #Draws the WWTBAM logo
    imgLogo = Image(Point(8.5,7), "logo.png")
    imgLogo.draw(win)
    #Draws the scores table.
    scorestab = Polygon(Point(1.5, 8), Point(6.5,8), Point(7,6.5), Point(6.5,5), Point(1.5,5), Point(1,6.5))
    scorestab.setFill('black')
    scorestab.setOutline('white')
    scorestab.setWidth(2)
    scorestab.draw(win)
    #Creates the current score and high scores text.
    current = CreateText(win, "Current Score: ", 3, 7.25, 'white', 'helvetica', 'bold', 16)
    current.draw(win)
    current2 = CreateText(win, "\t" + score, 3, 6.75, 'white', 'helvetica', 'bold', 16)
    current2.draw(win)
    hiScore = CreateText(win, "High Score: ", 3, 6.25, 'white', 'helvetica', 'bold', 16)
    hiScore = hiScore.draw(win)
    hiScore2 = CreateText(win, "\t" + hiscore, 3, 5.75, 'white', 'helvetica', 'bold', 16)
    hiScore2 = hiScore2.draw(win)
    #Draws the Continue Playing and Exit buttons.
    play = Polygon(Point(1.5, 4), Point(4.5,4), Point(5,3.5), Point(4.5,3), Point(1.5,3), Point(1,3.5))
    play.setFill('black')
    play.setOutline('white')
    play.setWidth(2)
    play.draw(win)

    exitb = play.clone()
    exitb.move(0, -2)
    exitb.draw(win)
    #Creates the Exit Text
    exitText = CreateText(win, "Exit", 3, 1.5, 'white', 'helvetica', 'bold', 16)
    exitText = exitText.draw(win)
    #Depending on the stage of the game, the Continue Playing button's text varies.
    #After the final question it becomes "Play Again"
    if a == 1:
        playtext = CreateText(win, "Continue Playing", 3, 3.5, 'white', 'helvetica', 'bold', 16)
        playtext = playtext.draw(win)
    elif a == 2:
        playtext = CreateText(win, "Play Again", 3, 3.5, 'white', 'helvetica', 'bold', 16)
        playtext = playtext.draw(win)
    else:
        playtext = CreateText(win, "Continue Playing", 3, 3.5, 'white', 'helvetica', 'bold', 16)
        playtext = playtext.draw(win)
    #Loop that obtains a click, defining the user's choice
    #between the Continue Playing and Exit buttons.
    while b == 0:
        p1 = win.getMouse()
        if p1.getX() >= 1 and p1.getY() >= 3 and p1.getX() <= 5 and p1.getY() <= 4:
            play.setFill('orange')
            b = 1
        elif p1.getX() >= 1 and p1.getY() >= 1 and p1.getX() <= 5 and p1.getY() <= 2:
            exitb.setFill('orange')
            b = 2
    #Return the choice's value
    return b
#Define HighScores function.          
def HighScores(win, hiscore):
    #Declare and initialize functions.
    b = 0
    #Draws an image background
    imgBackground = Image(Point(5,5), "bg1.png")
    imgBackground.draw(win)
    #Draws the WWTBAM logo
    imgLogo = Image(Point(8.5,7), "logo.png")
    imgLogo.draw(win)
    #Draws the High Scores table.
    hiscorestab = Polygon(Point(1.5, 8), Point(6.5,8), Point(7,6.5), Point(6.5,5), Point(1.5,5), Point(1,6.5))
    hiscorestab.setFill('black')
    hiscorestab.setOutline('white')
    hiscorestab.setWidth(2)
    hiscorestab.draw(win)
    #Creates the text for current High Score.
    hiScore = CreateText(win, "High Score:".center(3), 3, 7.25, 'white', 'helvetica', 'bold', 16)
    hiScore = hiScore.draw(win)
    hiScore2 = CreateText(win, "\t\t" + hiscore, 3, 6.75, 'white', 'helvetica', 'bold', 18)
    hiScore2 = hiScore2.draw(win)
    #Creates the Play and Exit buttons.
    play = Polygon(Point(1.5, 4), Point(4.5,4), Point(5,3.5), Point(4.5,3), Point(1.5,3), Point(1,3.5))
    play.setFill('black')
    play.setOutline('white')
    play.setWidth(2)
    play.draw(win)

    exitb = play.clone()
    exitb.move(0, -2)
    exitb.draw(win)
    #Creates the Back To Main Menu and Exit button's text.
    playtext = CreateText(win, "Back to Main Menu", 3, 3.5, 'white', 'helvetica', 'bold', 16)
    playtext.draw(win)

    exitText = CreateText(win, "Exit", 3, 1.5, 'white', 'helvetica', 'bold', 16)
    exitText = exitText.draw(win)
    #Loop that obtains a click in order to assign a value
    #to the user's choice between the buttons
    while b == 0:
        p1 = win.getMouse()
        if p1.getX() >= 1 and p1.getY() >= 3 and p1.getX() <= 5 and p1.getY() <= 4:
            play.setFill('orange')
            b = 1
        elif p1.getX() >= 1 and p1.getY() >= 1 and p1.getX() <= 5 and p1.getY() <= 2:
            exitb.setFill('orange')
            b = 2
    #Returns the choice's value.
    return b
#Define main function.
def main():
    #Define and initialize variables.
    choice = answer = scorec  = playon = playag = scores = play = hscoresc = 0
    question1 = hscore = ""
    #Creates a window of 700x550 dimensions.
    win = GraphWin("Who Wants to be a Millionaire?", 700, 550)
    #Sets the coordinates to the window.
    win.setCoords(0,0,10,10)
    #Opens the hscores.txt file in order to read its content.
    infile = open("hscores.txt", "r")
    line1 = infile.readline()
    #Assigns the value written in the .txt file to variable hscore.
    hscore = line1
    
    #Point values are: 100, 200, 500, 1000, 2000   

    #Loop that will keep going as long the play variable's value is not 1.
    while play != 1:
        #Plays the Main Theme sound.
        PlaySound("theme2.wav", SND_PURGE|SND_ASYNC)
        sleep(0.25)
        #Invoke mainMenu function and assigns it's value to variable choice.
        choice = mainMenu(win)
        #If choice is 1, proceed with the following.
        if choice == 1:
            #Invoke Interface function to draw the function.
            Interface(win)
            #Assign values to variables play, answer and scores
            #This resets said values in case the user wishes to play again.
            play = 1
            answer = 0
            scores = 0
            #Draws each of the answers options' buttons.
            choice1temp = Polygon(Point(1,4), Point(4,4), Point(4.5,3.5), Point(4,3), Point(1,3), Point(0.5,3.5))
            choice1temp.setFill("black")
            choice1temp.setOutline("white")
            choice1temp.setWidth(2)
            choice1temp.draw(win)

            choice2temp = choice1temp.clone()
            choice2temp.move(5,0)
            choice2temp.draw(win)

            choice3temp = choice2temp.clone()
            choice3temp.move(0,-2)
            choice3temp.draw(win)

            choice4temp = choice3temp.clone()
            choice4temp.move(-5,0)
            choice4temp.draw(win)
            #Plays the question ambient sound
            PlaySound("qsound2.wav", SND_PURGE|SND_ASYNC)
            #Invoke QuestionPaste to get the question and answers' text.
            QuestionPaste(win, "When did Christopher Colombus \ndiscover the New World?", "A)1492", "B) 1562", "C) 1993", "D) He never did.")
            #Creates the Check for Correct and the X for wrong answer.
            check = Line(Point(1.5, 5), Point(3.5, 1))
            check.setOutline('green')
            check.setWidth(20)
            check2 = Line(Point(3.5,1), Point(8,9))
            check2.setOutline('green')
            check2.setWidth(20)

            x1 = Line(Point(1.5, 9), Point(7.5, 1))
            x1.setOutline('red')
            x1.setWidth(20)
            x2 = Line(Point(8.5,9), Point(1.5,1))
            x2.setOutline('red')
            x2.setWidth(20)            
            #Loop that repeats as long answer variable's value is 0.
            while answer == 0:
                p1 = win.getMouse()
                #Invoke Click function and assign its value to answer variable.
                answer = Click(win)
                #Depending on the value assigned to answer, the program gives a different result.
                if answer == 1:
                    #Since answer 1 is correct, play question right sound.
                    PlaySound("qwin.wav", SND_PURGE|SND_ASYNC)
                    #Changes the button's color to show the user what option he clicked on.
                    choice1temp.setFill("orange")
                    #Draws the Correct Answer check.
                    check.draw(win)
                    check2.draw(win)
                    sleep(0.5)
                    check.undraw()
                    check2.undraw()
                    sleep(0.5)
                    check.draw(win)
                    check2.draw(win)
                    #Adds up 100 points to the scores variable.
                    scores = scores + 100
                    sleep(0.5)
                    #playon variable changes the text in the HiScoresTable based on the stage of the game.
                    #Here it will display "Continue Playing"
                    playon = 1
                    #Invoke the HiScoresTable function to obtain a choice, and draw the high scores tab.
                    playag = HiScoresTable(win, str(scores), hscore, playon)
                    #If the user choice is 2, implies he clicked on exit.
                    if playag == 2:
                        #Assign 1 to variable play in order to break the first loop
                        play = 1
                        #Close the  window.
                        win.close()
 


                elif answer == 2:
                    #Since answer 2 is wrong, play the wrong answer ssound.
                    PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                    choice2temp.setFill("orange")
                    #Draws the Wrong Answer X.
                    x1.draw(win)
                    x2.draw(win)
                    sleep(0.5)
                    x1.undraw()
                    x2.undraw()
                    sleep(0.5)
                    x1.draw(win)
                    x2.draw(win)
                    sleep(0.5)
                    playon = 0
                    playag = HiScoresTable(win, str(scores), hscore, playon)
                    if playag == 2:
                        play = 1
                        win.close()
                    

                elif answer == 3:
                    PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                    choice4temp.setFill("orange")
                    x1.draw(win)
                    x2.draw(win)
                    sleep(0.5)
                    x1.undraw()
                    x2.undraw()
                    sleep(0.5)
                    x1.draw(win)
                    x2.draw(win)
                    sleep(0.5)
                    playon = 0
                    playag = HiScoresTable(win, str(scores), hscore, playon)
                    if playag == 2:
                        play = 1
                        win.close()
                    

                elif answer == 4:
                    PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                    choice3temp.setFill("orange")
                    x1.draw(win)
                    x2.draw(win)
                    sleep(0.5)
                    x1.undraw()
                    x2.undraw()
                    sleep(0.5)
                    x1.draw(win)
                    x2.draw(win)
                    sleep(0.5)
                    playon = 0
                    playag = HiScoresTable(win, str(scores), hscore, playon)
                    if playag == 2:
                        play = 1
                        win.close()
                    
                #This else statement makes the loop continue on until the user clicks on one of the buttons.
                else:
                    answer == 0
                #If the user chooses to continue playing.
                if playag == 1:
                        playag = 0
                        while playag == 0:
                            #Resets the buttons back to black, and undraws them in order to get them drawn again afterwards.
                            choice1temp.setFill('black')
                            choice2temp.setFill('black')
                            choice3temp.setFill('black')
                            choice4temp.setFill('black')
                            choice1temp.undraw()
                            choice2temp.undraw()
                            choice3temp.undraw()
                            choice4temp.undraw()
                            
                            check.undraw()
                            check2.undraw()
                            x1.undraw()
                            x2.undraw()
                            #Invokes the interface function to draw the interface up again.
                            Interface(win)
                            choice1temp.draw(win)
                            choice2temp.draw(win)
                            choice3temp.draw(win)
                            choice4temp.draw(win)
                            #Plays the question ambient sound.
                            PlaySound("qsound2.wav", SND_PURGE|SND_ASYNC)
                            QuestionPaste(win, "What's the chemical \nsymbol for Sodium?", "A) Cl", "B) So", "C) Na", "D) Li")
                            #From here repeats the process above explained.
                            answer = Click(win)
                            if answer == 1:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice1temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                            
                            elif answer == 2:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice2temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play == 1
                                    win.close()

                            elif answer == 3:
                                PlaySound("qwin.wav", SND_PURGE|SND_ASYNC)
                                choice4temp.setFill("orange")
                                check.draw(win)
                                check2.draw(win)
                                sleep(0.5)
                                check.undraw()
                                check2.undraw()
                                sleep(0.5)
                                check.draw(win)
                                check2.draw(win)
                                sleep(0.5)
                                #Adds the 2nd answer's value to the scores variable.
                                scores = scores + 200
                                sleep(0.5)
                                playon = 1
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                                   
                            elif answer == 4:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice3temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                #Repeats the process if the user chooses to continue on playing.
                if playag == 1:
                    playag = 0
                    while playag == 0:
                            choice1temp.setFill('black')
                            choice2temp.setFill('black')
                            choice3temp.setFill('black')
                            choice4temp.setFill('black')
                            choice1temp.undraw()
                            choice2temp.undraw()
                            choice3temp.undraw()
                            choice4temp.undraw()
                            
                            check.undraw()
                            check2.undraw()
                            x1.undraw()
                            x2.undraw()
                            Interface(win)
                            choice1temp.draw(win)
                            choice2temp.draw(win)
                            choice3temp.draw(win)
                            choice4temp.draw(win)
                            PlaySound("qsound2.wav", SND_PURGE|SND_ASYNC)
                            QuestionPaste(win, "What's the name of the astronaut \nthat first stepped on the moon?", "A) Louis Armstrong", "B) Lance Armstrong", "C) Neil Livestrong", "D) Neil Armstrong")

                            answer = Click(win)
                            if answer == 1:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice1temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                            
                            elif answer == 2:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice2temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()

                            elif answer == 3:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice4temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()  
                                   
                            elif answer == 4:
                                PlaySound("qwin.wav", SND_PURGE|SND_ASYNC)
                                choice3temp.setFill("orange")
                                check.draw(win)
                                check2.draw(win)
                                sleep(0.5)
                                check.undraw()
                                check2.undraw()
                                sleep(0.5)
                                check.draw(win)
                                check2.draw(win)
                                scores = scores + 500
                                sleep(0.5)
                                playon = 1
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                          
            
                if playag == 1:
                    playag = 0
                    while playag == 0:
                            choice1temp.setFill('black')
                            choice2temp.setFill('black')
                            choice3temp.setFill('black')
                            choice4temp.setFill('black')
                            choice1temp.undraw()
                            choice2temp.undraw()
                            choice3temp.undraw()
                            choice4temp.undraw()
                            
                            check.undraw()
                            check2.undraw()
                            x1.undraw()
                            x2.undraw()
                            Interface(win)
                            choice1temp.draw(win)
                            choice2temp.draw(win)
                            choice3temp.draw(win)
                            choice4temp.draw(win)
                            PlaySound("qsound2.wav", SND_PURGE|SND_ASYNC)
                            QuestionPaste(win, "Who is the FIFA World Cup \nall time record goal scorer? ", "A) Miroslav Klose", "B) Pele", "C) Zinedine Zidane", "D) Ronaldo")

                            answer = Click(win)
                            if answer == 1:
                                PlaySound("qwin.wav", SND_PURGE|SND_ASYNC)
                                choice1temp.setFill("orange")
                                check.draw(win)
                                check2.draw(win)
                                sleep(0.5)
                                check.undraw()
                                check2.undraw()
                                sleep(0.5)
                                check.draw(win)
                                check2.draw(win)
                                scores = scores + 1000
                                sleep(0.5)
                                playon = 1
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                            
                            elif answer == 2:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice2temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()

                            elif answer == 3:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice4temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()  
                                   
                            elif answer == 4:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice3temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 0
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                                    
                if playag == 1:
                    playag = 0
                    while playag == 0:
                            choice1temp.setFill('black')
                            choice2temp.setFill('black')
                            choice3temp.setFill('black')
                            choice4temp.setFill('black')
                            choice1temp.undraw()
                            choice2temp.undraw()
                            choice3temp.undraw()
                            choice4temp.undraw()
                            
                            check.undraw()
                            check2.undraw()
                            x1.undraw()
                            x2.undraw()
                            Interface(win)
                            choice1temp.draw(win)
                            choice2temp.draw(win)
                            choice3temp.draw(win)
                            choice4temp.draw(win)
                            PlaySound("qsound2.wav", SND_PURGE|SND_ASYNC)
                            QuestionPaste(win, "Which WWE wrestler has become a major \ncontributor to the \nMake a Wish Foundation?", "A) The Terminator", "B) John Cena", "C) Hulk Hogan", "D) El Gato")

                            answer = Click(win)
                            if answer == 1:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice1temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 2
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                                else:
                                    play = 0
                                    
                            elif answer == 2:
                                #Since this is the last correct answer, plays the final correct answer music.
                                PlaySound("finalwin.wav", SND_PURGE|SND_ASYNC)
                                choice2temp.setFill("orange")
                                check.draw(win)
                                check2.draw(win)
                                sleep(0.5)
                                check.undraw()
                                check2.undraw()
                                sleep(0.5)
                                check.draw(win)
                                check2.draw(win)
                                sleep(0.5)
                                scores = scores + 2000
                                sleep(2)
                                #Here playon has value 2 in order to get "Play Again" button from HiScoresTable function.
                                playon = 2
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                                else:
                                    play = 0

                            elif answer == 3:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice4temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 2
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                                else:
                                    play = 0
                                   
                            elif answer == 4:
                                PlaySound("qlose.wav", SND_PURGE|SND_ASYNC)
                                choice3temp.setFill("orange")
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                x1.undraw()
                                x2.undraw()
                                sleep(0.5)
                                x1.draw(win)
                                x2.draw(win)
                                sleep(0.5)
                                playon = 2
                                playag = HiScoresTable(win, str(scores), hscore, playon)
                                if playag == 2:
                                    play = 1
                                    win.close()
                                else:
                                    play = 0
                                    

                                        
            #If the current score value is higher than the previous registered hscore.
            if scores > int(hscore):
                #Assign the scores value to hscore, as a way to overwrite the previous high score with a higher one.
                hscore = scores
                #Opens the outfile to write in it.
                outfile = open("hscores.txt", "w")
                #Writes the new high score value into the hscores.txt file.
                outfile.write(str(hscore))
                #Closes the outfile.
                outfile.close()
        #If the user clicks on the High Scores button, thus making choice's value = 2                
        elif choice == 2:
            #Invoke HighScores value to display the current High Score.
            hscoresc = HighScores(win, str(hscore))
            #Depending on the value obtained by the click, either go back to main menu or close the window.
            if hscoresc == 1:
                play == 0
            elif hscoresc == 2:
                play = 1
                win.close()
            

        #If the user clicks on the Exit button, break the first loop and close the game's window.
        elif choice == 3:
            play = 1
            win.close()
            
        

    
main()
