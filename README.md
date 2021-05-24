# My Sublime-Text Config

**Clone commands for different platforms:**

## macOS
```sh
git clone --recursive git@github.com:apfelchips/sublime-text-3.git "${HOME}/Library/Application Support/Sublime Text"
```

## Linux
```sh
git clone --recursive git@github.com:apfelchips/sublime-text-3.git "${XDG_CONFIG_HOME:-$HOME/.config}/sublime-text"
```

## Windows
*Powershell*:
```ps1
Remove-Item -Recurse -EA 0 "${env:LocalAppData}\Sublime Text\" # Index/Cache dir
git clone --recursive git@github.com:apfelchips/sublime-text-3.git "${env:AppData}\Sublime Text"
```
