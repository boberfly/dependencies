{

	"downloads" : [

		"https://github.com/curl/curl/archive/refs/tags/curl-8_7_1.tar.gz"

	],

	"url" : "https://curl.se/",
	"license" : "COPYING",

	"commands" : [

		"mkdir gafferBuild",
		"cd gafferBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_INSTALL_LIBDIR={buildDir}/lib"
			" -D BUILD_CURL_EXE=OFF"
			" ..",
		"cd gafferBuild && make install -j {jobs} VERBOSE=1",

	],

	"manifest" : [

		"include/curl",
		"lib/*curl{sharedLibraryExtension}*",

	],

}
