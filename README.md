# Introduction

This is a configuration generator application for the VoIP Monitor. It provides an
easy-to-use GUI for understanding the configuration parameters, and guides in creating
a configuration file for your VoIP Monitor installation. This created config can then
be consumed by your installation very simply.

## How to Use

1. Simply clone the repository

    ```bash
    git clone https://github.com/demoncoder95/voipmonitor-config-generator.git
    ```

2. switch to the master branch

    ```bash
    git checkout master
    ```

3. Run the ``main.py`` script. It should work with all Python versions. I've tested
with ``Python 3.8.2``. The CLI version simply dumps all the available parameters
to the terminal and provides total count per category and the overall total count.

4. Run the ``gui_main.py`` script for the GUI version. You'll need to install
the ``PyQt5`` library. The GUI version allows for configuration generation by
selecting parameters through checkboxes. You can also preview the config
before saving it to a file.
