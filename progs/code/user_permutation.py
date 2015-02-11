#!/usr/bin/env python
import math

def gen_perm(s):
	l_s = len(s)
	lim = math.factorial(l_s)
	counter = 0
	i = 0
	j = 0
	b = []
	while len(b) < lim:
		a = s[:]
		i = int(counter / l_s)
		counter += 1
		if j > l_s-1:
			j = 0
		try:
			a[i], a[j] = a[j], a[i]
		except : pass
		j += 1
		if a not in b:
			b.append(a)
			yield a


if __name__ == '__main__':
	s = [1,2,3,4]
	for k in gen_perm(s):
		print k
























































#
#
#     /~\                        
#                 And don't let me catch      |oo )                       
#                    you following me         _\=/_                       
#                    begging for help.    #  /  _  \                      
#                                         \\//|/.\|\\                     
#                                          \/  \_/  ||                    
#                                             |\ /| ||                    
#                                             \_ _/  #                    
#                                             | | |                       
#                                             | | |                       
#                                             []|[]                       
#                                             | | |                       
#       \____________________________________/_]_[_\_
#
#
#     ====                                                 
#                   ~~o o               ...but I'll remind him.           
#                   _\ -/_                                                
#                  /  \ / \                                               
#                 //|  | |\\                                              
#                 \\|  | | \\                                             
#                  \\  | |  \\                                            
#                   )====|   ')                                           
#                   | || |                                                
#                   (_)(_)          ___                                   
#                   |_||_|         /   |                                  
#                   |_||_|        /    |                                  
#      _____________[_][__\___
#
#
#
#
#
#
#
#
#                                             ====                        
#                                             o o~~     ...you've got     
#                                            _\- /_    something  jammed  
#                                ___        / \ /  \   in here real good. 
#                               /() \      //| |  |\\                     
#                             _|_____|_   // | |  |//                     
#                            | | === | | //  | |  //                      
#                            |_|  O  |_|('   |===(|                       
#                             ||  O  ||      | || |                       
#                             ||__*__||      (_)(_)                       
#               -------      |~ \___/ ~|     |_||_|                       
#               |     |      /=\ /=\ /=\     |_||_|                       
#      _________|_____|______[_]_[_]_[_]____/__][__\______________________^[[B
#^[[B^[[C^[[A^[[D
#'
#
#
#
#:-)
#
#
#
#                    /~\                                ====              
#                   ( oo|                               o o~~             
#                   _\=/_                              _\- /_             
#                  /  _  \                 ___        / \ /  \            
#                 //|/.\|\\               / ()\      //| |  |\\           
#                ||  \_/  ||            _|_____|_    \\| |  |//           
#                || |\ /| ||           | | === | |    \\ |  //            
#                 # \_ _/ #            |_|  O  |_|     )===(|             
#                   | | |               ||  O  ||      | || |             
#                   | | |               ||__*__||      (_)(_)             
#                   []|[]              |~ \___/ ~|     |_||_|             
#                   | | |              /=\ /=\ /=\     |_||_|             
#      ____________/_]_[_\_____________[_]_[_]_[_]____/__][__\_
#


