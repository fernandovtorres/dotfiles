return {
    'neovim/nvim-lspconfig',
    dependencies = {
        'mason-org/mason.nvim',
        'mason-org/mason-lspconfig.nvim',
        'j-hui/fidget.nvim',
        'saghen/blink.cmp'
    },
    config = function()

        local capabilities = vim.lsp.protocol.make_client_capabilities()
        if capabilities.textDocument and capabilities.textDocument.completion then
            capabilities.textDocument.completion.completionItem.snippetSupport = true
        end

        vim.lsp.config('*', { 
            capabilities = require('blink.cmp').get_lsp_capabilities()
        })
        vim.lsp.config('lua_ls', {
            settings = {
                Lua = {
                    runtime = { version = "Lua 5.1" },
                    diagnostics = {
                        globals = { "vim" },
                    }
                }
            }
        })

        require('fidget').setup({})
        require('mason').setup()
        require('mason-lspconfig').setup({
            ensure_installed = {
                "lua_ls",
                "pyright",  -- ensure it stays installed
            },
            automatic_enable = {
                exclude = { 'jdtls' }
            },
        })

        vim.diagnostic.config({
            float = {
                focusable = false,
                style = "minimal",
                border = "rounded",
                source = "always",
                header = "",
                prefix = "",
            },
        })
    end
}
