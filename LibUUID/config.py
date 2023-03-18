{

	"downloads" : [

		"https://github.com/certik/uuid/archive/refs/heads/master.tar.gz"

	],

	"url" : "http://en.wikipedia.org/wiki/Util-linux",
	"license" : "COPYING.libuuid",

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",

	],

	"manifest" : [

		"include/uuid",
		"lib/*uuid{sharedLibraryExtension}*",

	],

}
