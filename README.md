# LogicCraft

LogicCraft is a Fitch-like logical proof checker, written in
Minecraft commands using the Trident command preprocessor.

[Trident Language](https://github.com/Energyxxer/Trident-Language/releases)  
[Trident IDE](https://github.com/Energyxxer/Trident-UI/releases)  
[Trident Discord](https://discord.gg/VpfA3c6)

## Setup

The source files can be compiled with Trident, which will produce
a data pack and a resource pack. These may be placed in a save
file. LogicCraft should work in most worlds, but works best in
superflat worlds that do not extend above Y=5.

Once you have added the datapack and resource pack to the world,
enter the console command `/function logiccraft:clear_screen` to
setup the screen and `/function logiccraft:give_me_symbols` to get
all the symbols you need.

## Usage

Right click with a symbol in the main writing plane to write that
symbol to the plane. Existing symbols will be overwritten. Left
click on a written symbol to delete it.

Right click on a line's header (the black bar at the far left) with
a symbol that has associated rules to set the line's justification
to the Intro rule for that symbol. For example, right click on a
line's header with the `AND` symbol to set the line's justification
to `AND Intro`. Right click again to toggle between Into and
Elimination.

Left click on a line header to select it. While a line is selected,
right click other line headers with the *letter* symbol to select
them as the line's premises. A line can have up to three premises,
which is all that will be needed for any of the provided rules.

Signs are provided in the starting area for verifying every line,
verifying the selected line, clearing the screen, or getting a
fresh set of symbols. Right click them to activate. Alternatively,
you can call the functions yourself:
```mcfunction
function logiccraft:verify/every_line
function logiccraft:verify/active_line
function logiccraft:clear_screen
function logiccraft:give_me_symbols
```

## Rules

Thus far, the following rules have been implemented:

### AND Intro
Cite: Two sentences of any kind.  
Produces: The conjunction of the two expressions.
### AND Elim
Cite: One conjunction.  
Produces: Either of the two conjuncts.
### NOT Elim
Cite: A negation of a negation.  
Produces: The sentence with the two negations removed.
### CONTRADICTION Intro
Cite: A sentence and its negation.  
Produces: A contradiction.
### CONTRADICTION Elim
Cite: A contradiction.  
Produces: Any sentence.
