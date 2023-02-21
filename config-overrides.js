const path = require('path');


module.exports = {
    paths: function (paths, env) {        
        paths.appIndexJs = path.resolve(__dirname, 'react/index.js');
        paths.appSrc = path.resolve(__dirname, 'react');
        paths.appBuild = path.resolve(__dirname, 'src/swan/specterext/spa/static/app');
        // paths.appPublic = path.resolve(__dirname, 'react/public');
        // paths.appHtml = path.resolve(__dirname, 'react/public/index.html');
        return paths;
    },
    webpack: function (config, env) {
        config.output.filename = 'static/js/[name].[hash].js';
        config.output.publicPath = "/svc/spa/app"
        return config;
    }
}