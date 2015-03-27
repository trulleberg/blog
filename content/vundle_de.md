Title: Vundle für VIM installieren
date: 2015-03-18
Modified: 2015-03-20
Category: tech
Tags: vim, dotfiles
lang: de
Slug: vundle-in-vim
Authors: Hannes Bellmer
Summary: Vundle, Installation und Benutzung.

Warum sollte ich Vundle nutzen?

1. Weil es dein leben mit VIM und Plungins soo einfach macht!
2. Es kann Plugins direkt aus Github installieren.
3. ....


#### Quick Start 
Geklaut von [Github](https://github.com/gmarik/Vundle.vim), einfach in die `.vimrc` kopieren und los geht es.

##### Eine Kopie runterladen

Einfach `git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim` ausführen. Natürlich muss git installiert sein.

##### Anpassen der *.vimrc*

Dies ist der "Vundle Teil" meiner `.vimrc`. 
Hiermit wird [nerdTree]({filename}/nerdtree_en.md), Syntax Highlight für [Docker](http://docker.com) & Markdown zu meiner VIM Umgebung hinzugefügt.


    :::vim
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " Vundle
    " """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    set nocompatible " be iMproved, required
    filetype off " required
    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')


    :::vim
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " Vundle
    " """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    set nocompatible " be iMproved, required
    filetype off " required
    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')
    " let Vundle manage Vundle, required
    Plugin 'gmarik/Vundle.vim'
    " Nerdtree, nothing to add
    Plugin 'scrooloose/nerdtree'
    " Syntax for Doccker files
    Plugin 'ekalinin/Dockerfile.vim'
    " Vim Markdown syntax hightlight
    Plugin 'godlygeek/tabular'
    Plugin 'plasticboy/vim-markdown'
    " All of your Plugins must be added before the following line
    call vundle#end() " required
    filetype plugin indent on " required
    " To ignore plugin indent changes, instead use:
    "filetype plugin on
    "
    " Brief help
    " :PluginList - lists configured plugins
    " :PluginInstall - installs plugins; append `!` to update or just
    " :PluginUpdate
    " :PluginSearch foo - searches for foo; append `!` to refresh local cache
    " :PluginClean - confirms removal of unused plugins; append `!` to
    " auto-approve removal
    "
    " see :h vundle for more details or wiki for FAQ
    " Put your non-Plugin stuff after this line

##### Installieren der Plugins:

Entweder:
Starte `vim` und tippe `:PluginInstall`

Oder via CLI:

 `vim +PluginInstall +qall`

