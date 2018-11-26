const path = require('path');

module.exports = {
    mode: "production",

    entry: {
        "form": "./jsx/form.jsx"
    },

    output: {
        path: path.resolve(__dirname, "plugins/static"),
        filename: "[name].pack.js"
    },

    module: {
        rules: [
            {
                test: /\.jsx?$/,
                include: [
                    path.resolve(__dirname, "jsx")
                ],
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: [
                            "@babel/preset-env",
                            "@babel/preset-react"
                        ]
                    }
                },
            }
        ]
    }
}