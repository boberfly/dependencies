{

	"downloads" : [

		"https://www.lua.org/ftp/lua-5.4.7.tar.gz"

	],

	"url" : "https://www.lua.org/",

	"license" : "LICENSE",

	"dependencies" : [],

	"commands" : [

		"mkdir moonrayBuild",
		"cd moonrayBuild &&"
			" cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D LUA_ENABLE_TESTING=OFF"
			" -D LUA_ENABLE_SHARED=OFF"
			" -D LUA_BUILD_BINARY=ON"
			" -D LUA_BUILD_COMPILER=ON"
			" ..",
		"cd moonrayBuild && cmake --build . --config Release --target install -- {jobs}",

	],

	"manifest" : [

		"bin/lua*",
		"include/lua*",
		"include/lauxlib.h"
		"lib/*lua*",

	],

}
