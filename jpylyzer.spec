# -*- mode: python -*-
a = Analysis(['.\cli.py'],
             pathex=['.\jpylyzer'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name='jpylyzer.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries +
               [('./license/LICENSE.txt','LICENSE','DATA')],
               [('./doc/jpylyzerUserManual.html','./doc/jpylyzerUserManual.html','DATA')],
               [('./example_files/balloon.jp2','./example_files/balloon.jp2','DATA')],
               [('./example_files/balloon_trunc1.jp2','./example_files/balloon_trunc1.jp2','DATA')],
               [('./example_files/balloon_trunc2.jp2','./example_files/balloon_trunc2.jp2','DATA')],
               [('./example_files/balloon_trunc3.jp2','./example_files/balloon_trunc3.jp2','DATA')],
               [('./example_files/readme.txt','./example_files/readme.txt','DATA')],
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='jpylyzer')
