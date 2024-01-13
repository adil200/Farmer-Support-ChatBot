/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      maxWidth: {
        '3/4': '75%'
      },
      fontFamily: {
        'anton': 'Anton',
        'poppins': 'Poppins',
        'bebas': 'Bebas Neue',
      }
    },
  },
  plugins: [],
}
