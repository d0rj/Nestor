# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\Projects\\Python\\nestor'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['cv2', 'numpy', 'win32', '_ssl', 'PIL', 'PIL.Image', 'lib2to3', 'encoding', 'distutils', 'PySide', 'pkg_resources', 'PySide2', 'PySide2.QtCore', 'PySide2.QtGui', 'pycparser', 'win32com', 'xml', 'xml.dom.domreg', 'xml.etree.cElementTree'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
