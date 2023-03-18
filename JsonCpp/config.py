{

	"downloads" : [

		"https://github.com/open-source-parsers/jsoncpp/archive/refs/tags/1.9.5.tar.gz"

	],

	"url" : "https://github.com/open-source-parsers/jsoncpp",

	"license" : "LICENSE",

	"dependencies" : [ "Python" ],

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D JSONCPP_LIB_BUILD_SHARED:BOOL=ON"
			" -D JSONCPP_WITH_TESTS:BOOL=OFF"
			" -D JSONCPP_WITH_POST_BUILD_UNITTEST:BOOL=OFF"
			" -D PYTHON_EXECUTABLE={buildDir}/bin/python"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",

	],

	"manifest" : [

		"include/json",
		"lib/*jsoncpp*",

	],

}
