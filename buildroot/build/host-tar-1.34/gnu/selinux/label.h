/* DO NOT EDIT! GENERATED AUTOMATICALLY! */
/* Replacement <selinux/label.h> for platforms that lack it.
   Copyright 2020-2021 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* Written by Paul Eggert.  */

#ifndef SELINUX_LABEL_H

#define SELINUX_LABEL_H

#include <selinux/selinux.h>
#include <errno.h>

#ifndef _GL_INLINE_HEADER_BEGIN
 #error "Please include config.h first."
#endif
_GL_INLINE_HEADER_BEGIN
#ifndef SE_LABEL_INLINE
# define SE_LABEL_INLINE _GL_INLINE
#endif

/* The definition of _GL_UNUSED_PARAMETER is copied here.  */
/* A C macro for declaring that specific function parameters are not used.
   Copyright (C) 2008-2021 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify it
   under the terms of the GNU General Public License as published
   by the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* _GL_UNUSED_PARAMETER is a marker that can be appended to function parameter
   declarations for parameters that are not used.  This helps to reduce
   warnings, such as from GCC -Wunused-parameter.  The syntax is as follows:
       type param _GL_UNUSED_PARAMETER
   or more generally
       param_decl _GL_UNUSED_PARAMETER
   For example:
       int param _GL_UNUSED_PARAMETER
       int *(*param)(void) _GL_UNUSED_PARAMETER
   Other possible, but obscure and discouraged syntaxes:
       int _GL_UNUSED_PARAMETER *(*param)(void)
       _GL_UNUSED_PARAMETER int *(*param)(void)
 */
#ifndef _GL_UNUSED_PARAMETER
# define _GL_UNUSED_PARAMETER _GL_ATTRIBUTE_MAYBE_UNUSED
#endif

#define SELABEL_CTX_FILE 0

struct selabel_handle;

SE_LABEL_INLINE int
selabel_lookup (struct selabel_handle *hnd _GL_UNUSED_PARAMETER,
                char **context _GL_UNUSED_PARAMETER,
                char const *key _GL_UNUSED_PARAMETER,
                int type _GL_UNUSED_PARAMETER)
{ errno = ENOTSUP; return -1; }

SE_LABEL_INLINE struct selabel_handle *
selabel_open (int backend _GL_UNUSED_PARAMETER,
              struct selinux_opt *options _GL_UNUSED_PARAMETER,
              unsigned nopt _GL_UNUSED_PARAMETER)
{ errno = ENOTSUP; return 0; }

SE_LABEL_INLINE void
selabel_close (struct selabel_handle *hnd _GL_UNUSED_PARAMETER)
{ errno = ENOTSUP; }

_GL_INLINE_HEADER_END

#endif
