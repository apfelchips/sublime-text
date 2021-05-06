# My Sublime-Text Config

**Clone commands for different platforms:**

## macOS
```sh
git clone git@github.com:apfelchips/sublime-text-3.git "${HOME}/Library/Application Support/Sublime Text 3"
```

## Linux
```sh
git clone git@github.com:apfelchips/sublime-text-3.git "${XDG_CONFIG_HOME:-$HOME/.config}/sublime-text-3"
```

## Windows
*Powershell*:
```ps1
Remove-Item "${env:LocalAppData}\Sublime Text 3\" # Index/Cache dir
git clone git@github.com:apfelchips/sublime-text-3.git "${env:AppData}\Sublime Text 3"
```
