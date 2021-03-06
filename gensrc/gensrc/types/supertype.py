
"""
 Copyright (C) 2007, 2008 Eric Ehlers

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it
 under the terms of the QuantLib license.  You should have received a
 copy of the license along with this program; if not, please email
 <quantlib-dev@lists.sf.net>. The license is also available online at
 <http://quantlib.org/license.shtml>.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
"""

"""Properties that may be shared by multiple DataType objects."""

from gensrc.utilities import common
from gensrc.serialization import serializable

class SuperType(serializable.Serializable):
    """Properties that may be shared by multiple DataType objects."""

    #############################################
    # class variables
    #############################################

    groupName_ = 'SuperTypes'

    #############################################
    # public interface
    #############################################

    def nativeType(self):
        """Return the native datatype associated with this supertype."""
        return self.nativeType_

    def conversionSuffix(self):
        """Return the conversion suffix defined for this supertype.

        The conversion suffix is some text to be appended to variable
        names in autogenerated source code after data conversion."""
        return self.conversionSuffix_

    def memberAccess(self):
        """Return the member access text defined for this supertype.

        The member access text is the symbol used to access members
        of variables of the given type e.g. '.' or '->'."""
        return self.memberAccess_

    def objectReference(self):
        """Return a boolean indicating whether variables of the associated
        type represent references to objects."""
        return self.objectReference_

    #############################################
    # serializer interface
    #############################################

    def serialize(self, serializer):
        """Load/unload class state to/from serializer object."""
        serializer.serializeAttribute(self, common.NAME)
        serializer.serializeAttribute(self, common.NATIVE_TYPE)
        serializer.serializeAttribute(self, common.CONVERSION_SUFFIX, '')
        serializer.serializeAttribute(self, common.MEMBER_ACCESS, '->')
        serializer.serializeAttributeBoolean(self, common.OBJECT_REFERENCE, True)

class SuperTypeDict(serializable.Serializable):
    """Wrapper for a dictionary of SuperType objects."""

    #############################################
    # public interface
    #############################################

    def superTypes(self):
        """Return the dictionary of SuperType objects."""
        return self.superTypes_

    #############################################
    # serializer interface
    #############################################

    def serialize(self, serializer):
        """Load/unload class state to/from serializer object."""
        serializer.serializeObjectDict(self, SuperType)

