// This file is included by all compilation units, including those in
// src/third_party. It should only contain macros and typedefs.

#pragma once
#ifdef __clang__
#  pragma clang diagnostic push
#  if __has_warning("-Wreserved-id-macro")
#    pragma clang diagnostic ignored "-Wreserved-id-macro"
#  endif
#endif

#ifdef __MINGW32__
#  define __USE_MINGW_ANSI_STDIO 1
#  define __STDC_FORMAT_MACROS 1
#endif

// For example for vasprintf under i686-w64-mingw32-g++-posix. The later
// definition of _XOPEN_SOURCE disables certain features on Linux, so we need
// _GNU_SOURCE to re-enable them (makedev, tm_zone).
#define _GNU_SOURCE 1

// The later definition of _XOPEN_SOURCE and _POSIX_C_SOURCE disables certain
// features on NetBSD, so we need _NETBSD_SOURCE to re-enable them.
#define _NETBSD_SOURCE 1

// The later definition of _XOPEN_SOURCE and _POSIX_C_SOURCE disables certain
// features on FreeBSD, so we need __BSD_VISIBLE to re-enable them.
#define __BSD_VISIBLE 1

// The later definition of _XOPEN_SOURCE and _POSIX_C_SOURCE disables u_int on
// Irix 5.3. Defining _BSD_TYPES brings it back.
#define _BSD_TYPES 1

// The later definition of _XOPEN_SOURCE and _POSIX_C_SOURCE disables certain
// features on Mac OS X, so we need _DARWIN_C_SOURCE to re-enable them.
/* #undef _DARWIN_C_SOURCE */

// Define to activate features from IEEE Stds 1003.1-2008.
#define _POSIX_C_SOURCE 200809L

#if defined(__SunOS_5_8) || defined(__SunOS_5_9) || defined(__SunOS_5_10)
#  define _XOPEN_SOURCE 500
#elif defined(__FreeBSD__)
#  define _XOPEN_SOURCE 700
#elif defined(__ibmxl__) && defined(__clang__) // Compiler xlclang
#  define _XOPEN_SOURCE 600
#  define _ALL_SOURCE 1
#elif !defined(__SunOS_5_11) && !defined(__APPLE__)
#  define _XOPEN_SOURCE
#endif

#if defined(__SunOS_5_10) || defined(__SunOS_5_11)
#  define __EXTENSIONS__ 1
#else
#  define _XOPEN_SOURCE_EXTENDED
#endif

// Handle large files when compiled in 32-bit mode.
#ifndef _FILE_OFFSET_BITS
#  define _FILE_OFFSET_BITS 64
#endif

// clang-format off
/* #undef _WIN32_WINNT */
// clang-format on

#ifdef __clang__
#  pragma clang diagnostic pop
#endif

/* #undef MTR_ENABLED */

// Define if you have the "asctime_r" function.
#define HAVE_ASCTIME_R

// Define if your compiler supports AVX2.
#define HAVE_AVX2

// Define if you have the "getopt_long" function.
#define HAVE_GETOPT_LONG

// Define if you have the "getpwuid" function.
#define HAVE_GETPWUID

// Define if you have the <linux/fs.h> header file.
#define HAVE_LINUX_FS_H

// Define if the system has the type "long long".
/* #undef HAVE_LONG_LONG */

// Define if you have the "posix_fallocate.
#define HAVE_POSIX_FALLOCATE

// Define if you have the <pwd.h> header file.
#define HAVE_PWD_H

// Define if you have the "realpath"" function.
#define HAVE_REALPATH

// Define if you have the "setenv" function.
#define HAVE_SETENV

// Define if you have the "strndup" function.
#define HAVE_STRNDUP

// Define if "f_fstypename" is a member of "struct statfs".
/* #undef HAVE_STRUCT_STATFS_F_FSTYPENAME */

// Define if "st_atim" is a member of "struct stat".
#define HAVE_STRUCT_STAT_ST_ATIM

// Define if "st_ctim" is a member of "struct stat".
#define HAVE_STRUCT_STAT_ST_CTIM

// Define if "st_mtim" is a member of "struct stat".
#define HAVE_STRUCT_STAT_ST_MTIM

// Define if "st_atimespec" is a member of "struct stat".
/* #undef HAVE_STRUCT_STAT_ST_ATIMESPEC */

// Define if "st_ctimespec" is a member of "struct stat".
/* #undef HAVE_STRUCT_STAT_ST_CTIMESPEC */

// Define if "st_mtimespec" is a member of "struct stat".
/* #undef HAVE_STRUCT_STAT_ST_MTIMESPEC */

// Define if you have the "syslog" function.
#define HAVE_SYSLOG

// Define if you have the <syslog.h> header file.
#define HAVE_SYSLOG_H

// Define if you have the <sys/clonefile.h> header file.
/* #undef HAVE_SYS_CLONEFILE_H */

// Define if you have the <sys/ioctl.h> header file.
#define HAVE_SYS_IOCTL_H

// Define if you have the <sys/mman.h> header file.
#define HAVE_SYS_MMAN_H

// Define if you have the <sys/time.h> header file.
#define HAVE_SYS_TIME_H

// Define if you have <sys/wait.h> that is POSIX.1 compatible.
#define HAVE_SYS_WAIT_H

// Define if you have the <sys/file.h> header file.
#define HAVE_SYS_FILE_H

// Define if you have the <termios.h> header file.
#define HAVE_TERMIOS_H

// Define if you have the <dirent.h> header file.
#define HAVE_DIRENT_H

// Define if you have the <strings.h> header file.
#define HAVE_STRINGS_H

// Define if you have the <unistd.h> header file.
#define HAVE_UNISTD_H

// Define if you have the <utime.h> header file.
#define HAVE_UTIME_H

// Define if you have the <sys/utime.h> header file.
/* #undef HAVE_SYS_UTIME_H */

// Define if you have the <varargs.h> header file.
/* #undef HAVE_VARARGS_H */

// Define if you have the "unsetenv" function.
#define HAVE_UNSETENV

// Define if you have the "utimensat" function.
#define HAVE_UTIMENSAT

// Define if you have the "utimes" function.
#define HAVE_UTIMES

#if defined(__ibmxl__) && defined(__clang__) // Compiler xlclang
#  undef HAVE_VARARGS_H // varargs.h would hide macros of stdarg.h
#  undef HAVE_STRUCT_STAT_ST_CTIM
#  undef HAVE_STRUCT_STAT_ST_MTIM
#endif

// Typedefs that make it possible to use common types in ccache header files
// without including core/wincompat.hpp.
#ifdef _WIN32
#  ifdef _MSC_VER
typedef unsigned __int32 mode_t;
typedef int pid_t;
#  endif // _MSC_VER
#endif   // _WIN32

// O_BINARY is needed when reading binary data on Windows, so use it everywhere
// with a compatibility define for Unix platforms.
#if !defined(_WIN32) && !defined(O_BINARY)
#  define O_BINARY 0
#endif
#if !defined(_WIN32) && !defined(O_TEXT)
#  define O_TEXT 0
#endif

#ifndef ESTALE
#  define ESTALE -1
#endif

#define SYSCONFDIR "/home/huzi/Documents/houdini/buildroot/host/etc"

#define INODE_CACHE_SUPPORTED

// Buffer size for I/O operations. Should be a multiple of 4 KiB.
#define CCACHE_READ_BUFFER_SIZE 65536
