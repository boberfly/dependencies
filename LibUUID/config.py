{

	"downloads" : [

		"https://github.com/certik/uuid/archive/refs/heads/master.tar.gz"

	],

	"url" : "http://en.wikipedia.org/wiki/Util-linux",
	"license" : "COPYING.libuuid",

	"commands" : [

		"mkdir moonrayBuild",
		"cd moonrayBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" ..",
		"cd moonrayBuild && cmake --build . --config Release --target install -- {jobs}",

	],

	"manifest" : [

		"include/uuid",
		"lib/*uuid{sharedLibraryExtension}*",

	],

}
