# Default editor
c.editor.command = ['kitty', '-e', 'nvim', '{file}', '-c', 'normal {line}G{column0}l']

# Privacy
config.load_autoconfig(False)
config.set("content.blocking.enabled", True)
config.set("content.cookies.accept", "never")
config.set("content.cookies.store", True)
config.set("content.blocking.method", "both")


# Persistent logins
config.set("content.cookies.accept", "all", "*://*.reddit.com/*")
config.set("content.cookies.accept", "all", "*://*.youtube.com/*")
config.set("content.cookies.accept", "all", "*://*.google.com/*")
config.set("content.cookies.accept", "all", "*://*.withgoogle.com/*")
config.set("content.cookies.accept", "all", "*://*.google.com.br/*")
config.set("content.cookies.accept", "all", "*://*.usp.br/*")
config.set("content.cookies.accept", "all", "*://*.telegram.org/*")
config.set("content.cookies.accept", "all", "*://*.github.com/*")
config.set("content.cookies.accept", "all", "*://*.geeksforgeeks.org/*")
config.set("content.cookies.accept", "all", "*://*.whatsapp.com/*")
config.set("content.cookies.accept", "all", "*://*.overleaf.com/*")
config.set("content.cookies.accept", "all", "*://*.wolframalpha.com/*")
config.set("content.cookies.accept", "all", "*://*.canva.com/*")
config.set("content.cookies.accept", "all", "*://*.leetcode.com/*")
config.set("content.cookies.accept", "all", "*://*.linkedin.com/*")
config.set("content.cookies.accept", "all", "*://*.figma.com/*")
config.set("content.cookies.accept", "all", "*://*.sampa-curso.org/*")
config.set("content.cookies.accept", "all", "*://*.claude.ai/*")


# Vertical tabs
c.tabs.position = "left"
c.tabs.width = "5%"

# Search Engines
c.url.searchengines = {
        'DEFAULT': 'https://duckduckgo.com/?q={}',
        '!aw': 'https://wiki.archlinux.org/?search={}',
        '!yt': 'https://www.youtube.com/results?search_query={}',
        '!re': 'https://www.reddit.com/search/?q={}'
        }

# Completion

c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

# Dark Mode
config.set('colors.webpage.darkmode.enabled', False, 'file://*')


# Colorscheme
#c.colors.webpage.darkmode.enabled = False
#c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
#c.colors.webpage.darkmode.policy.images = 'never'
c.colors.webpage.preferred_color_scheme = 'dark'


import json
import os

color_file = os.path.expanduser('~/.cache/wal/colors.json')

def load_colors(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"background": "#000000", "foreground": "#ffffff"}

colors = load_colors(color_file)

bg = colors["special"]["background"]
fg = colors["special"]["foreground"]
colorss = colors["colors"]


c.colors.statusbar.normal.bg = bg
c.colors.statusbar.command.bg = colorss["color14"]
# c.colors.statusbar.normal.bg = bg
# c.colors.statusbar.command.bg = bg
c.colors.statusbar.command.fg = colorss["color0"]
c.colors.statusbar.normal.fg = colorss["color14"]
c.colors.statusbar.passthrough.fg = colorss["color14"]
c.colors.statusbar.url.fg = colorss["color13"]
c.colors.statusbar.url.success.https.fg = colorss["color13"]
c.colors.statusbar.url.hover.fg = colorss["color12"]
# c.statusbar.show = "always"

c.colors.tabs.even.bg = colorss["color0"] # transparent tabs!!
c.colors.tabs.odd.bg = colorss["color0"]
c.colors.tabs.bar.bg = bg
# c.colors.tabs.even.bg = bg
# c.colors.tabs.odd.bg = bg
c.colors.tabs.even.fg = colorss["color13"]
c.colors.tabs.odd.fg = colorss["color12"]
c.colors.tabs.selected.even.bg = colorss["color13"] 
c.colors.tabs.selected.odd.bg = colorss["color12"] 
c.colors.tabs.selected.even.fg = colorss["color0"]
c.colors.tabs.selected.odd.fg = colorss["color0"]
c.colors.hints.bg = bg
c.colors.hints.fg = fg
c.tabs.show = "multiple"

c.colors.completion.item.selected.match.fg = colorss["color6"]
c.colors.completion.match.fg = colorss["color6"]

c.colors.tabs.indicator.start = colorss["color10"]
c.colors.tabs.indicator.stop = colorss["color8"]

c.colors.completion.odd.bg = bg
c.colors.completion.even.bg = bg
c.colors.completion.fg = fg
c.colors.completion.category.bg = bg
c.colors.completion.category.fg = fg
c.colors.completion.item.selected.bg = bg
c.colors.completion.item.selected.fg = fg

c.colors.messages.info.bg = bg
c.colors.messages.info.fg = fg
c.colors.messages.error.bg = bg
c.colors.messages.error.fg = fg
c.colors.downloads.error.bg = bg
c.colors.downloads.error.fg = fg

c.colors.downloads.bar.bg = bg
c.colors.downloads.start.bg = colorss["color10"]
c.colors.downloads.start.fg = fg
c.colors.downloads.stop.bg = colorss["color8"]
c.colors.downloads.stop.fg = fg

c.colors.tooltip.bg = bg
c.colors.webpage.bg = bg
c.hints.border = fg
