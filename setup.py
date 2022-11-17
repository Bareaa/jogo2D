import cx_Freeze

executables = [cx_Freeze.Executable(script="jogo.py", icon="assets/clarencio.ico")]
cx_Freeze.setup( name="jogo do clarencio", options={"build.exe":{"packages":["pygame"],"include_files":["assets"]}}, executables = executables)