
# Useful things about coding for this project

not only for this project, but in general my current Visual Studio Code status is:

## Current Visual Studio Code setup

### Theme

Dark+ (Default dark)
I'have tried some of great color scheme available... but nothing total satisfying me!
However this themes was installed:

- Monokai Pro
- One Dark Pro

### Extensions

- :emojisense:
- Bracket Pair Colorizer 2
- Italian Language Pack for Visual Studio Code
- Live Share
- Markdown All in One
- Markdown Preview Github Styling
- Markdownlint
- Prettier - Code formatter
- Python
- Remote VSCode
- Spell Right
- Todo Tree
- vscode-icons

### Other settings

Nothing special here... :thinking:

___

# Python specific useful notes

A few example of base header and skeleton that I use:

```python
#!/usr/bin/python
# name_of_module
#
# GNU Public License version 3 - See http://www.gnu.org/licenses/licenses.html
#
# (c) Fabio Celsalonga
#
# useful description and instructions
# ...
# ...
#
# Version x.x YYYY-MM-DD
```

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
name_of_module.py: Description of what the module does, and other useful things

Copyright (c) 2019 Fabio Celsalonga
MIT License

"""

# Imports
import sys
#import os

# Global variables

# Class declarations

# Function declarations

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--flags options] [inputs] ')
        sys.exit(1)

# Main body
if __name__ == '__main__':
    main()

```

See also on template directory to use other start project file.