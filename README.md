# My Sublime-Text Config

**Clone commands for different platforms:**

## macOS
```sh
rm -rf "${HOME}/Library/Application Support/Sublime Text"

git clone --recursive git@github.com:apfelchips/sublime-text.git "${HOME}/Library/Application Support/Sublime Text"
```

## Linux
```sh
rm -rf "${XDG_CONFIG_HOME:-$HOME/.config}/sublime-text"

git clone --recursive git@github.com:apfelchips/sublime-text.git "${XDG_CONFIG_HOME:-$HOME/.config}/sublime-text"
```

## Windows
*Powershell*:
```ps1
Remove-Item -Recurse -EA 0 "${env:LocalAppData}\Sublime Text\" # Index/Cache dir
Remove-Item -Recurse -EA 0 "${env:AppData}\Sublime Text\"

git clone --recursive git@github.com:apfelchips/sublime-text.git "${env:AppData}\Sublime Text"
```
