from cmu_graphics import *

#Initializes the color scheme
boxFill = rgb(220, 214, 202)
textFill = rgb(45, 41, 38);
#These lines configure some basic app settings
app.background = rgb(45, 41, 38);
app.stepsPerSecond = 50;
app.width = 560;
app.height = 600;

app.promptClassNumber = 0;
app.grades = ["A", "B+", "B", "B-", "C+", "C", "C-", "N"];
app.classTypes = ["AP", "H", "R"];

app.game = False;

#Info Box creation
Rect(20, 20, 520, 560, fill = rgb(200, 194, 182))

startBtn = Group(
    Rect(280, 250, 120, 50, fill = textFill, align = 'center'),
    Label("START", 280, 250, fill = boxFill, size = 25, bold = True),
)
instructionsBtn = Group(
    Rect(280, 370, 220, 50, fill = textFill, align = 'center'),
    Label("INSTRUCTIONS", 280, 370, fill = boxFill, size = 25, bold = True),
)

againBtn = Group(
    Rect(280, 450, 120, 50, fill = textFill, align = 'center'),
    Label("BACK", 280, 450, fill = boxFill, size = 25, bold = True),
)
againBtn.visible = False

#Title creation
Label("High School GPA Calculator", 275, 50, fill = textFill, size = 35,
                           font = 'Barlow', bold = True, align = 'center'),

instructions = Group(
    Label("Instructions", 280, 100, fill = textFill, size = 30, bold = True, font = 'Barlow'),
    Label("This is a program that will calculate your high school GPA.", 280, 150, fill = textFill, size = 20, font = 'Barlow'),
    Label("To calculate your GPA, input the grade you received for", 280, 200, fill = textFill, size = 20, font = 'Barlow'),
    Label("each class and the type of class it is. Providing the course", 280, 250, fill = textFill, size = 20, font = 'Barlow'),
    Label("name is optional. The types of classes are written as AP", 280, 300, fill = textFill, size = 20, font = 'Barlow'),
    Label("for advanced placement, H for honors, and R for regular.", 280, 350, fill = textFill, size = 20, font = 'Barlow'),
)

instructions.visible = False
#This is some basic information that is a part of the UI.
uiElements = Group(
    #Course header
    Label("Course Name", 280, 120, fill = textFill, size = 20,
                           font = 'Barlow', bold = True, align = 'center'),
    #Type header
    Label("Type", 105, 120, fill = textFill, size = 20,
                           font = 'Barlow', bold = True, align = 'center'),
    #Grade header
    Label("Grade", 455, 120, fill = textFill, size = 20,
                           font = 'Barlow', bold = True, align = 'center'),
)

allGrades = Group();
allTypesOfClasses = Group();
allClassNames = Group();
for i in range(7):
    #This is the rectangle for the classes
    uiElements.add(Rect(160, 140+i * 50, 240, 51, fill = boxFill, border = textFill));
    #This is the rectangle for the type
    uiElements.add(Rect(70, 140 + i * 50, 70, 51, fill = boxFill, border = textFill));
    #This is the rectangle for the grade
    uiElements.add(Rect(420, 140 + i * 50, 70, 51, fill = boxFill, border = textFill));
    #Empty text labels for grade and type boxes
    allGrades.add(Label("-", 455, 165 + i * 50, size = 30, fill = textFill));
    allTypesOfClasses.add(Label("-", 100, 165 + i * 50, size = 30, fill = textFill));
    allClassNames.add(Label("insert class", 280, 165 + i * 50, size = 30, fill = textFill, opacity = 40))
    #These are the dropdown triangles
    uiElements.add(RegularPolygon(130, 165 + i * 50, 7, 3, rotateAngle = 180, fill = textFill));
    uiElements.add(RegularPolygon(480, 165 + i * 50, 7, 3, rotateAngle = 180, fill = textFill));

