userInput = '1' #change to make it from gui
pausePog
inputs= ['0.5', '1', '1.5', '2']
inputmm = ['50', '100', '150', '200']

inc_value = ''

for x,y in zip(inputs, inputmm):
    if inputs(x) = userInput
        inc_value = inputmm(y)

### gcode file creation

total_incs_direction = 900 / int(inc_value)

x_val = 0
y_val = 0
z_val = 0
pausePog = 500
gcode_file = open("gcode_" + inc_value, "w+")

for z in range(0, total_incs+1):
    gcode_file.write("X%i Y%i Z%i")
    z_val = z_val + int(inc_value)
    gcode_file.write("G4 P" + str(pausePog))   
    for y in range(0, total_incs +1):
        gcode_file.write("X%i Y%i Z%i")
        gcode_file.write("G4 P" + str(pausePog))
        y_val = y_val + int(inc_value)
        for x in range(0, total_incs +1):
            gcode_file.write("X%i Y%i Z%i \n", [x_val, y_val, z_val])
            gcode_file.write("G4 P" + str(pausePog))
            x_val = x_val + int(inc_value)
