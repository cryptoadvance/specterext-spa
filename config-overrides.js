const path = require('path');


module.exports = {
    paths: function (paths, env) {        
        paths.appIndexJs = path.resolve(__dirname, 'react/index.js');
        paths.appSrc = path.resolve(__dirname, 'react');
        return paths;
    },
    webpack: function (config, env) {
        config.output.filename = 'static/js/[name].[hash].js';
        config.output.publicPath = "/svc/spa/app"
        return config;
    }
}