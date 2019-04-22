individual_model = """{{
	"parent": "logiccraft:item/symbol",
	"textures": {{
		"layer0": "logiccraft:symbol/{name}"
	}}
}}"""

main_model_start = """{
	"parent": "item/template_spawn_egg",
	"overrides": ["""
main_model_mid = """
		{{
			"predicate": {{ "custom_model_data": {num} }},
			"model": "logiccraft:item/{name}"
		}}"""
main_model_end = """
	]
}"""

with open("minecraft/models/item/endermite_spawn_egg.json", "w") as main_file:
	
	print(main_model_start, end="", file=main_file)
	
	num = 1
	
	def make_model(name):
		global num
		
		with open(f"logiccraft/models/item/{name}.json", "w") as file:
			print(individual_model.format(name=name),
				end="", file=file)
		
		if num != 1:
			print(",", end="", file=main_file)
		
		print(main_model_mid.format(name=name, num=num),
			end="", file=main_file)
		
		num += 1
	
	for name in ["and", "or", "not",
			"condition", "bicondition", "contradiction",
			"open_parens", "close_parens",
			"subproof"]:
		make_model(name)
	
	for c in "abcdefghijklmnopqrstuvwxyz":
		make_model(f"letter_{c}")
	
	print(main_model_end, end="", file=main_file)
