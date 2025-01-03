# ECAD functions and utilities library for Xpedition Constraints Management

This toolbox contains commonly used functions and tools with regard to ECAD Tool automation, here with Siemens Xpedition Constraints Manager.
It also contains IntelliSense stub module generator which is used to assist development of Automation Scripts by means of code autocompletion.
More information about the generator can be found [here:](./constraintmanager_lib_gen/README.md).

Directory structure:

* constraintmanager_ifc - mockup module containing constants defined by Constraint-Manager; module is iported as 'constants' and it can be used in Automation Scripts executed internally and externally 
* constraintmanager_lib_gen - python script used to generate Constraint-Manager stub for autocompletion; additional [info:](./constraintmanager_lib_gen/README.md) 

## Usage

### 0. Prerequisites
```
# COM interface Python Module (start from installation Directory of the desired Python installation, e.g. C:\app\Python311)
python -m pip install pywin32
```
### 1. Generate COM interface classes
```
# Generate the Python file contaz011ining COM interface classes
python mpy.py
```
This is the tool to be used for Constraint-Manager (when makepy.py from within mp.py is passed with no arguments)

![Constraint-Manager](images/COM-Library-Xpedition-Constraint-Manager.jpg)

### 2. Extending COM interface (optional: Need to be done when switching to newer Xpedition Constraint-Manager Release)

Generated file can be used together with Visual Studio Code (VSCode) IDE to enable autocompletion function.
One can use ‘sniff’ tool to add COM-object properties into classes which were generated with, as those will not be available from 
original description file generated by makepy utility. Following script generates properties for ‘Constraint-Manager’ tool.

```
# Generate the Python file containing COM interface classes
python sniff_constraintmanager_ifc.py 
```
Copy the generated file into this folder [here:](./constraintmanager_ifc.py).

Example for autocompletion:
![autocompletion](images/VSCode_autocompletion_example.JPG)
Annotation in the code is required to get this to work. See constraintmanager_template.py for annotation examples (objApplalication and objComp).

### 3. Use the constraintmanager_template.py as starting point for your code
```
python constraintmanager_template.py
```

## License

This project is open-source and available under the [MIT License](LICENSE).
"""


