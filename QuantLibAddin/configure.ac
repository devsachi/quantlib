
# Process this file with autoconf to produce a configure script.

AC_INIT([QuantLibAddin], [1.5.0],
        [quantlib-dev@lists.sourceforge.net],
        [QuantLibAddin])
AC_PREREQ(2.50)
AC_CONFIG_SRCDIR([qlo/qladdindefines.hpp])
AC_CONFIG_AUX_DIR([config])
AC_CONFIG_HEADERS([qlo/config.hpp])
AM_INIT_AUTOMAKE([foreign])

AC_COPYRIGHT([
Copyright (C) 2004, 2005, 2006, 2007, 2008 Eric Ehlers
Copyright (C) 2004, 2005, 2006, 2007 Ferdinando Ametrano

Copyright (C) 2004, 2006 StatPro Italia srl
Copyright (C) 2005, 2006 Aurelien Chanudet
Copyright (C) 2005, 2006 Plamen Neykov
Copyright (C) 2005 Walter Penschke
Copyright (C) 2006, 2007 Chiara Fornarola
Copyright (C) 2006, 2007 Cristina Duminuco
Copyright (C) 2006, 2007 Francois du Vignaud
Copyright (C) 2006, 2007 Giorgio Facchinetti
Copyright (C) 2006, 2007 Katiuscia Manzoni
Copyright (C) 2006, 2007 Marco Bianchetti
Copyright (C) 2006 Mario Pucci
Copyright (C) 2006 Silvia Frasson
Copyright (C) 2007 Luigi Ballabio

This file is part of QuantLib, a free-software/open-source library
for financial quantitative analysts and developers - http://quantlib.org/

QuantLib is free software: you can redistribute it and/or modify it under the
terms of the QuantLib license.  You should have received a copy of the
license along with this program; if not, please email
<quantlib-dev@lists.sf.net>. The license is also available online at
<http://quantlib.org/license.shtml>.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the license for more details.])

AC_PROG_INSTALL

# Default compilation variables

AC_SUBST([CXXFLAGS],[${CXXFLAGS='-g -O2 -Wall'}])

# Continue setup

AC_PROG_CC
AC_PROG_CXX
AC_PROG_CPP
AC_PROG_LIBTOOL
AC_LANG([C++])

# Check for tools needed for building documentation

AC_PATH_PROG([DOXYGEN], [doxygen])
AC_PATH_PROG([SED], [sed])

# Possibly enable features

AC_ARG_ENABLE([addin-cpp],
              AC_HELP_STRING([--enable-addin-cpp],
                             [build C++ addin and clients [[default=no]]]),
                             [qla_build_cpp=$enableval],
                             [qla_build_cpp=omitted])
#AC_ARG_ENABLE([addin-calc],
#              AC_HELP_STRING([--enable-addin-calc],
#                             [build Calc addin [[default=no]]]),
#                             [qla_build_calc=$enableval],
#                             [qla_build_calc=omitted])
#AC_ARG_ENABLE([addin-c],
#              AC_HELP_STRING([--enable-addin-c],
#                             [build C addin and clients [[default=no]]]),
#                             [qla_build_c=$enableval],
#                             [qla_build_c=omitted])
#AC_ARG_ENABLE([addin-guile],
#              AC_HELP_STRING([--enable-addin-guile],
#                             [build Guile addin [[default=no]]]),
#                             [qla_build_guile=$enableval],
#                             [qla_build_guile=omitted])
AC_ARG_ENABLE([addin-excel],
              AC_HELP_STRING([--enable-addin-excel],
                             [generate source for Excel addin [[default=no]]]),
                             [qla_build_excel=$enableval],
                             [qla_build_excel=omitted])
AC_ARG_ENABLE([addin-all],
              AC_HELP_STRING([--enable-addin-all],
                             [build all addins and clients [[default=no]]]),
                             [qla_build_all=$enableval])
AM_CONDITIONAL(BUILD_CPP, [test "$qla_build_cpp" = "omitted" \
    && test "$qla_build_all" = "yes" || test "$qla_build_cpp" = "yes"])
AM_CONDITIONAL(BUILD_CALC, [test "$qla_build_calc" = "omitted" \
    && test "$qla_build_all" = "yes" || test "$qla_build_calc" = "yes"])
#AM_CONDITIONAL(BUILD_C, [test "$qla_build_c" = "omitted" \
#    && test "$qla_build_all" = "yes" || test "$qla_build_c" = "yes"])
#AM_CONDITIONAL(BUILD_GUILE, [test "$qla_build_guile" = "omitted" \
#    && test "$qla_build_all" = "yes" || test "$qla_build_guile" = "yes"])
AM_CONDITIONAL(BUILD_EXCEL, [test "$qla_build_excel" = "omitted" \
    && test "$qla_build_all" = "yes" || test "$qla_build_excel" = "yes"])

# Configure and validate the path to gensrc

AC_ARG_WITH([gensrc],
            AC_HELP_STRING([--with-gensrc=/path/to/gensrc],
                           [Specify the path to gensrc]),
            [gensrc_path=${withval}],
            [AC_MSG_ERROR([You must specify the location of gensrc: "./configure --with-gensrc=path/to/gensrc"])])
AC_CHECK_FILE([${gensrc_path}/gensrc.py], [],
            [AC_MSG_ERROR([Unable to locate script gensrc.py in specified gensrc directory])])
AC_ARG_VAR(gensrc_dir, path to gensrc)
AC_SUBST(gensrc_dir, [${gensrc_path}])

# Configure and validate the path to ObjectHandler

AC_ARG_WITH([oh],
            AC_HELP_STRING([--with-oh=/path/to/ObjectHandler],
                           [Specify the root directory of the ObjectHandler source tree]),
            [oh_path=${withval}],
            [AC_MSG_ERROR([You must specify the location of ObjectHandler: "./configure --with-oh=path/to/ObjectHandler"])])
AC_CHECK_FILE([${oh_path}/oh/objecthandler.hpp], [],
            [AC_MSG_ERROR([Unable to locate file oh/objecthandler.hpp in specified ObjectHandler directory])])
AC_ARG_VAR(oh_dir, path to ObjectHandler)
AC_SUBST(oh_dir, [${oh_path}])

# Done, output the configured files

AC_CONFIG_FILES([
    Addins/Cpp/Makefile
    Addins/Calc/Makefile
    Clients/Cpp/Makefile
    Clients/CppInstrumentIn/Makefile
    Clients/CppSwapOut/Makefile
    Clients/Calc/Makefile
    Docs/Makefile
    gensrc/Makefile
    Makefile
    qlo/conversions/Makefile
    qlo/enumerations/constructors/Makefile
    qlo/enumerations/factories/Makefile
    qlo/enumerations/register/Makefile
    qlo/indexes/Makefile
    qlo/indexes/ibor/Makefile
    qlo/indexes/swap/Makefile
    qlo/loop/Makefile
    qlo/serialization/create/Makefile
    qlo/serialization/register/Makefile
    qlo/serialization/Makefile
    qlo/valueobjects/Makefile
    qlo/Makefile])

AC_OUTPUT

