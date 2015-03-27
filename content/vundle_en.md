Title: How to install vundle in vim
date: 2015-03-18
Modified: 2015-03-20
Category: tech
Tags: vim, dotfiles
lang: en
Slug: vundle-in-vim
Authors: Hannes Bellmer
Summary: How to install Vundle and quick usage

Why should you use Vundle?  => because it makes you vim-plugin-file sooo easy that you never want to manually do all this again. 

Vundle can get a name of a plugin as it appears in the vim plugin directory, a github “:user/:repo” style string, and even a full git url.


#### Quick Start 
Taken from the [Github Page](https://github.com/gmarik/Vundle.vim) and inserted my own config as posted in my [Dotfiles](https://github.com/trulleberg/Dotfiles).

##### Clone the repository

Issue `git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim` in your home directory.

##### Adjust your *.vimrc*

This is part of my config. It installs Vundle itself, [nerdTree]({filename}/nerdtree_en.md), Syntax Highlight for [Docker](http://docker.com) & Markdown

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

##### Install Plugins:

Launch `vim` and run `:PluginInstall`. 

To install from command line: `vim +PluginInstall +qall`

