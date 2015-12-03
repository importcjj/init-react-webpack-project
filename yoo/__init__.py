# -*- coding:utf-8 -*-

import os
import os.path
import subprocess
import argparse

pwd = os.getcwd()

parser = argparse.ArgumentParser('init a react project.')
parser.add_argument(
    '--dir',
    dest='project_dir',
    default=pwd,
    help='A specific project directory')

webpack = """module.exports = {
    entry: {
        entry: './entry.js'
    },
    output: {
        path: './build',
        filename: '[name].js',
        publicPath: './build'
    },
    module: {
        loaders : [
            {test: /\.js$/, loader: 'jsx-loader'},
            {test: /\.css$/, loader: 'style-loader!css'},
            {test: /\.(png|jpg)$/, loader: 'url-loader?size=8192'}
        ]
    }
}
"""
devDependencies = [
    'react',
    'react-dom',
    'css-loader',
    'file-loader',
    'jsx-loader',
    'style-loader',
    'url-loader'
]

index = """<!DOCTYPE html>
<html>
<head>
    <title>Fo</title>
</head>
<body>
<div id="hello-react"></div>
<h4>Created by Fo</h4>
<script type="text/javascript" src="./build/entry.js"></script>
</body>
</html>
"""

entry = """
require('./index.css')
var React = require('react');
var ReactDOM = require('react-dom');

var HelloProton = React.createClass({
    render: function () {
        return <h1>Hello Fo</h1>
    }
});

ReactDOM.render(
    <HelloProton/>,
    document.getElementById('hello-react')
);
"""
css = """
* {
    margin: 0;
    padding: 0;
}

body {
    text-align: center;
}
"""


def main(project_dir):
    try:
        os.chdir(project_dir)
    except OSError:
        os.mkdir(project_dir)
        os.chdir(project_dir)

    with open('webpack.config.js', 'w') as f:
        f.write(webpack)
    with open('entry.js', 'w') as f:
        f.write(entry)
    with open('index.html', 'w') as f:
        f.write(index)
    with open('index.css', 'w') as f:
        f.write(css)

    subprocess.call(['npm', 'init'])
    subprocess.call(['npm', 'install', '--save-dev'] + devDependencies)
    subprocess.call(['webpack'])

if __name__ == '__main__':
    args = parser.parse_args()
    project_dir = args.project_dir
    main(project_dir)
