#⚡️yoo⚡️


####A simple and small python2🐍 script that can help you to init a react & webpack project.

***Yoo*** will help you to create some simple files, such as config file of webpack and the package.json of npm. You may need to provide your project infomation in the cli when ***yoo*** is init the project. And After that, then he will install dependencies uses npm. when finished installing dependencies, proton will uses the webpack to pack the html, js, css, and other static files.

####I wish you will enjoy it ! 😀

##🏠Initial Organization

* build/
	* entry.js
* node_modules/
	* css-loader/
	* file-loader/
	* jsx-loader/
	* react/
	* react-dom/
	* style-loader/
	* url-loader/
* index.html
* entry.js
* index.css
* package.json
* webpack.config.js

###Dependencies
- node.js
- npm
- python2.7

###Installation
	pip install yoo

###Usage
	 yoo --dir <project_dir_url>
	 
######Argument *--dir* is used to specify the project directory. Default is PWD.