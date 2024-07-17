
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/jdemaray/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/jdemaray/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/jdemaray/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/jdemaray/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# Below is good; I want to make directory info purple though
PS1='%F{reset}[%F{green}%n%F{red}@%m %F{blue}%~%F{reset}]%F{green}$ %f'

export CLICOLOR=1
alias ls='ls -G'
alias ll='ls -lG'

export DYLD_LIBRARY_PATH=/opt/homebrew/Cellar/openslide/4.0.0/lib:$DYLD_LIBRARY_PATH

