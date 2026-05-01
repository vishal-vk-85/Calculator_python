import math   # for sqrt, trigonometry, logs, pi etc
import statistics   # for mean median mode
import numpy as np   # for matrix calculations

# Example function structure

def factorial_calc():
    # Take integer input from user
    n = int(input("Enter number: "))

    # math.factorial computes factorial
    result = math.factorial(n)

    # display result
    print("Factorial =", result)

# ---------------- BASIC MATH ---------------- #

def quadratic_solver():
    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))

    d=b**2-4*a*c

    if d>0:
        r1=(-b+math.sqrt(d))/(2*a)
        r2=(-b-math.sqrt(d))/(2*a)
        print("Roots:",r1,r2)
    elif d==0:
        print("Root:",-b/(2*a))
    else:
        real=-b/(2*a)
        imag=math.sqrt(-d)/(2*a)
        print(f"Roots = {real}+{imag}i and {real}-{imag}i")


def factorial_calc():
    n=int(input("Number: "))
    print("Factorial:",math.factorial(n))


def sqrt_calc():
    x=float(input("Number: "))
    print(math.sqrt(x))


def power_calc():
    a=float(input("Base: "))
    b=float(input("Exponent: "))
    print(a**b)


def linear_solver():
    print("Solve:")
    print("a1x+b1y=c1")
    print("a2x+b2y=c2")
    a1=float(input("a1: "))
    b1=float(input("b1: "))
    c1=float(input("c1: "))
    a2=float(input("a2: "))
    b2=float(input("b2: "))
    c2=float(input("c2: "))

    A=np.array([[a1,b1],[a2,b2]])
    B=np.array([c1,c2])
    try:
        sol=np.linalg.solve(A,B)
        print("x=",sol[0]," y=",sol[1])
    except:
        print("No unique solution")

# ---------------- MATRIX ---------------- #

def input_matrix():
    r=int(input("Rows: "))
    c=int(input("Cols: "))
    data=[]
    for i in range(r):
        row=list(map(float,input(f"Row {i+1}: ").split()))
        data.append(row)
    return np.array(data)


def matrix_add():
    A=input_matrix()
    B=input_matrix()
    print(A+B)
    
def matrix_sub():
    A=input_matrix()
    B=input_matrix()
    print(A-B)


def matrix_mult():
    A=input_matrix()
    B=input_matrix()
    print(np.dot(A,B))


def determinant_calc():
    A=input_matrix()
    print(np.linalg.det(A))
    
def inverse_matrix():
    A=input_matrix()
    try:
        print(np.linalg.inv(A))
    except:
        print("Inverse doesn't exist")
        
# ---------------- CONVERTERS ---------------- #
    print('2 lb->kg')
    print('3 g->oz')
    print('4 oz->g')
    c=input('Choice: ')
    x=float(input('Value: '))
    if c=='1': print(x*2.20462)
    elif c=='2': print(x/2.20462)
    elif c=='3': print(x*0.035274)
    else: print(x/0.035274)


def time_converter():
    print('1 seconds->minutes')
    print('2 hours->days')
    c=input('Choice: ')
    x=float(input('Value: '))
    if c=='1': print(x/60)
    else: print(x/24)


def speed_converter():
    print('1 m/s->km/h')
    print('2 km/h->m/s')
    x=float(input('Value: '))
    c=input('Choice: ')
    if c=='1': print(x*3.6)
    else: print(x/3.6)


def pressure_converter():
    print('1 pascal->atm')
    print('2 bar->psi')
    c=input('Choice: ')
    x=float(input('Value: '))
    if c=='1': print(x/101325)
    else: print(x*14.5038)


def power_converter():
    print('1 watts->horsepower')
    print('2 kilowatts->megawatts')
    c=input('Choice: ')
    x=float(input('Value: '))
    if c=='1': print(x/745.7)
    else: print(x/1000)

# ---------------- SHAPES ---------------- #
    try:
        print('Mode=',statistics.mode(nums))
    except:
        print('No unique mode')

# ---------------- TRIG ---------------- #

def trig_calc():
    x=math.radians(float(input('Angle in degrees: ')))
    print('sin=',math.sin(x))
    print('cos=',math.cos(x))
    print('tan=',math.tan(x))


def inverse_trig():
    x=float(input('Value: '))
    print('asin=',math.degrees(math.asin(x)))
    print('acos=',math.degrees(math.acos(x)))
    print('atan=',math.degrees(math.atan(x)))


def degree_radian():
    print('1 Degree->Radian')
    print('2 Radian->Degree')
    c=input('Choice: ')
    x=float(input('Value: '))
    if c=='1':
        print(math.radians(x))
    else:
        print(math.degrees(x))
        
# ---------------- MENU ---------------- #

def menu():
    while True:
        print('\n=== MEGA CALCULATOR ===')
        print('1 Quadratic Solver')
        print('2 Factorial')
        print('3 Matrix Addition')
        print('4 Matrix Subtraction')
        print('5 Matrix Multiplication')
        print('6 Determinant')
        print('7 Square Root')
        print('8 Power')
        print('9 Linear Equation Solver')
        print('10 Matrix Inverse')
        print('11 Temperature Converter')
        print('12 Length Converter')
        print('13 Area/Perimeter')
        print('14 Area Converter')
        print('15 Volume Shapes')
        print('16 Volume Converter')
        print('17 Weight Converter')
        print('18 Time Converter')
        print('19 Speed Converter')
        print('20 Pressure Converter')
        print('21 Power Converter')
        print('22 Number System Converter')
        print('23 Log Calculator')
        print('24 Exponential Calculator')
        print('25 Percentage Calculator')
        print('26 Mean Median Mode')
        print('27 Trigonometric Functions')
        print('28 Inverse Trig')
        print('29 Degree-Radian Converter')
        print('0 Exit')

        choice=input('Enter choice: ')

        if choice=='1': quadratic_solver()
        elif choice=='2': factorial_calc()
        elif choice=='3': matrix_add()
        elif choice=='4': matrix_sub()
        elif choice=='5': matrix_mult()
        elif choice=='6': determinant_calc()
        elif choice=='7': sqrt_calc()
        elif choice=='8': power_calc()
        elif choice=='9': linear_solver()
        elif choice=='10': inverse_matrix()
        elif choice=='11': temperature_converter()
        elif choice=='12': length_converter()
        elif choice=='13': area_perimeter()
        elif choice=='14': area_converter()
        elif choice=='15': volume_shapes()
        elif choice=='16': volume_converter()
        elif choice=='17': weight_converter()
        elif choice=='18': time_converter()
        elif choice=='19': speed_converter()
        elif choice=='20': pressure_converter()
        elif choice=='21': power_converter()
        elif choice=='22': number_converter()
        elif choice=='23': log_calc()
        elif choice=='24': exp_calc()
        elif choice=='25': percentage_calc()
        elif choice=='26': mean_median_mode()
        elif choice=='27': trig_calc()
        elif choice=='28': inverse_trig()
        elif choice=='29': degree_radian()
        elif choice=='0':
            print('Goodbye!')
            break
        else:
            print('Invalid choice')

menu()        