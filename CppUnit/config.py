{

	"downloads" : [

		"http://dev-www.libreoffice.org/src/cppunit-1.15.1.tar.gz"

	],

	"url" : "https://freedesktop.org/wiki/Software/cppunit/",

	"license" : "COPYING",

	"commands" : [

		"mkdir moonrayBuild",
		"cd moonrayBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=ON"
			" ..",
		"cd moonrayBuild && cmake --build . --config Release --target install -- {jobs}",

	],

	"manifest" : [

		"include/cppunit",
		"lib/*cppunit*",

	],

}
