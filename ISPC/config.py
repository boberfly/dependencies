{

	"url" : "https://ispc.github.io/",

	"license" : "LICENSE.txt",

	"dependencies" : [],

	"commands" : [

		"cp bin/ispc {buildDir}/bin/ispc",

	],

	"manifest" : [

		"bin/ispc",

	],

	"platform:linux" : {

		"downloads" : {

			"https://github.com/ispc/ispc/releases/download/v1.23.0/ispc-v1.23.0-linux.tar.gz"

		},


	},

	"platform:macos" : {

		"downloads" : {

			"https://github.com/ispc/ispc/releases/download/v1.23.0/ispc-v1.23.0-macOS.tar.gz"

		},

	},

	"platform:windows" : {

		"downloads" : {

			"https://github.com/ispc/ispc/releases/download/v1.23.0/ispc-v1.23.0-windows.zip"

		},

	},

}
