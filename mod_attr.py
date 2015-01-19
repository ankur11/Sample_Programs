#!/usr/bin/env python

from __future__ import print_function

sep_chr = '-'
sep_len = 60

def get_attr_det(mod_name, verbose=True):
	if verbose:
		print(sep_chr*sep_len)
		print('Module Name -> '+ mod_name.__name__ +' ....... File name -> '+mod_name.__file__)
		print(sep_chr*sep_len)
	for attr in mod_name.__dict__:
		if attr.startswith('__'):
			print('<builtin-name> .... ',attr)#' -> ',getattr(mod_name, attr))
		else:
			print('Defined attribute(',attr,') => ',getattr(mod_name, attr))


if __name__ == '__main__':
	import mod_attr
	get_attr_det(mod_attr)
