from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('cursorMove.py', base=base)
]

setup(name='cursorMove',
      version = '1.0',
      description = 'A simple program that listens for a particular keyboard shortcut and moves the cursor to the top left of the primary monitor when the shortcut is pressed.',
      options = dict(build_exe = buildOptions),
      executables = executables)
