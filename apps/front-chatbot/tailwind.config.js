/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#e6e3e4',
          100: '#d9d5d6',
          200: '#ccc7c8',
          300: '#bfb9ba',
          400: '#b2abac',
          500: '#545454',
          600: '#4a4a4a',
          700: '#404040',
          800: '#363636',
          900: '#000000',
        },
        secondary: {
          50: '#e5dfd2',
          100: '#ddd5c4',
          200: '#d5cbb6',
          300: '#cdc1a8',
          400: '#c5b79a',
          500: '#545454',
          600: '#4a4a4a',
          700: '#404040',
          800: '#363636',
          900: '#000000',
        },
        accent: {
          50: '#e6e3e4',
          100: '#d9d5d6',
          200: '#ccc7c8',
          300: '#bfb9ba',
          400: '#b2abac',
          500: '#545454',
          600: '#4a4a4a',
          700: '#404040',
          800: '#363636',
          900: '#000000',
        },
        fashion: {
          black: '#000000',
          gray: '#545454',
          light: '#e6e3e4',
          cream: '#e5dfd2',
        }
      },
      fontFamily: {
        sans: ['Poppins', 'system-ui', 'sans-serif'],
        display: ['Poppins', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
        'fashion-gradient': 'linear-gradient(135deg, #000000 0%, #545454 50%, #e5dfd2 100%)',
        'glass-gradient': 'linear-gradient(135deg, rgba(230,227,228,0.15) 0%, rgba(229,223,210,0.08) 100%)',
      },
      backdropBlur: {
        xs: '2px',
      },
      animation: {
        'fade-in': 'fadeIn 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
        'slide-up': 'slideUp 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
        'slide-in-right': 'slideInRight 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
        'slide-in-left': 'slideInLeft 0.4s cubic-bezier(0.4, 0, 0.2, 1)',
        'scale-in': 'scaleIn 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
        'float': 'float 3s ease-in-out infinite',
        'glow': 'glow 2s ease-in-out infinite alternate',
        'shimmer': 'shimmer 2s linear infinite',
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideInRight: {
          '0%': { transform: 'translateX(20px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        slideInLeft: {
          '0%': { transform: 'translateX(-20px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        glow: {
          '0%': { boxShadow: '0 0 20px rgba(136, 99, 56, 0.3)' },
          '100%': { boxShadow: '0 0 30px rgba(136, 99, 56, 0.6)' },
        },
        shimmer: {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(100%)' },
        },
      },
      boxShadow: {
        'fashion': '0 10px 40px rgba(2, 2, 2, 0.1)',
        'fashion-lg': '0 20px 60px rgba(2, 2, 2, 0.15)',
        'glass': '0 8px 32px rgba(0, 0, 0, 0.1)',
        'glow': '0 0 20px rgba(136, 99, 56, 0.4)',
        'inner-fashion': 'inset 0 2px 4px rgba(2, 2, 2, 0.1)',
      },
    },
  },
  plugins: [],
}
