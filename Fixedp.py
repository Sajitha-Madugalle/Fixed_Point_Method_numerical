def fixed_point(g, x0, n):
    results = []

    for i in range(n):
        x1 = g(x0)
        relative_error = abs((x1 - x0) / x1) * 100
        results.append([i + 1, x1, relative_error])

        x0 = x1

    print("Iteration\tCurrent Answer\tRelative Error")
    print("-" * 45)

    for row in results:
        print(row[0], "\t\t", row[1], "\t\t", row[2])

    return x1, relative_error

function = input("Enter the function (use 'x' as the variable): ")
g_x = lambda x: eval(function)

x0 = float(input("Enter the initial guess: "))
iterations = int(input("Enter the number of iterations: "))

answer, relative_error = fixed_point(g_x, x0, iterations)
print("Answer is converging to", answer, "with a relative error of", relative_error)
