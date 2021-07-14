def arithmetic_arranger(problems, show_answer=False):
    # problems - list of strings e.g. ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    # returns the problems arranged vertically and side-by-side.
    # When 'show_answer'  is  True, the answers should be displayed.

    problems_count = len(problems)
    first_line, second_line, underline, result_line = "", "", "", ""

    if problems_count > 5:
        return "Error: Too many problems."

    for problem in problems:

        first_number, second_number, operator = problem.split()
        # input error check
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        elif operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        # if input is OK
        if operator == "+":
            result = int(first_number) + int(second_number)
        else:
            result = int(first_number) - int(second_number)
        # forming result lines
        width = max(len(first_number), len(second_number)) + 2
        first_line += first_number.rjust(width) + "    "
        second_line += operator + second_number.rjust(width - 1) + "    "
        underline += "-" * width + "    "
        result_line += str(result).rjust(width) + "    "

    arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + underline.rstrip() + (
                '\n' + result_line.rstrip()) * show_answer

    return arranged_problems
