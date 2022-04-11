const colors = require('tailwindcss/colors')
module.exports = {
  content: [
    "./resources/**/*.css",
    "./resources/**/*.js",
    "./templates/**/*.html",
  ],
  theme: {
    colors:{
      slate: colors.slate,
    },
  },
  plugins: [],
}