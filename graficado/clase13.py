from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("clase13.html")
    p = figure()

    total_vals = int(input("Enter the number of values to plot: "))
    x_vals = list(range(total_vals))
    y_vals = []

    for i in x_vals:
        val = int(input(f"Enter value for x={i}: "))
        y_vals.append(val)

    p.line(x_vals, y_vals, line_width=2)
    show(p)