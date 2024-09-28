{

	"downloads" : [

		"https://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-0.9.71.tar.gz"

	],

	"url" : "https://www.gnu.org/software/libmicrohttpd/",

	"license" : "COPYING",

	"commands" : [

		"mkdir moonrayBuild",
		"cd moonrayBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D ENABLE_TESTS=NO"
			" -D ENABLE_EXAMPLES=NO"
			" -D ENABLE_DOC=NO"
			" -D ENABLE_HTTPS=NO" # todo: check if needed
			" ..",
		"cd moonrayBuild && cmake --build . --config Release --target install -- {jobs}",

	],

	"manifest" : [

		"include/microhttpd*",
		"lib/*microhttpd*",

	],

}
