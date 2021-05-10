The folder contains 3 sub-folders:

1. BASIC - basic fire spread along with density, prob_burning and problem size variation
2. q1a - FIRE spread model with time required for burning = 2.
3. q2 - FIRE spread model with probabilitic model for cell to catch fire.

Each of these sub-folder contains 2 python files:

1. simulate - to generate gif and initial condition
2. density_vary - to obtain graphs for density variation.
3. size_vary - to obtain graphs for size variation (only for basic sub-folder)

The subfolders also contain all the relevant data (gif and graphs to view)
Note:

A. Run all of the files via a text editor (preferably vscode) which support python 3.7 and above.
B. In each of the problems there is a python list , S=[], which contains the problem sizes.If you wish to run it for the deafult condition run as it is, else put the desired values seperated by a comma in the list.
C. For simulate.py files the initial forest condition plot needs to be closed to see the animation window. 