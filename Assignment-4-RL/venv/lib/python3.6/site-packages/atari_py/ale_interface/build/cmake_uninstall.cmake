
IF(NOT EXISTS "/tmp/pip-req-build-8l8uecsn/build/lib.linux-x86_64-3.6/atari_py/ale_interface/build/install_manifest.txt")
  MESSAGE(FATAL_ERROR "Cannot find install manifest: /tmp/pip-req-build-8l8uecsn/build/lib.linux-x86_64-3.6/atari_py/ale_interface/build/install_manifest.txt")
ENDIF(NOT EXISTS "/tmp/pip-req-build-8l8uecsn/build/lib.linux-x86_64-3.6/atari_py/ale_interface/build/install_manifest.txt")

FILE(READ "/tmp/pip-req-build-8l8uecsn/build/lib.linux-x86_64-3.6/atari_py/ale_interface/build/install_manifest.txt" files)
STRING(REGEX REPLACE "\n" ";" files "${files}")
FOREACH(file ${files})
  MESSAGE(STATUS "Uninstalling "$ENV{DESTDIR}${file}"")
  IF(EXISTS "$ENV{DESTDIR}${file}")
    EXEC_PROGRAM(
      "/opt/_internal/cpython-3.6.7/lib/python3.6/site-packages/cmake/data/bin/cmake" ARGS "-E remove "$ENV{DESTDIR}${file}""
      OUTPUT_VARIABLE rm_out
      RETURN_VALUE rm_retval
      )
    IF(NOT "${rm_retval}" STREQUAL 0)
      MESSAGE(FATAL_ERROR "Problem when removing "$ENV{DESTDIR}${file}"")
    ENDIF(NOT "${rm_retval}" STREQUAL 0)
  ELSE(EXISTS "$ENV{DESTDIR}${file}")
    MESSAGE(STATUS "File "$ENV{DESTDIR}${file}" does not exist.")
  ENDIF(EXISTS "$ENV{DESTDIR}${file}")
ENDFOREACH(file)
