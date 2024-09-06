import webbrowser

f = open(" AboutMe.html", "w")

info = """"
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
        }a
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
            </tr>-
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

with open("AboutMe.html", "w") as f:
    f.write(info)
f.close()

filename = "AboutMe.html"
webbrowser.open_new_tab(filename)
