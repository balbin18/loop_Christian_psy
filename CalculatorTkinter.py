
from tkinter import*

calculator = Tk()
calculator.title("Calculator")
calculator.geometry("360x440")
calculator.resizable(width=False, height=False)
operator = ""
text_Input = StringVar()

#Function
def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def buttonClear():
    global operator
    operator = ""
    text_Input.set("")

def buttonEqual():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def buttonTemp():
    temptop = Toplevel()
    temptop.geometry("390x135")
    temptop.resizable(width=False, height=False)
    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()

        if celTempVar.get() != 0.0:
            celToFah = (celTemp * 9/5 + 32)
            print(celToFah)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * 5/9)
            print(fahToCel)
            celTempVar.set(fahToCel)

    def reset():
        fahTempVar.set(int(0))
        celTempVar.set(int(0))

    Temp = tk.Label(temptop, text="Celcius/Fahrenheit Converter", font=("arial",20,"bold"), justify=CENTER).grid(row=5, columnspan=3)
    celTempLabel = tk.Label(temptop, text="Celcius: ", font=("arial",10,"bold")).grid(row=6, column=0)
    InputTempCel = Entry(temptop, bd=5, textvariable = celTempVar).grid(row=6, column=1)
    fahTempLabel = tk.Label(temptop, text="Fahrenheit: ", font=("arial",10,"bold")).grid(row=7, column=0)
    InputempFah = Entry(temptop, bd=5, textvariable = fahTempVar).grid(row=7, column=1)
    convertButton = Button(temptop, text="Convert", font=("Arial", 8, "bold"), bd=5, justify=CENTER, command=convert).grid(row=8, column=1)
    resetButton = Button(temptop, text="Reset", font=("Arial", 8, "bold"), bd=5, justify=RIGHT, command=reset).grid(row=8, column=2)

#Display
txtDisplay = Entry(calculator, font=("arial",20,"bold"), textvariable=text_Input, bd=30, insertwidth=4, bg="white", justify="right").grid(columnspan = 4)

#Buttons
#FirstRow
button7 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="7", command=lambda:buttonClick(7)).grid(row=1,column=0)
button8 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="8",command=lambda:buttonClick(8)).grid(row=1,column=1)
button9 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="9",command=lambda:buttonClick(9)).grid(row=1,column=2)
division = Button(calculator, padx=18, bd=8, fg="black", font=("arial",20,"bold"), text="/",command=lambda:buttonClick("/")).grid(row=1,column=3)
#SecondRow
button4 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="4",command=lambda:buttonClick(4)).grid(row=2,column=0)
button5 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="5",command=lambda:buttonClick(5)).grid(row=2,column=1)
button6 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="6",command=lambda:buttonClick(6)).grid(row=2,column=2)
multiplication = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="*",command=lambda:buttonClick("*")).grid(row=2,column=3)
#ThirdRow
button1 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="1",command=lambda:buttonClick(1)).grid(row=3,column=0)
button2 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="2",command=lambda:buttonClick(2)).grid(row=3,column=1)
button3 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="3",command=lambda:buttonClick(3)).grid(row=3,column=2)
subtraction = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="-",command=lambda:buttonClick("-")).grid(row=3,column=3)
#FourthRow
button0 = Button(calculator, padx=16, bd=8, fg="black", font=("arial",20,"bold"), text="0",command=lambda:buttonClick(0)).grid(row=4,column=0)
decimal = Button(calculator, padx=19.4, bd=8, fg="black", font=("arial",20,"bold"), text=".",command=lambda:buttonClick(".")).grid(row=4,column=1)
clear = Button(calculator, padx=15 , bd=8, fg="black", font=("arial",20,"bold"), text="C", command=buttonClear).grid(row=4,column=2)
addition = Button(calculator, padx=13, bd=8, fg="black", font=("arial",20,"bold"), text="+",command=lambda:buttonClick("+")).grid(row=4,column=3)
#FifthRow
equal = Button(calculator, padx=80, bd=8, fg="black", font=("arial",20,"bold"), text="=",command=buttonEqual).grid(row=5,columnspan=3)
temp = Button(calculator, padx=11, pady=11, bd=8, fg="black", font=("arial",10,"bold"), text="Temp",command=buttonTemp).grid(row=5,column=3)

calculator.mainloop()
