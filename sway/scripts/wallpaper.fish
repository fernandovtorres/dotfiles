#!/usr/bin/fish

set fzf_preview_cmd 'kitten icat --clear --transfer-mode=memory --stdin=no --place "$FZF_PREVIEW_COLUMNS"x"$FZF_PREVIEW_LINES"@"$FZF_PREVIEW_LEFT"x"$FZF_PREVIEW_TOP" {}'

set wal_script_path '~/.config/sway/scripts/pywal16'

set choice (fzf --walker-root=$HOME/wallpapers \
    --layout=reverse \
    --border \
    --preview=$fzf_preview_cmd)

if test -n "$choice"
    wal -i "$choice" -o "$wal_script_path"
    pkill swaybg
    swaymsg exec "swaybg -i '$choice' -m fill"
end
