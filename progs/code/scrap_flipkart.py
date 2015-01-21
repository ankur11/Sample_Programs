#!/usr/bin/env python
from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
import re

def readable_cat_tree(d, indent=0):
        for key, value in d.iteritems():
                print ('\t' * indent + str(key))
                if isinstance(value, dict):
                        readable_cat_tree(value, indent+1)


def crawl_url(url, run_headless=True):
	if run_headless:
		display = Display(visible=0, size=(1024, 768))
		display.start()
	browser = webdriver.Firefox()
	browser.get(url)
	level_0_menu = browser.find_elements_by_class_name("menu-l0")
	for menu_elm in level_0_menu:
		elm = menu_elm.find_element_by_tag_name("a").find_element_by_tag_name("span")
		cat_text = elm.text.lower()
		cat_text = re.sub(' & |\s','-',cat_text)
		hover = ActionChains(browser).move_to_element(elm)
		hover.perform()
		scrapped_categories['HOME'][elm.text] = {}
		l_1_cat = scrapped_categories['HOME'][elm.text]
		for a in browser.find_elements_by_id('menu-'+cat_text+'-tab-0-content'):
			ul = a.find_elements_by_tag_name('ul')
			for ul_elm in ul:
				for li_elm in ul_elm.find_elements_by_tag_name('li'):
					class_li_elm = li_elm.get_attribute('class')
					if class_li_elm == 'heading':
						l_1_cat[li_elm.find_element_by_tag_name("a").text] = {}
						obj = l_1_cat[li_elm.find_element_by_tag_name("a").text]
					elif class_li_elm == 'unclickable-heading':
						l_1_cat[li_elm.find_element_by_tag_name("span").text] = {}
                                                obj = l_1_cat[li_elm.find_element_by_tag_name("span").text]
					else:
						obj[li_elm.find_element_by_tag_name("a").text] = None
	browser.quit()


if __name__=='__main__':
	url = "http://www.flipkart.com"
	scrapped_categories = {'HOME':{}}
	crawl_url(url)
	readable_cat_tree(scrapped_categories)