uiElements.add(allGrades)
uiElements.add(allTypesOfClasses)
uiElements.add(allClassNames)
uiElements.visible = False

dropdownShapes = Group();
#Creates the boxes for the grade dropdown menu
for i in range(8):
    GradeRect = Rect(490.1, 0 + i * 30, 40, 30, fill = boxFill, border = textFill);
    dropdownShapes.add(GradeRect);
    
nextY = 15;
#Creates the labels for the grade dropdown menu
for i in range(8):
    grade = Label(app.grades[i], dropdownShapes.centerX,
                   nextY, size = 20, fill = textFill)
    nextY = grade.centerY + 30;
    dropdownShapes.add(grade);

dropdownShapes.visible = False

dropdownTypeShapes = Group();
#Creates the boxes for the type dropdown menu
for i in range(3):
    typeRect = Rect(31, 140 + i * 30, 40, 30, fill = boxFill, border = textFill)
    dropdownTypeShapes.add(typeRect);

nextY = 155;
#Creates the labels for the type dropdown menu
for i in range(3):
    type = Label(app.classTypes[i], dropdownTypeShapes.centerX, nextY, size = 20)
    nextY = type.centerY + 30;
    dropdownTypeShapes.add(type);
dropdownTypeShapes.visible = False

#Creates the calculate box
calculate = Rect(280, 530, 120, 50, fill = textFill, align = 'center');
textForCalculate = Label("Calculate", calculate.centerX, calculate.centerY, fill = boxFill, size = 25, bold = True);
calculateBox = Group(calculate, textForCalculate);
calculateBox.visible = False

#Creates the labels for displaying the GPA
unweighted = Label("Unweighted GPA:", 40, 240, align = 'left', size = 45, fill = textFill, font = 'barlow');
unweightedLabel = Label(0, unweighted.right + 10, unweighted.centerY, align = 'left', size = 45, fill = textFill, font = 'barlow');

weighted = Label("Weighted GPA:", 40, 360, align = 'left', size = 45, fill = textFill, font = 'barlow');
weightedLabel = Label(0, weighted.right + 20, weighted.centerY, align = 'left', size = 45, fill = textFill, font = 'barlow');

#Creates the group containing everything needed to be displayed when the program ends
finalScreen = Group(unweighted, unweightedLabel, weighted, weightedLabel);
finalScreen.visible = False


#This is a function, which converts the letter grades into numbers.
def convert_Grade_to_Number(grade):
    grade_to_number = { 'A': 4.0,
                        'B+': 3.3,
                        'B': 3.0,
                        'B-': 2.7,
                        'C+': 2.3,
                        'C': 2.0,
                        'C-': 1.7,
                        'N': 0.0
                    }
    return grade_to_number.get(grade, None)

#Calculates the centerY value of the box the mouse clicked on based on the mouse's Y value and the box's starting height if the box height is 50
def calculateY(mouseY, startingY):
    for i in range(7):
        if mouseY < i * 50 + startingY:
            return i * 50 + 165

#Changes the grade displayed in the box to the user after the mouse has been pressed
def calculateGradeAfterClick(mouseY):
    for i in range(8):
        if(mouseY < dropdownShapes.centerY - 90 + i * 30):
            for grade in allGrades:
                if grade.centerY == calculateY(app.currentMouseY, 190):
                    grade.value = app.grades[i]
            return

#Changes the type displayed in the box to the user after the mouse has been pressed
def calculateTypeAfterClick(mouseY):
    for i in range(3):
        if(mouseY < dropdownTypeShapes.centerY - 15 + i * 30):
            for type in allTypesOfClasses:
                if type.centerY == calculateY(app.currentMouseY, 190):
                    type.value = app.classTypes[i]        
            return

