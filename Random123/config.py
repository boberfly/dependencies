{
	"downloads" : [

		"https://github.com/DEShawResearch/random123/archive/refs/tags/v1.14.0.tar.gz"

	],

	"url" : "https://github.com/DEShawResearch/random123",

	"license" : "LICENSE",

	"commands" : [

		"cp -R include/Random123 {buildDir}/include/Random123",

	],

	"manifest" : [

		"include/Random123",

	],

	"platform:windows" : {

		"commands" : [

			"xcopy /E /I include\\Random123 {buildDir}\\include\\Random123",

		]

	}

}