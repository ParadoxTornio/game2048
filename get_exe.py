import cx_Freeze


executables = [cx_Freeze.Executable('game.py',
                                    base='Win32GUI',
                                    icon='images/icon.ico',
                                    shortcut_dir='DesktopFolder',
                                    shortcut_name='2048')]
cx_Freeze.setup(
    name='2048', options={'build_exe': {'excludes':['tkinter'], 'packages': ['arcade'],
                                           'include_files': ['images']},
                          "bdist_msi": {'target_name': '2048.msi', 'install_icon': 'images/icon.ico'}},
    executables=executables)
