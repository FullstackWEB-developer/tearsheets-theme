module.exports = {
    theme: {
        extend: {
            screens: {
                'xs': '480px',
                'sm': '600px',
                'md': '960px',
                'lg': '1280px',
                'xl': '1920px',
                'print': { 'raw': 'print' },
                // => @media print { ... }
            }
        }
    },
    variants: {},
    plugins: [
        require('@tailwindcss/ui'),
        require('@tailwindcss/forms'),
    ]
}