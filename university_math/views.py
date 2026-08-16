import logging

from django.shortcuts import render, redirect
from django.views import View

from mathedu_core.expressions import ExpressionError, build_equation
from mathedu_core.roots import (
    bisection_method,
    has_root_between,
    newton_raphson_method,
    successive_approximation,
)

logger = logging.getLogger(__name__)


class FindRootsView(View):
    def get(self, request):
        return render(request, "uni/index.html")

    def post(self, request):
        interval1 = request.POST.get("interval1")
        interval2 = request.POST.get("interval2")
        eqn = request.POST.get("equation")
        tol = request.POST.get("tolerance")
        method = request.POST.get("root_method")

        def error_render(message, **extra):
            context = {"data": request.POST, "error_msg": message}
            context.update(extra)
            return render(request, "uni/index.html", context)

        # Validate interval bounds.
        try:
            a = float(interval1)
            b = float(interval2)
        except (TypeError, ValueError):
            return error_render("values for interval must be numeric")
        if a >= b:
            return error_render(
                "interval1 must be less than interval2", interval1_err=True
            )

        # Validate tolerance.
        try:
            tolerance = float(tol)
            if tolerance < 0.000001:
                raise ValueError
        except (TypeError, ValueError):
            return error_render("tolerance value is invalid", tol_error=True)

        # Parse the equation safely (no eval) and build f(x).
        try:
            equation = build_equation(eqn)
        except ExpressionError as err:
            return error_render(str(err), eqn_err=True)

        context = {"data": request.POST}

        if method == "newton_raphson":
            context["method"] = "Newton Raphson"
            try:
                root = newton_raphson_method(equation, initial_guess=a)
                if root.get("other_results") is None:
                    return error_render(
                        "root not found! kindly check your intervals and tolerance"
                    )
                table_data = [
                    {
                        "res": res,
                        "x_i": x_i,
                        "fx": fx,
                        "fx1": fx1,
                        "e": e,
                    }
                    for res, x_i, fx, fx1, e in zip(
                        root["other_results"],
                        root["x_i"],
                        root["fx"],
                        root["fx1"],
                        root["e"],
                    )
                ]
                context.update(method=context["method"], result=root["result"], table_data=table_data)
            except Exception as err:
                logger.warning("newton_raphson failed: %s", err)
                return error_render(
                    "root not found! kindly check your intervals and tolerance"
                )

        elif method == "bisection":
            context["method"] = "Bisection"
            if not has_root_between(equation, interval1, interval2):
                return error_render(
                    f"root does not exist between {interval1} and {interval2}"
                )
            try:
                root = bisection_method(equation, a, b, tolerance)
                table_data = [
                    {"a": a, "b": b, "c": c, "b_c": b_c, "func": func}
                    for a, b, c, b_c, func in zip(
                        root["a"], root["b"], root["other_results"], root["b_c"], root["func"]
                    )
                ]
                context.update(method=context["method"], result=root["result"], table_data=table_data)
            except Exception as err:
                logger.warning("bisection failed: %s", err)
                return error_render(
                    "root not found! kindly check your intervals and tolerance"
                )

        elif method == "successive_approximation":
            context["method"] = "Successive Approximation"
            if not has_root_between(equation, interval1, interval2):
                return error_render(
                    f"root does not exist between {interval1} and {interval2}"
                )
            try:
                root = successive_approximation(equation, a, b, tolerance, max_iter=1000)
                if root["result"].startswith("Root not found"):
                    return error_render(root["result"])
                context.update(method=context["method"], result=root["result"])
            except Exception as err:
                logger.warning("successive_approximation failed: %s", err)
                return error_render(
                    "root not found! kindly check your intervals and tolerance"
                )

        else:
            return error_render("please select a root-finding method")

        return render(request, "uni/index.html", context)


find_roots = FindRootsView.as_view()


def custom_404_view(request, exception):
    return redirect("index")


def custom_500_view(request):
    return render(request, "500.html", status=500)