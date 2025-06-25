from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pygame"],
    "include_files": [
        ("assets", "assets"),
        ("code/menu.py", "menu.py"),
        ("code/game.py", "game.py"),
        ("code/player.py", "player.py"),
        ("code/enemy.py", "enemy.py"),
        ("code/bullet.py", "bullet.py"),
        ("code/enemy_bullet.py", "enemy_bullet.py"),
        ("code/explosion.py", "explosion.py"),
        ("code/config.py", "config.py")
    ]
}

setup(
    name="CityShooter",
    version="1.0",
    description="Jogo com pygame",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("code/main.py", base="Win32GUI", target_name="CityShooter.exe")
    ]
)
