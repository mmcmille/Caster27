'''
Michael McMillen
search
to do
filter dictation, press escape
'''


from dragonfly import Repeat, Pause, Function, Choice, MappingRule, ShortIntegerRef
from castervoice.lib.actions import Key, Text
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R

from castervoice.lib import github_automation
from castervoice.lib.temporary import Store, Retrieve

class FreeplaneRule(MappingRule):#free plane
	mapping = {
		#generic key rule
		"<key_rule>": R(Key("%(key_rule)s/40")),
		#menu control
		"<menu_title> menu": R(Key("a-%(menu_title)s")),
		#zoom
		"zoom out [<m>]": R(Key("a-down")) * Repeat(extra='m'),
		"zoom in [<m>]": R(Key("a-up")) * Repeat(extra='m'),
		#movement
		"move <direction> [<m>]": R(Key("c-%(direction)s")) * Repeat(extra='m'),

		#"drop text": R(Key("cs-v/20, a-p, enter")),
	}
	extras = [
		ShortIntegerRef("m", 1, 10),
		Choice("menu_title", {
			"file": "f",
			"edit": "e",
			"insert": "r",
			"view": "v",
			"format": "o",
			"navigate": "n",
			"filter": "i",
			"tools": "t",
			"maps": "m",
			"help": "h",
		}),
		Choice("direction", {
			"up": "up",
			"down": "down",
			"left": "left",
			"right": "right",
		}),
		Choice("key_rule", {

			"okay":"a-o",
			# "cancel":"a-c", # esc will also cancel
			# menu items
			"preferences": "c-comma",
			"save all": "a-f, a",#"a-s",
			"(copy|get) branch": "cs-c",
			"(copy|get) [node] ID": "a-e,c,c",# "cs-i",
			"get (link|address)": "a-e,c,o",
			# navigation
			"last": "a-left",
			"next": "a-right",
			"(jump in|isolate)":"s-escape",
			"jump out":"a-n,m",

			"next":"enter,enter",

			"fold [it]": "right",
			"(fold|collapse) all": "a-home",
			"unfold all": "a-end",
			"outline view": "a-v,v,o", #"cs-o",
			"edit styles": "c-f11",

			# filter
			"search": "cs-j",
			"filter": "c-f",
			"clear filter": "a-i,n",#"ca-f",

			#split
			"split here": "a-s",

			"split dot": "ca-dot",
			"split comma": "ca-comma",

			#edit
			"edit": "end",
			"edit dialogue": "a-enter",
			"edit note":"a-e,n,e",
			"title it":"ca-c",
			"(capitalize| cap) this":"ca-up",
			"(all caps|title) this":"ca-c",

			#nodes
			"(insert|big bro)": "s-enter",
			"(child|kid)": "tab",
			"(paste|drop) clone": "c-d",
			"summary node": "a-r,n,w",

			#links
			"open link": "c-enter",
			"edit link": "c-k",
			"get link": "a-e/20, c, c",

			#view
			"center ( view | node )": "ca-c",
			"new (window|view)": "a-v,e",#"ca-v",
			"tool panel":"a-v,c,o",

			#icons
			"info icon ": "ca-i",
			"school":"",
			"remove (icon | icons )": "a-r,o,r,e", #"cs-d",
			"project icon": "a-r,o,i,o,l",
			"task icon": "a-r,o,i,s,m",
			"unchecked": "a-r,o,i,s,u",# "c-1",
			"checked": "a-r,o,i,s,c",#"c-2",

		}),
	]
	defaults = {
		"m":1,
	}

def get_rule():
	return FreeplaneRule, RuleDetails(name="freeplane", executable="javaw")
