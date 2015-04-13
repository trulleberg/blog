Title: Spellcheck in VIM
Date: 2015-04-13
Category: tech
Tags: vim
Slug: spellcheck-vim
lang: de
Authors: Hannes Bellmer
Summary: Spellcheck in VIM
Status: Published

#### Rechtschreibkontrolle in VIM
Ich denke jeder kennt es, es gibt immer wieder Worte die bei denen man
Buchstabendreher hat oder sich immer wieder vertippt. Solltest du VI/VIM nutzen
kannst du recht einfach die Rechtschreibkontrolle aktivieren.

Folgende Liste ist für mich als Gedächtnisstütze gedacht. 

    :set spell          => Aktiviert den Spellcheck
    :set nospell        => Deaktiviert den Spellcheck
    :set spelllang=de   => deutsch
    z=                  => Vorschläge für falsch geschriebenes Wort
    zg                  => Wort in eigenes Wörterbuch aufnehmen

#### Was noch?
Sollte sich gerade die tollen Kürzel `z=` und `zg` nicht in meinem Hirn
verfestigen, werde ich mir bestimmt einen Alias erzeugen.

#### Wenn ich Standard-Einstellungen möchte?
Dann einfach folgendes in die `.vimrc`eintragen:

    set spell
    set spellang=de,en
