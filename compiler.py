from importlib.resources import contents
from os import listdir
from traceback import print_tb

start = '#include <Keyboard.h>\nvoid setup() {\n  delay(1000);\n'


def get_content():
    dir = listdir('./')
    for i in dir:
        if i.endswith('.ludo'):
            txt = i
    file = open('./' + txt, "r")
    content = file.read()
    content = content.split('\n')
    file.close()
    return content

def convert_to_arduino(content,arduino):
    for i in content:
        if i.endswith('pause'):
            i = i.replace(' pause','')
            add = '  delay(' + i + ');\n'
        elif i.startswith('ctrl'):
            i = i.replace('ctrl ','')
            add = '  Keyboard.press(KEY_LEFT_CTRL);\n  Keyboard.press("'+i+'");\n  delay(100);\n  Keyboard.releaseAll();\n'
        elif i.startswith('windows'):
            i = i.replace('windows ','')
            add = '  Keyboard.press(KEY_LEFT_GUI);\n  Keyboard.press("'+i+'");\n  delay(100);\n  Keyboard.releaseAll();\n'
        elif i.startswith('custom'):
            i = i.replace('custom ','')
            add = i
        else:
            if i == "":
                add = i
            else:
                add = '  Keyboard.print("' + i + '");\n'
        arduino += add
    return arduino



content = get_content()
arduino = convert_to_arduino(content,start)
arduino = arduino + '  Keyboard.releaseAll();\n  Keyboard.end();\n}\nvoid loop() '+"{"+"}"
print(arduino)