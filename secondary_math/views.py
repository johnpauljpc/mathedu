from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

import math
from .formulas import simple_interest, quadratic
from .formulas.comGraphics.dda import DDA

from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import pyplot as plt
import io
import base64

# Create your views here.
class DDA_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sec/dda.html')
    
    def post(self, request, *args, **kwargs):
        x0 =float(request.POST.get('x0', 0))
        y0 =float(request.POST.get('y0', 0))

        x1 =float(request.POST.get('x1', 0))
        y1 =float(request.POST.get('y1', 0))

        # Call the DDA function with sample coordinates
        
        x_coordinates, y_coordinates, x_inc, y_inc = DDA(x0, y0, x1, y1)

        # Generate the plot
        plt.plot(x_coordinates, y_coordinates, marker="o", markersize=5, markerfacecolor="black")
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.title('DDA graph')
        plt.grid(True)
        print(x_coordinates)
        print(y_coordinates)

        coordinates = []
        for x, y, x_inc, y_inc in zip(x_coordinates, y_coordinates, x_inc, y_inc):
            coordinates.append({"x":(x), "y":y, 'x_inc':x_inc, 'y_inc':y_inc})

        # Save the plot as a byte stream
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Encode the image to base64
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
        plt.close()

        # Render the HTML template with the image data
        return render(request, 'sec/dda.html', {'image_base64': image_base64,
                                             'cord':coordinates,
                                             'data':request.POST})

dda_line_generation = DDA_View.as_view()

class IndexView(View):
    def get(self, request):
        return render(request, "sec/index.html")


index_view = IndexView.as_view()


class SimpleInterest(View):
    def get(self, request):
        return render(request, "sec/simple-interest.html")

    def post(self, request):
        P = float(request.POST["principal"])
        R = float(request.POST.get("rate"))
        T = float(request.POST.get("time"))
        choice = request.POST.get("choice", "simple_interest")
        I = None
        CI = None
        i_tot = None
        amount = None
        compound_rate = None
        compound_rate_add = None
        compound_rate_exp = None

        print(f"data:  {request.POST}, {P}")
        try:
            if choice == "compound_interest":
                CI, amount = simple_interest.CompoundInterest(P=P, R=R, T=T)
                compound_rate = R/100
                compound_rate_add = compound_rate + 1
                compound_rate_exp = round((math.pow(compound_rate_add, T)), 4)
            else:
                I = simple_interest.SI(P=P, R=R, T=T)
                i_tot = P * R * T

        except Exception as err:
            print(f"error   {err}")
            messages.error(request, f"something is wrong! \n {err}")
            return render(
                request, "sec/simple-interest.html", {"data": request.POST}
            )
        context = {
            "s_interest": I,
            "i_tot": i_tot,
            "comp_interest": CI,
            "amount": amount,
            "compound_rate":compound_rate,
            "compound_rate_add":compound_rate_add,
            "compound_rate_exp":compound_rate_exp,
            "data": request.POST,
        }

        return render(request, "sec/simple-interest.html", context)


simple_interest_view = SimpleInterest.as_view()


class CompoundInterest(View):
    def get(self, request):
        return render(request, "sec/compound-interest.html")

    def post(self, request):
        P = float(request.POST["principal"])
        R = float(request.POST.get("rate"))
        T = float(request.POST.get("time"))
        choice = request.POST.get("choice", "compound_interest")
        I = None
        CI = None
        i_tot = None
        amount = None
        compound_rate = None
        compound_rate_add = None
        compound_rate_exp = None

        print(f"data:  {request.POST}, {P}")
        try:
            if choice == "compound_interest":
                CI, amount = simple_interest.CompoundInterest(P=P, R=R, T=T)
                compound_rate = R/100
                compound_rate_add = compound_rate + 1
                compound_rate_exp = round((math.pow(compound_rate_add, T)), 4)
            else:
                I = simple_interest.SI(P=P, R=R, T=T)
                i_tot = P * R * T

        except Exception as err:
            print(f"error   {err}")
            messages.error(request, f"something is wrong! \n {err}")
            return render(
                request, "sec/compound-interest.html", {"data": request.POST}
            )
        context = {
            "s_interest": I,
            "i_tot": i_tot,
            "comp_interest": CI,
            "amount": amount,
            "compound_rate":compound_rate,
            "compound_rate_add":compound_rate_add,
            "compound_rate_exp":compound_rate_exp,
            "data": request.POST,
        }

        return render(request, "sec/compound-interest.html", context)


compound_interest_view = CompoundInterest.as_view()


class Simultaneous_LE(View):
    def get(self, request):
        return render(request, "sec/simultanous.html")

    def post(self, request):
        return render(request, "sec/simultanous.html")


simultaneous_LE_view = Simultaneous_LE.as_view()


# Quadratic equation
class QuadraticView(View):
    def get(self, request):
        return render(request, "sec/quadratic.html")

    def post(self, request):
        a = float(request.POST.get("a", 0))
        b = float(request.POST.get("b", 0))
        c = float(request.POST.get("c", 0))

        root1 = None
        root2 = None

        try:
            root1, root2, msg = quadratic.solve_quadratic(a=a, b=b, c=c)
            if msg:
                messages.info(request, msg)
        except Exception as err:
            messages.warning(request, f"{err}")

        context = {"root1": (root1), "root2": root2, 'data':request.POST}

        return render(request, "sec/quadratic.html", context)


quadratic_view = QuadraticView.as_view()


# custom 404 view
def custom_404_view(request, exception):
    return redirect('/')