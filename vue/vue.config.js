const path = require("path");

module.exports = {
  configureWebpack:{
    resolve:{
      alias: {
        '@': path.resolve(__dirname,'src'),
      }
    },
    devServer:{
      host: '0.0.0.0',
      port:8080,
      allowedHosts: "all",
    }
  }

}
