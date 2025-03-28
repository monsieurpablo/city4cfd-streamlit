# Install script for directory: /root/github/City4CFD/thirdparty/LAStools/LASlib/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/LASlib" TYPE FILE FILES
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/arithmeticdecoder.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/arithmeticencoder.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/arithmeticmodel.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamin.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamin_array.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamin_file.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamin_istream.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreaminout.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreaminout_file.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamout.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamout_array.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamout_file.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamout_nil.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/bytestreamout_ostream.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/integercompressor.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasattributer.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasindex.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasinterval.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laspoint.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasquadtree.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasquantizer.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasreaditem.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasreaditemcompressed_v1.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasreaditemcompressed_v2.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasreaditemcompressed_v3.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasreaditemcompressed_v4.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasreaditemraw.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/lasreadpoint.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laswriteitem.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laswriteitemcompressed_v1.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laswriteitemcompressed_v2.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laswriteitemcompressed_v3.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laswriteitemcompressed_v4.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laswriteitemraw.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laswritepoint.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laszip.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laszip_common_v1.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laszip_common_v2.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laszip_common_v3.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/laszip_decompress_selective_v3.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../../LASzip/src/mydefs.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasdefinitions.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasfilter.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasignore.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laskdtree.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_asc.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_bil.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_bin.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_dtm.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_las.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_ply.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_qfit.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_shp.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreader_txt.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreaderbuffered.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreadermerged.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreaderpipeon.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasreaderstored.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lastransform.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasutility.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasvlr.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/lasvlrpayload.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswaveform13reader.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswaveform13writer.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswriter.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswriter_bin.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswriter_las.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswriter_qfit.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswriter_txt.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswriter_wrl.hpp"
    "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/../inc/laswritercompatible.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/LASlib" TYPE STATIC_LIBRARY FILES "/root/github/City4CFD/thirdparty/LAStools/LASlib/lib/libLASlib.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/LASlib/laslib-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/LASlib/laslib-targets.cmake"
         "/root/github/City4CFD/build/thirdparty/LAStools/LASlib/src/CMakeFiles/Export/c55326e5cb745217e14af8383b523273/laslib-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/LASlib/laslib-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/LASlib/laslib-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/LASlib" TYPE FILE FILES "/root/github/City4CFD/build/thirdparty/LAStools/LASlib/src/CMakeFiles/Export/c55326e5cb745217e14af8383b523273/laslib-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/LASlib" TYPE FILE FILES "/root/github/City4CFD/build/thirdparty/LAStools/LASlib/src/CMakeFiles/Export/c55326e5cb745217e14af8383b523273/laslib-targets-release.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/LASlib" TYPE FILE FILES "/root/github/City4CFD/thirdparty/LAStools/LASlib/src/laslib-config.cmake")
endif()