#Is called every time the mouse is pressed
def onMousePress(mouseX, mouseY):
    if(app.game == True and uiElements.hits(mouseX, mouseY)):
        if(mouseX > 160 and mouseX < 400):
            response = app.getTextInput("Please enter the name of the class");
            for name in allClassNames:
                if name.centerY == calculateY(mouseY, 190):
                    name.value = response
                    name.opacity = 100

        if(mouseX > 420 and mouseX < 490):
            app.currentMouseY = mouseY;
            dropdownShapes.visible = True;
            dropdownShapes.centerY = calculateY(mouseY, 190) + 50;
        
        if(mouseX > 70 and mouseX < 140):
            app.currentMouseY = mouseY;
            dropdownTypeShapes.visible = True;
            dropdownTypeShapes.centerY = calculateY(mouseY, 190) + 30;
    elif (startBtn.contains(mouseX, mouseY) and startBtn.visible) or (againBtn.contains(mouseX, mouseY) and againBtn.visible):
        app.game = True
        uiElements.visible = True
        startBtn.visible = False
        instructions.visible = False
        instructionsBtn.visible = False
        againBtn.visible = False
        finalScreen.visible = False
    elif instructionsBtn.contains(mouseX, mouseY) and instructionsBtn.visible:
        instructions.visible = True
        instructionsBtn.visible = False
        startBtn.centerY = 450
    if(dropdownShapes.hits(mouseX, mouseY) and dropdownShapes.visible):      
        calculateGradeAfterClick(mouseY);
        dropdownShapes.visible = False;

    if(dropdownTypeShapes.hits(mouseX, mouseY) and dropdownTypeShapes.visible):
        calculateTypeAfterClick(mouseY);
        dropdownTypeShapes.visible = False;

    if(calculateBox.visible and calculateBox.hits(mouseX, mouseY)):
        app.game = False;
        calculateBox.visible = False;
        endGame();

    
def onMouseMove(mouseX, mouseY):
    if startBtn.contains(mouseX, mouseY):
        startBtn.opacity = 80
    else:
        startBtn.opacity = 100
    
    if instructionsBtn.contains(mouseX, mouseY):
        instructionsBtn.opacity = 80
    else:
        instructionsBtn.opacity = 100

    if againBtn.contains(mouseX, mouseY):
        againBtn.opacity = 80
    else:
        againBtn.opacity = 100
    
    if calculate.contains(mouseX, mouseY):
        calculate.opacity = 80
    else:
        calculate.opacity = 100
#Loads the results screen and ends the game/program
def endGame():
    uiElements.visible = False;
    totalCount = 0
    weightedCount = 0

    for grade in allGrades:
        totalCount += convert_Grade_to_Number(grade.value)
    for type in allTypesOfClasses:
        if (type.value == "AP"):
            weightedCount += 1.0
        elif (type.value == "H"):
            weightedCount += 0.5
    unweightedValue = pythonRound(totalCount/7, 2)
    weightedValue = pythonRound((totalCount + weightedCount)/7, 2)
    if (unweightedValue != pythonRound(unweightedValue, 1)):
        unweightedLabel.centerX = unweighted.right + 60
    elif (unweightedValue != pythonRound(unweightedValue, 0)):
        unweightedLabel.centerX = unweighted.right + 40
    else:
        unweightedLabel.centerX = unweighted.right + 20
    if (weightedValue != pythonRound(weightedValue, 1)):
        weightedLabel.centerX = weighted.right + 60
    elif (weightedValue != pythonRound(weightedValue, 0)):
        weightedLabel.centerX = weighted.right + 40
    else:
        weightedLabel.centerX = weighted.right + 20
    unweightedLabel.value = unweightedValue;
    weightedLabel.value = weightedValue;
    finalScreen.visible = True;
    againBtn.visible = True

#Is called every step (which is 50 times per second)
def onStep():
    showCalcBtn = True;
    if app.game:
        for grade in allGrades:
            if grade.value == "-":
                showCalcBtn = False
        for type in allTypesOfClasses:
            if type.value == "-":
                showCalcBtn = False
        if showCalcBtn:
            calculateBox.visible = True
    


cmu_graphics.run();
