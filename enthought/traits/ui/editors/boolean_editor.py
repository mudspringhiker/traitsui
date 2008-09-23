#------------------------------------------------------------------------------
#
#  Copyright (c) 2008, Enthought, Inc.
#  All rights reserved.
#  
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#  
#  Author: David C. Morrill
#  Date:   10/21/2004
#
#------------------------------------------------------------------------------

""" Defines the Boolean editor factory for all traits toolkit backends.
"""

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from enthought.traits.api \
    import Dict, Str, Any

# CIRCULAR IMPORT FIXME: Importing from the source rather than traits.ui.api
# to avoid circular imports, as this EditorFactory will be part of 
# traits.ui.api as well. 
    
from enthought.traits.ui.view \
    import View
    
from text_editor \
    import ToolkitEditorFactory as EditorFactory
    
#-------------------------------------------------------------------------------
#  Trait definitions:
#-------------------------------------------------------------------------------

# Mapping from user input text to Boolean values
mapping_trait = Dict( Str, Any, { 'True':  True,
                                  'true':  True,
                                  't':     True,
                                  'yes':   True,
                                  'y':     True,
                                  'False': False,
                                  'false': False,
                                  'f':     False,
                                  'no':    False,
                                  'n':     False,
                    } )

#-------------------------------------------------------------------------------
#  'ToolkitEditorFactory' class:
#-------------------------------------------------------------------------------

class ToolkitEditorFactory ( EditorFactory ):
    """ Editor factory for Boolean editors.
    """
    #---------------------------------------------------------------------------
    #  Trait definitions:
    #---------------------------------------------------------------------------
    
    # Dictionary mapping user input to other values. 
    # These definitions override definitions in the 'text_editor' version
    mapping = mapping_trait  
    
    #---------------------------------------------------------------------------
    #  Traits view definition:  
    #---------------------------------------------------------------------------
    
    traits_view = View()    
    
# Define the BooleanEditor class
BooleanEditor = ToolkitEditorFactory

#- EOF -----------------------------------------------------------------------