# ECAD functions and utilities library

This library contains commonly used functions and tools with regard to ECAD Tool automation, here with Siemens Xpedition Designer.
It also contains IntelliSense stub module generator which is used to assist development of Automation Scripts by means of code autocompletion.
More information about the generator can be found [here:](./designer_lib_gen/README.md).

Directory structure:

* designer_ifc - mockup module containing constants defined by Designer; module is iported as 'constants' and it can be used in Automation Scripts executed internally and externally 
* designer_lib_gen - python script used to generate Designer stub for autocompletion; additional [info:](./designer_lib_gen/README.md) 

## Usage

### 0. Prerequisites
```
# COM interface Python Module (start from installation Directory of the desired Python installation, e.g. C:\app\Python311)
python -m pip install pywin32
```
### 1. Generate COM interface classes
```
# Generate the Python file containing COM interface classes (already creating .py file for 'ViewDraw' (=Xpedition Desinger))
python mpy.py
```
This is the tool to be used for Designer (when makepy.py from within mp.py is passed with no arguments)

![Designer](images/COM-Library-Xpedition-Designer.jpg)


This is the tool to be used for Layout

![Layout](images/COM-Library-Xpedition-Layout.jpg)


Similarly it works for Fablink, Constraint Management, etc.

File containing library COM ifc classes will be generated:
![COM module](images/Generated_COM-Module.jpg)

### 2. Extending COM interface (optional: Need to be done when switching to newer Xpedition Designer Release)

Generated file can be used together with Visual Studio Code (VSCode) IDE to enable autocompletion function.
One can use ‘sniff’ tool to add COM-object properties into classes which were generated with, as those will not be available from 
original description file generated by makepy utility. Following script generates properties for ‘Designer’ tool.

```
# Generate the Python file containing COM interface classes
python sniff_designer_ifc.py 
```
Copy the generated file into this folder [here:](./designer_ifc.py).

Example for autocompletion:
![autocompletion](images/VSCode_autocompletion_example.JPG)
Aonnation in the code is required to get this to work. See designer_template.py for annotation examples (objApplalication and objComp).

### 3. Use the designer_template.py as starting point for your code
```
python designer_template.py
```

## License

This project is open-source and available under the [MIT License](LICENSE).
"""


