# Daisy World project


DaisyWorld_clean.ipynb is the Jupyter Notebook that will have to adapt, it is now a non-functional code, you have to fix it with information from the assignment description in the DaisyWorld_assignment.docx.. 

# Run

To run the notebooks **in the cloud** using Binder(https://mybinder.org) click on this badge:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VU-IVM/Learning_Python/master)

# Install Python
To run the notebooks **locally** you need to have python installed. We strongly recommend to install Python rather sooner then later. The whole procedure should take around 15-20 minutes. To install Python, we advice to use a Minicoda(https://docs.conda.io/en/latest/miniconda.html) distribution. Install the Python 3.7 64 bit for your OS (MACOSX or Windows). 
When opening your terminal, you can now use 'conda' functionality manage your Python installation (creating environments and installing packages). 

- Mac has a terminal by default, you can open via spotlight (cmd+space) and then type terminal, press enter. 
- For Windows you will need to install the terminal first, with [this Youtube movie](https://www.youtube.com/watch?v=mByMbtyew_E), you can simultaneously have small dance (also recommended) while installing the terminal. 

Next, open the terminal and create a new conda environment. The environment.yml (likely) contains the packages that you will need for all the tutorials and practicums that you will do during your studies. After you installed anaconda, type the following in you terminal
`conda env create -f environment.yml`. 

We have named the environment 'ivm_github'. Activate the conda environment by typing:
'conda activate ivm_github'

After installation, download the repository from Github, open the terminal and go to the folder that you downloaded, then type (and wait a few seconds, the notebook will launch in your internet browser):
'jupyter notebook'


