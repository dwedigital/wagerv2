const colors = require('tailwindcss/colors')
module.exports = {
  content: [
    "./resources/**/*.{html, js, css}",
    "./templates/**/*.{html,js}",
  ],
  theme: {
    colors:{
      transparent: 'transparent',
      current: 'currentColor',
      slate: colors.slate,
    },
  },
  plugins: [],
}