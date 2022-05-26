const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
  content: [
    "./resources/**/*.{html, js, css}",
    "./templates/**/*.{html,js}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        'dark':'#171817',
        'heading': "#fdad00"
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}