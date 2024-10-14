# Starter-Code 

This repo contains starter code to implement projects without implementing everything from scratch

## Project Structure 

    - Project Folder 
        - src
            -main.cpp
        - CMakeLists.txt
        - ReadMe.MD
        - conanfile.py
        - .gitignore


## Tooling
- Compilers 
    1. Windows: Microsoft Visual Studio 2019 revision 16.7 Community Edition or newer.
    2. Linux (Ubuntu): GCC 10 or newer.
    3. macOS: Apple Clang 12.0 or newer (part of XCode 12 or newer).

- Build systems 
    1. ninja v1.8 or newer.
    2. CMake v3.18 or newer.

- Package manager 
    1. Python 3.7 or newer.
    2. conan v1.43 or newer.

# Setup 
    ``` 
    pip install conan
    sudo apt install cmake 
    
    ```

## Running
```
cd build 
conan install .. --build missing --output-folder=./dependencies
cmake .. -GNinja -DCMAKE_BUILD_TYPE=Release
ninja
cd ..
```


## Conventions 

## Contact
anallani94@gmail.com