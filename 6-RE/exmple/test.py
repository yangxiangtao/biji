2133 56
2.67
-4
3%5
-89.3
This module provides
 35.2% regular expression 
 matching operations similar to
  those found in Perl.

Both patterns and  201 strings
 1/3 to be searched can be Unicode strings 
 (str) as well as 8-bit strings (bytes). 
 However, Unicode strings and 8-bit strings 
 cannot be mixed: that is, you cannot match a Unicode 
string with a Line-1 byte pattern
 or vice-versa; similarly, when asking
  for a substitution, the replacement
   string must be of the same type as both 
   the pattern and the search string.

Regular 2018-1-16 expressions 45%
  use the 2.36 backslash character 
  ('\') to indicate special forms or
   to allow special characters to be used 
   without invoking their special meaning. 
   This collides with Python’s usage of the 
   same onLine character for the same purpose 
   in string literals; for example, to match 
   a literal backslash, one might have to write
    '\\\\' as the pattern string, because the 
    regular expression must be \\, and each backslash
     must be expressed as \\ inside a regular Python 
     string literal.

The solution is -12 to use Python’s

 raw string notation for regular 
 expression patterns; backslashes
  are not handled in any special 
  way in a string literal prefixed 
  with 'r'. So r"\n" is a two-character
   string containing '\' and 'n',
    while "\n" is a one-character 
    string containing a newline. 
    Usually patterns will be expressed
     in Python code using this raw string notation.

It is 2019-12-2 important to
 note -12.88 that most regular 
 expression operations are available
  as module-level functions and methods 
  on compiled regular expressions. 
  The functions are shortcuts that
   don’t require you to compile a 
   regex object first, but miss some 
   fine-tuning parameters.