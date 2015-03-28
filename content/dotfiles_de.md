Title: Dotfiles, oder warum ich GITHUB so mag
Date: 2015-03-27
Modified: 2015-03-25 21:00
Category: tech
Tags: dotfiles
Slug: dotfiles-und-git
lang: de
Authors: Hannes Bellmer
Summary: Wie man seine Dotfiles via Github synchronisiert 
Status: Published

#### Was sind dotfiles?
In _unixoiden_ Betriebssystemen werden ja bekanntlich die Einstellungen in
regulären Textdateien gespeichert. Dies hat den schönen Vorteil, dass man seine
Persönlichen Einstellungen einfach auf einen neuen Server/Workstation/etc
transferieren kann. 

#### Warum sollte ich Sie bei Github hochladen?
Mir war es immer etwas zu mühsam, alle Dateien händisch zu synchronisieren und
bei Änderungen alle Systeme zu aktualisieren. Deshalb habe ich vor vier Monaten
angefangen mich näher mit [GIT](https://github.com/git/git) zu Beschäftigen.

Jetzt könnte sich der geneigte Leser fragen, warum zum Geier brauche ich eine
Quellcodeverwaltung um meine 'blöden' Einstellungen zu verwalten? Naja, weil
es:

* Saucool ist
* Man Änderungen super verfolgen und Rückgängig machen kann.
* Mit einem `git fetch` man sofort sein System auf dem aktuellen Stand hat.
* Man seine Einstellungen prima via GITHUB teilen kann.
* Und natürlich macht GITHUB für einen quasi ein Backup seiner Dotfiles.

#### Und wie jetzt?
Am besten legt man ein Repository bei Github an und führt erstmal die folgenden
Schritte aus:

    :::bash
    mkdir ~/Dotfiles
    cd ~/Dotfiles
    echo "# Meine Dotfiles" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/$MyGithubUsername/Dotfiles.git
    git push -u origin master

Bitte daran denken den Github-namen anzupassen. Jetzt hat man einen erstmal
einen reguläres Verzeichnis, welches mit GIT synchronisiert werden kann. 

Jetzt kann man seine Konfigurationsdateien in dieses Verzeichnis verschieben
und mittels
[Symlinks](https://de.wikipedia.org/wiki/Symbolische_Verkn%C3%BCpfung) am alten
Ort die neue Konfiguration bekannt machen. Auf meinem Rechner sieht das wie
folgt aus:

    :::bash
    lrwxr-xr-x   1 hannes  staff    32B  9 Dez 20:16 .gitconfig -> /Users/hannes/Dotfiles/gitconfig
    lrwxr-xr-x   1 hannes  staff    31B  9 Dez 20:14 .screenrc -> /Users/hannes/Dotfiles/screenrc
    lrwxr-xr-x   1 hannes  staff    18B 30 Dez 14:10 .tmux.conf -> Dotfiles/tmux.conf
    lrwxr-xr-x   1 hannes  staff    26B  9 Dez 20:16 .vim -> /Users/hannes/Dotfiles/vim
    lrwxr-xr-x   1 hannes  staff    28B  9 Dez 20:16 .vimrc -> /Users/hannes/Dotfiles/vimrc


Es gibt im Netz so einige schicke Scripte, die sogar das Erzeugen der Symlinks
autorisieren und für die alten Dateien Sicherungen anlegen. Da ich zZ nur fünf
Datein und auf manchen Systemen noch zwei Symlinks in `/etc/profile.d` kann ich
dieses noch gerade so händisch erledigen.

##### Beispiele?
[Offizieller GH Dotfiles Seite](https://dotfiles.github.io/)   
[Meine Dotfiles](https://github.com/trulleberg/Dotfiles)   
[Svens Dotfiles][SVEN], Sven hat mich auf die Idee mit den Dotfiles gebracht ;)  



[SVEN]: https://github.com/Strubbl/dotfiles
