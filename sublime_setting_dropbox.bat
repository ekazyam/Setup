:: Move Sublime text Setting.
move "C:\Users\%username%\AppData\Roaming\Sublime Text 3\Installed Packages" "C:\Users\%username\Dropbox\"
move "C:\Users\%username%\AppData\Roaming\Sublime Text 3\Packages" "C:\Users\%username\Dropbox\"

::Make Symbol Link
mklink /d "C:\Users\%username%\AppData\Roaming\Sublime Text 3\Installed Packages" "C:\Users\%username%\Dropbox\SublimeText3\Installed Packages"
mklink /d "C:\Users\%username%\AppData\Roaming\Sublime Text 3\Packages" "C:\Users\%username%\Dropbox\SublimeText3\Packages"
