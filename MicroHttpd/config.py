{

	"downloads" : [

		"https://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-0.9.71.tar.gz"

	],

	"url" : "https://www.gnu.org/software/libmicrohttpd/",

	"license" : "COPYING",

	"dependencies" : [],

	"commands" : [

		"./configure --prefix {buildDir}",
		"make install",

	],

	"manifest" : [

		"include/microhttpd*",
		"lib/*microhttpd*",

	],

}
