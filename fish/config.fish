if status is-interactive
# Commands to run in interactive sessions can go here
end
set fish_greeting
starship init fish | source
zoxide init --cmd cd fish | source

#fzf colors
if test -f ~/.cache/wal/fzf.fish
    source ~/.cache/wal/fzf.fish
end


set -gx EDITOR '/usr/bin/nvim'
