import colors from "vuetify/es5/util/colors";
import i18n from './config/i18n'
require('dotenv').config()
export default {
  target: 'static',

  server:{
    host: '0.0.0.0',
    port: 3005,
  },
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: "%s System",
    title: "Abnormal detection",
    htmlAttrs: {
      lang: "en"
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" }
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }]
  },
  ssr: false,
  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ["@/assets/scss/main.scss"],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    "@/plugins/global-functions.js",
    "@/plugins/global-components.js",
    "@/plugins/local-storage"
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,
  axios: {
    proxy: true,
    credentials: false,
    baseURL:  process.env.BASE_URL || 'http://127.0.0.1:8080/api/'
  },

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    "@nuxtjs/vuetify",
    "@nuxtjs/axios",
    "@nuxtjs/auth-next",
    "nuxt-i18n",
    'cookie-universal-nuxt',
    'bootstrap-vue/nuxt',
    '@plugins/axios',
    '@nuxtjs/dotenv',
  ],
  i18n: {
    vueI18nLoader: true,
    locales: ["en", "vi"],
    defaultLocale: "en",
    vueI18n: i18n
  },
  env: {
    baseUrl: process.env.BASE_URL
  },
  auth: {
    localStorage: false,
    cookie: {
      options: {
        expires: 1
      }
    },
    strategies: {
      local: {
        scheme: 'refresh',
        refreshToken: {
          property: 'refresh',
          data: 'refresh',
          maxAge: 60 * 60 * 24 * 30
        },
        endpoints: {
          token: {
            property: 'token',
            // required: true,
            // type: 'Bearer'
          },
          local:false,
          refresh: {
            url: "/api/token/refresh/",
            method: "post",
            propertyName: false
          }, // change to your refresh token url
          logout: false,
          user: { url: "/users/me", method: "get", propertyName: false }
        }
      }
    }
  },
  styleResources: {
    scss: ["./assets/scss/*.scss"]
  },
  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [],

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ["~/assets/variables.scss"],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {}
};
