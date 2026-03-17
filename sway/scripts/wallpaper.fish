#!/usr/bin/fish

set fzf_preview_cmd 'kitten icat --clear --transfer-mode=memory --stdin=no --place "$FZF_PREVIEW_COLUMNS"x"$FZF_PREVIEW_LINES"@"$FZF_PREVIEW_LEFT"x"$FZF_PREVIEW_TOP" {}'

set choice (fzf --walker-root=$HOME/wallpapers \
    --layout=reverse \
    --border \
    --preview=$fzf_preview_cmd)

if test -n "$choice"
    wal -i "$choice"
    python3 /home/pave/dotfiles/sway/scripts/waybar-constrast.py
    pkill swaybg
    swaymsg exec "swaybg -i '$choice' -m fill"
end
