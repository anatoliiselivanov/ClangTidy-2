set(CMAKE_CXX_CLANG_TIDY "clang-tidy; --extra-arg=-Wno-error=unknown-warning-option")

idf_component_register(SRCS "hello_world_main.c" "myFile.cpp"
                    INCLUDE_DIRS "")
