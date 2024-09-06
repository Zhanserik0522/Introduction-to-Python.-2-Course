# Ex 1
def simple_calculator():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")

        if operator not in ['+', '-', '*', '/', '%']:
            raise ValueError("Invalid operator")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error: Division by zero!")
                return
        elif operator == '%':
            try:
                result = num1 % num2
            except ZeroDivisionError:
                print("Error: Modulo by zero!")
                return

        print("Result:", result)

    except (ValueError, TypeError) as e:
        print("Error:", e)
    except ZeroDivisionError as e:
        print("Error:", e)


# Ex 2

import webbrowser

def create_about_me_page():
    try:
        filename = "AboutMe.html"
        with open(filename, "w") as f:
            info = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Personal Webpage</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                        text-align: center;
                    }
                    header {
                        background-color: #333;
                        color: #fff;
                        padding: 20px 0;
                    }
                    section {
                        padding: 20px;
                    }
                    img {
                        border-radius: 50%;
                        width: 150px;
                        height: 150px;
                        margin-bottom: 20px;
                    }
                    table {
                        margin: 0 auto;
                    }
                    table, th, td {
                        border: 1px solid #333;
                        border-collapse: collapse;
                    }
                    th, td {
                        padding: 10px;
                    }
                </style>
            </head>
            <body>
                <header>
                    <h1>Zhenisov Zhanserik</h1>
                </header>
                <section>
                    <img src="C:\\Users\\nurpe\\Downloads\\profile.jpeg" alt="Profile Picture">
                    <table>
                        <tr>
                            <th>Age</th>
                            <td>18</td>
                        </tr>
                        <tr>
                            <th>Brief Information</th>
                            <td> A young specialist, Student of IITU</td>
                        </tr>
                        <tr>
                            <th>Email</th>
                            <td>zhenisovzhanserik05@gmail.com</td>
                        </tr>
                        <tr>
                            <th>Birth Country</th>
                            <td>The Republic of Kazakhstan</td>
                        </tr>
                        <tr>
                            <th>Hobbies</th>
                            <td>Reading, Games, Sport</td>
                        </tr>
                        <tr>
                            <th>Study Interests</th>
                            <td>Data Science</td>
                        </tr>
                        <tr>
                            <th>Languages</th>
                            <td>Kazakh (native), Russian (proficient), English(pre)</td>
                        </tr>
                        <tr>
                            <th>Programming/IT Skills</th>
                            <td>C++, Python, Java</td>
                        </tr>
                    </table>
                </section>
            </body>
            </html>
            """
            f.write(info)
        print("AboutMe.html created successfully!")
        return filename
    except Exception as e:
        print("Error:", e)
        return None

def open_webpage(filename):
    try:
        if filename:
            webbrowser.open_new_tab(filename)
        else:
            print("Error: Couldn't open webpage due to previous errors.")
    except Exception as e:
        print("Error:", e)

def main():
    filename = create_about_me_page()
    open_webpage(filename)

if __name__ == "__main__":
    main()

