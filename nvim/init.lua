vim.cmd("set conceallevel=2")
require("config.lazy")
vim.cmd.colorscheme "pywal16"

vim.o.number = true
vim.o.relativenumber = true
vim.o.wrap = false
vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.swapfile = false
vim.o.mouse = 'a'
vim.o.showmode = false
vim.schedule(function()
    vim.o.clipboard  = 'unnamedplus'
end)
vim.cmd("set expandtab")
vim.cmd("set expandtab")
vim.o.breakindent = true
vim.o.undofile = true
vim.o.ignorecase = true
vim.o.smartcase = true
vim.o.splitright = true
vim.o.splitbelow = true
vim.o.confirm = true
vim.opt.signcolumn = 'yes'
vim.opt.updatetime = 250
vim.opt.timeoutlen = 300

vim.g.mapleader = ' '
vim.g.have_nerd_font = true

vim.keymap.set('n', '<Esc>', '<cmd>nohlsearch<CR>')
vim.keymap.set('n', '[d', vim.diagnostic.goto_prev)
vim.keymap.set('n', ']d', vim.diagnostic.goto_next)
vim.keymap.set('n', '<C-h>', '<C-w><C-h>', { desc = 'Ir para esquerda' })
vim.keymap.set('n', '<C-l>', '<C-w><C-l>', { desc = 'Ir para direita' })
vim.keymap.set('n', '<C-j>', '<C-w><C-j>', { desc = 'Ir para baixo' })
vim.keymap.set('n', '<C-k>', '<C-w><C-k>', { desc = 'Ir para cima' })
vim.keymap.set('n', '<leader>ee', '<cmd>Oil<CR>')

vim.diagnostic.config( {update_in_insert= true })
