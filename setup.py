import cx_Freeze

executables = [cx_Freeze.Executable(
    script="main.py",
    icon="assets/food.ico"
)]
cx_Freeze.setup(
    name="Catch The Food",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["assets"]
        }}
    ,executables = executables
)