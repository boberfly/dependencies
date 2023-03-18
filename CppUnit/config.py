{

	"downloads" : [

		"http://dev-www.libreoffice.org/src/cppunit-1.15.1.tar.gz"

	],

	"url" : "https://freedesktop.org/wiki/Software/cppunit/",

	"license" : "COPYING",

	"dependencies" : [],

	"commands" : [

		"./configure --prefix {buildDir}",
		"make install",

	],

	"manifest" : [

		"include/cppunit",
		"lib/*cppunit*",

	],

}
