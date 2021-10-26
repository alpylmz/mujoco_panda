


out = ""

for i in range(0,8):
    starting_x = 0.4
    starting_y = -0.4
    for j in range(0,8):
        number = i * 8 + j
        out += "<body name=\"table{}\" pos=\"{:.2f} {:.2f} 0.01\">\n".format(number, starting_x + i * 0.1, starting_y + j * 0.1)
        out += "    <geom name=\"table{}_geom\" class=\"block_collision\" size =\".05 .05 0.01\" ".format(number)
        number = i + j
        if number % 2:
            out += "rgba=\"255 255 255 1\" friction=\"2.5 0.005 0.0001\" mass = \"20\" type=\"box\"/>\n"
        else:
            out += "rgba=\"0 0 0 1\" friction=\"2.5 0.005 0.0001\" mass = \"20\" type=\"box\"/>\n"
        out += "</body>\n"

out += "<body name=\"kutu1\" pos=\"0.5 -0.3 0.6\">\n"
out += "    <geom name=\"kutu1_geom\" class=\"block_collision\" size =\".025 .025 0.02\" "
out += "rgba=\"128 128 0 1\" friction=\"2.5 0.005 0.0001\" mass = \"0.0001\" type=\"box\"/>\n"
out += "</body>\n"

print(out)