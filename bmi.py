import tkinter
import healthsignup
root = tkinter.Tk()
root.title("bmi calculator")
 

def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round( kg/ (height **  2))
    label_result['text'] = f"BMI: {bmi}"  


label_kg = tkinter.Label(root, text = "Weight Kg:")
label_kg.grid(column=0, row = 0)

entry_kg = tkinter.Entry(root)
entry_kg.grid(column=1, row = 0)

label_height = tkinter.Label(root, text = "Height: ")
label_height.grid(column=0, row = 1)
 
entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row = 1)

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
button_calculate.grid(column=0, row = 2)
   
label_result = tkinter.Label(root, text = "BMI: ")
label_result.grid(column=1, row = 2 )


root.mainloop()
