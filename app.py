from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "dev-secret-key"


def compute_operation(value_a: float, value_b: float, operator: str) -> float:
    if operator == "add":
        return value_a + value_b
    if operator == "subtract":
        return value_a - value_b
    if operator == "multiply":
        return value_a * value_b
    if operator == "divide":
        if value_b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return value_a / value_b
    raise ValueError("Unsupported operation")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    first = request.form.get("first", "")
    second = request.form.get("second", "")
    operator = request.form.get("operator", "add")

    if request.method == "POST":
        if not first or not second:
            flash("Please provide values for both numbers.")
        else:
            try:
                value_a = float(first)
                value_b = float(second)
                result = compute_operation(value_a, value_b, operator)
            except ValueError:
                flash("Please enter valid numeric values.")
            except ZeroDivisionError:
                flash("Division by zero is not allowed.")

    return render_template("index.html", result=result, first=first, second=second, operator=operator)


if __name__ == "__main__":
    app.run(debug=True)
