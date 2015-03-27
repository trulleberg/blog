Title: Nerdtree in VIM installieren
Date: 2015-03-19
Modified: 2015-03-24
Category: tech
Tags: vim, dotfiles
Slug: nerdtree-in-vim
lang: de
Authors: Hannes Bellmer
Summary: Nerdtree, installation und einfache Nutzung


Warum Nerdtree?
Weil ich so super einfach im Dateibaum navigieren kann ohne VIM verlassen zu müssen. 

Wie: 
Ich empfehle [vundle]({filename}/vundle_de.md) weil es nicht einfacher geht.

### SupereasyVundleInstal
Einfach `Plugin 'scrooloose/nerdtree'` zur `.vimrc` hinzufügen, VIM neu starten und `:PluginInstall` eingeben!

##### Anpassungen
Folgende Anpassungen in der `.vimrc` machen mir mein Leben leichter, siehe auch meine [Dotfiles](https://github.com/trulleberg)
   
    :::vim
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " Options for NERDTree, from https://github.com/scrooloose/nerdtree
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " Open NERDTree when no file is spcified!
    autocmd StdinReadPre * let s:std_in=1
    autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
    " CTRL N Toggles NERDTree
    "map <silent> <C-n> :NERDTreeFocus<CR>
    map <silent> <C-n> :NERDTreeToggle<CR>
    " Close vim if NERDTree is the last windows
    autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif 

##### Nutzung
Regelmäßig muss ich in verschiedenen Dateien nach Inhalten suchen und diese in Zusammenhang bringen. Einfach "STRG+n" drücken, die gewünschte Datei auswählen und schwupp schon kann ich einfach beide Datein anschauen.

##### Quelle
[Github](https://github.com/scrooloose/nerdtree)
