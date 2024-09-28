{

	"downloads" : [

		"https://github.com/log4cplus/log4cplus/releases/download/REL_2_1_1/log4cplus-2.1.1.tar.gz"

	],

	"url" : "https://sourceforge.net/projects/log4cplus/",

	"license" : "LICENSE",

	"commands" : [

		"mkdir moonrayBuild",
		"cd moonrayBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_BUILD_TYPE=Release"
			" -D LOG4CPLUS_ENABLE_DECORATED_LIBRARY_NAME=OFF"
			" -D WITH_UNIT_TESTS=OFF"
			" -D LOG4CPLUS_BUILD_TESTING=OFF"
			" -D LOG4CPLUS_BUILD_LOGGINGSERVER=OFF"
#			" -D LOG4CPLUS_ENABLE_THREAD_POOL=OFF"
			" ..",
		"cd moonrayBuild && cmake --build . --config Release --target install -- {jobs}",

	],

	"manifest" : [

		"include/log4cplus",
		"lib/liblog4cplus*",

	],

}
