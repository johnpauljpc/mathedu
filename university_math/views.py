from django.shortcuts import render, redirect
import math

import sympy
from django.contrib import messages
from .val_checker import check_number

# Create your views here.
from django.shortcuts import render
from .utils import (bisection, raphson_newton, 
                    successive_approx, test_roots)

from django.views import View
from .utils.replacement_of_non_x import replace_non_x_alphabet
from .utils.RE import interpret_expression
from .utils.add_math_func import replace_math_functions

class Find_roots_View(View):
    def get(self, request):
        
        return render(request, "uni/index.html")

    def post(self, request):

        interval1 = request.POST['interval1']
        interval2 = request.POST['interval2']
        eqn = request.POST['equation']
        tol = request.POST['tolerance']
        method = request.POST['root_method']

        context = None
      

        # Set the initial interval and tolerance
        if check_number(tol):
            print("Whatsuo")
        else:
            print("false")
        try:
            a = float(interval1)
            b = float(interval2)
            if a >= b:
                messages.error(request, f"interval1 must be less than interval2")
                return render(request, 'uni/index.html', {"data":request.POST, "interval1_err":True})

        except:
            messages.error(request, f"values for interval must be numeric")
            return render(request, 'uni/index.html', {"data":request.POST})

        try:
            if (float(tol)) >= 0.000001:
                tolerance = float(tol)
            else:
                raise Exception
        except:
            
            messages.error(request, f"tolerance value is invalid")
            return render(request, 'uni/index.html', {"data":request.POST, "tol_error":True})

        # Change every non x alphabet to x
        # temp_eqn = replace_non_x_alphabet(eqn)
        temp_eqn = replace_math_functions(eqn.lower())
        print(temp_eqn)
        #interprets 2x as 2*x
        interpret_expr = interpret_expression(temp_eqn) #interprets 2x as 2*x
        print("interpret_expr:  ", interpret_expr)
        # filtered_equation = interpret_expr.replace("^", "**")
        
        # print("++++++++++++++++++++++")
        # print(filtered_equation)
        
        
        def equation(x):
            return eval(interpret_expr)
        

        # Test Script to check if the equation suplied if valid
        def eqTest(x = 1):
            return eval(interpret_expr)
        
        try:
            eq = eqTest()
            print("eq     >: ", eq)
        except Exception as err:
            print("test error:   ",err)
            messages.error(request, f"your equation <b>{eqn}</b> is invalid ")
            return render(request, 'uni/index.html', {"data":request.POST, "eqn_err":True})
        # The end of the test script
        
        
        
        

        #####       Using  Newton Raphson method      ########
        if method == "newton_raphson":
            option = "Newton Raphson"
            try:
                root = raphson_newton.newton_raphson_method(equation, initial_guess = a)
                # "e":e, "x_i":x_i, "fx":fx, "fx1":fx1
               
                res = root['other_results']
                x_i = root['x_i']
                fx = root["fx"]
                fx1 = root["fx1"]
                error_limit = root["e"]

                table_data = []
                for res, x_i, fx, fx1, e in zip(res, x_i, fx, fx1, error_limit):
                    table_data.append({"res":res, "x_i":x_i, "fx":fx, "fx1":fx1, "e":e})
                print(table_data)
                context = {
                    "method":option,
                    "result":root['result'],
                    "table_data": table_data,
                    "data":request.POST,
                    
                 }
            except Exception as err:
                messages.info(request, f"root not found! kindly check your intervals and tolerance")
                print("error------> ", err)
                return render(request, 'uni/index.html', {"data":request.POST})
        


        #####       Using  Bisection method      ########
        if method == "bisection":
            option = "Bisection"
            try:
                test_root = test_roots.test_root(interval1, interval2, expr=interpret_expr)
                root = bisection.bisection_method(equation, a, b, tolerance)
                a = root["a"]
                b = root["b"]
                c = root["other_results"]
                b_c = root["b_c"]
                func = root["func"]

                table_data = []
                for a, b, c, b_c, func in zip(a,b,c, b_c, func):
                    table_data.append({"a":a, "b":b, "c":c, "b_c":b_c, "func":func})
                
                
                
                context = {
                    "method":option,
                    "result":root['result'],
                    "table_data": table_data,
                    "data":request.POST,
                    
                 }
                if test_root == False:
                    messages.info(request, f"root does not exist between {interval1} and {interval2}")
                    return render(request, 'uni/index.html', {"data":request.POST})

            except Exception as err:
                messages.info(request, f"root not found! kindly check your intervals and tolerance")
                print("error------> ", err)
                return render(request, 'uni/index.html', {"data":request.POST})
            
        
        
        #####       Using  Bisection method      ########
        if method == "successive_approximation":
            option = "Successive Approximation"
            try:
                root = successive_approx.successive_approximation(f = equation, a = a, b = b, tol = tolerance, max_iter = 1000)
                test_root = test_roots.test_root(interval1, interval2, expr=interpret_expr)
                if test_root == False:
                    messages.info(request, f"root does not exist between {interval1} and {interval2}")
                    return render(request, 'uni/index.html', {"data":request.POST})
                
                elif root['result'] == f"Root not found within maximum iterations (1000).":
                    # err = f"Root not found within maximum iterations (1000). and within the <b>intervals</b> ({a} - {b})"
                    err = f"not found"
                    
                    messages.info(request, f"{root['result']}")
                    return render(request, 'uni/index.html', {"data":request.POST, "error":err,"method":option, "result":err })
                
                else:
                    return render(request, 'uni/index.html', {"data":request.POST,"method":option, "result":root['result']})
                    

            except Exception as err: 
                messages.info(request, f"root not found! kindly check your intervals and tolerance")
                print("error------> ", err)
                return render(request, 'uni/index.html', {"data":request.POST})
    

        print("------------------------------------")
        # print(root)
        # # The solutions 
        # try:
        #     context
        # except Exception as err:
        #     messages.error(request, f"something is wrong!")
        #     return render(request, 'index.html', {"data":request.POST})


      
        return render(request, 'uni/index.html', context)

find_roots = Find_roots_View.as_view()

# custom 404 view
def custom_404_view(request, exception):
    return redirect('index')

def custom_500_view(request):
    return render(request, '500.html', status=500)

# custom 403 view
# def custom_403_view(request, exception):
#     return render(request, "403_csrf.html")
