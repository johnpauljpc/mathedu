import base64
import io
import logging

from django.shortcuts import redirect, render
from django.views.generic import View
from matplotlib import pyplot as plt

from mathedu_core.algebra import solve_quadratic
from mathedu_core.finance import compound_interest, simple_interest
from mathedu_core.graphics import dda_line

logger = logging.getLogger(__name__)


class DDAView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "sec/dda.html")

    def post(self, request, *args, **kwargs):
        try:
            x0 = float(request.POST.get("x0"))
            y0 = float(request.POST.get("y0"))
            x1 = float(request.POST.get("x1"))
            y1 = float(request.POST.get("y1"))
        except (TypeError, ValueError):
            return render(
                request,
                "sec/dda.html",
                {"data": request.POST, "error_msg": "coordinates must be numeric"},
            )

        x_coordinates, y_coordinates, x_inc, y_inc = dda_line(x0, y0, x1, y1)

        plt.plot(x_coordinates, y_coordinates, marker="o", markersize=5, markerfacecolor="black")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.title("DDA graph")
        plt.grid(True)

        coordinates = [
            {"x": x, "y": y, "x_inc": x_inc_i, "y_inc": y_inc_i}
            for x, y, x_inc_i, y_inc_i in zip(x_coordinates, y_coordinates, x_inc, y_inc)
        ]

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
        plt.close()

        return render(
            request,
            "sec/dda.html",
            {
                "image_base64": image_base64,
                "cord": coordinates,
                "data": request.POST,
            },
        )


dda_line_generation = DDAView.as_view()


class IndexView(View):
    def get(self, request):
        return render(request, "sec/index.html")


index_view = IndexView.as_view()


class InterestView(View):
    template_name = "sec/simple-interest.html"
    default_choice = "simple_interest"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            principal = float(request.POST.get("principal"))
            rate = float(request.POST.get("rate"))
            time = float(request.POST.get("time"))
        except (TypeError, ValueError):
            return render(
                request,
                self.template_name,
                {"data": request.POST, "error_msg": "principal, rate and time must be numeric"},
            )

        choice = request.POST.get("choice", self.default_choice)

        try:
            if choice == "compound_interest":
                ci, amount = compound_interest(principal, rate, time)
                context = {
                    "comp_interest": ci,
                    "amount": amount,
                    "compound_rate": rate / 100,
                    "compound_rate_add": 1 + rate / 100,
                    "compound_rate_exp": round((1 + rate / 100) ** time, 4),
                    "data": request.POST,
                }
            else:
                si = simple_interest(principal, rate, time)
                context = {
                    "s_interest": si,
                    "i_tot": principal * rate * time,
                    "data": request.POST,
                }
        except Exception as err:
            logger.warning("interest calculation failed: %s", err)
            return render(
                request,
                self.template_name,
                {"data": request.POST, "error_msg": "something went wrong with the calculation"},
            )

        return render(request, self.template_name, context)


simple_interest_view = InterestView.as_view()


class CompoundInterestView(InterestView):
    template_name = "sec/compound-interest.html"
    default_choice = "compound_interest"


compound_interest_view = CompoundInterestView.as_view()


class QuadraticView(View):
    def get(self, request):
        return render(request, "sec/quadratic.html")

    def post(self, request):
        try:
            a = float(request.POST.get("a"))
            b = float(request.POST.get("b"))
            c = float(request.POST.get("c"))
        except (TypeError, ValueError):
            return render(
                request,
                "sec/quadratic.html",
                {"data": request.POST, "error_msg": "a, b and c must be numeric"},
            )

        root1 = None
        root2 = None
        error_msg = None

        try:
            root1, root2, msg = solve_quadratic(a=a, b=b, c=c)
            error_msg = msg
        except ValueError as err:
            error_msg = str(err)
        except Exception as err:
            logger.warning("quadratic failed: %s", err)
            error_msg = "something went wrong with the calculation"

        return render(
            request,
            "sec/quadratic.html",
            {"root1": root1, "root2": root2, "error_msg": error_msg, "data": request.POST},
        )


quadratic_view = QuadraticView.as_view()


def custom_404_view(request, exception):
    return redirect("/")