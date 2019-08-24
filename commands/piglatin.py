from commands.base import Command

class PigLatin(Command):
	desc = "This command is used to translate a given sentence into Pig Latin."

	def eval(self, *args):
		suffix = 'ay'
		res = []
		
		if args:
			# There are arguments and it's not PCSocBot conducting the command
			
			for arg in args:
			# Start for
			
				# I can't think of a single good name for this first variable ngl
				temp = 0
				addQuoteEnd = 0
				flag = (arg[0] != '@' and arg[0] != ':')
				
				# Navigates to the first non junk character, assuming printable and not part of the alphabet
				# However mentions and emotes should remain printable, so we don't wanna just catch every junk thing
				# Hence the flag
				while arg[temp].isprintable and (not arg[temp].isalpha) and flag:
					temp+=1
				
				# If we do get some junk, we wanna keep it at the start, such as quotation marks.
				if temp != 0:
					res.append(arg[0:temp])
				
				if arg[-1] == '\"' or arg[-2:] == "\" ":
					arg = arg[:-1]
					addQuoteEnd = 1
				
				# Start if/else
				if arg[temp].lower() in 'aeiou':
					# Starts with a vowel
					res.append(arg[temp:] + suffix)
				elif arg[temp].isalpha():
					# Consonant
					res.append(arg[(temp+1):] + arg[temp] + suffix)
				else:
					# Anything else (eg emotes, mentions)
					res.append(arg)
				# End if/else
				
				if addQuoteEnd:
					res.append("\" ")
				
			# End for
		# End if	
	return ' '.join(res) if res else None
# End function
