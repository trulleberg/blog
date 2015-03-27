Title: How to install nerdTree in vim
date: 2015-03-19
Modified: 2015-03-19
Category: tech
Tags: vim, dotfiles
Slug: nerdtree-in-vim
lang: en
Authors: Hannes Bellmer
Summary: How to install nerdtree and quick usage


[vundle]({filename}/vundle_en.md) is the recommended way to install nerdtree.

Best is to add `Plugin 'scrooloose/nerdtree'`to the `.vimrc`, restart vim and type `:PluginInstall`

##### Adjustments
I made the following adjustments in my `.vimrc` like posted in my [Dotfiles](https://github.com/trulleberg)
   
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

##### Usage
Every now and then I am VIM and need to lookup something from another file, now I just press "CTRL+n", navigate to the file, press *i* and have t
he content I need in my vim buffer.

##### Source
Go to [Github](https://github.com/scrooloose/nerdtree) and have fun:
