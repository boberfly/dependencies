{

	"downloads" : [

		"https://github.com/log4cplus/log4cplus/archive/refs/tags/REL_1_1_2.tar.gz"

	],

	"url" : "https://sourceforge.net/projects/log4cplus/",

	"license" : "LICENSE",

	"dependencies" : [],

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",

	],

	"manifest" : [

		"include/log4cplus",
		"lib/liblog4cplus*",

	],

}
