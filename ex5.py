# -*- coding: utf-8 -*-
name = 'myself'
age = 30 # not a lie
height = 69 # inches
heightMetric = height * 2.54
weight = 186 #lbs
weightMetric = weight / 2.2
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
number = 6

print "Let's talk about %s." % name
print "He likes the number %c." % number
print "He's %d inches tall." % height
print "That's %d centimeters." % heightMetric
print "He's %d pounds heavy." % weight
print "That's about %f kg." % weightMetric
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)


# Conversion	Meaning	Notes
# d	Signed integer decimal.
# i	Signed integer decimal.
# o	Unsigned octal.	(1)
# u	Unsigned decimal.
# x	Unsigned hexadecimal (lowercase).	(2)
# X	Unsigned hexadecimal (uppercase).	(2)
# e	Floating point exponential format (lowercase).
# E	Floating point exponential format (uppercase).
# f	Floating point decimal format.
# F	Floating point decimal format.
# g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
# G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
# c	Single character (accepts integer or single character string).
# r	String (converts any python object using repr()).	(3)
# s	String (converts any python object using str()).	(4)
# %	No argument is converted, results in a "%" character in the result.
#
# (1)
# The alternate form causes a leading zero ("0") to be inserted between left-hand padding and the formatting of the number if the leading character of the result is not already a zero.
# (2)
# The alternate form causes a leading '0x' or '0X' (depending on whether the "x" or "X" format was used) to be inserted between left-hand padding and the formatting of the number if the leading character of the result is not already a zero.
# (3)
# The %r conversion was added in Python 2.0.
# (4)
# If the object or format provided is a unicode string, the resulting string will also be unicode.
# Since Python strings have an explicit length, %s conversions do not assume that '\0' is the end of the string.
#
# For safety reasons, floating point precisions are clipped to 50; %f conversions for numbers whose absolute value is over 1e25 are replaced by %g conversions.2.9 All other errors raise exceptions.
#
# Additional string operations are defined in standard modules string and re.
