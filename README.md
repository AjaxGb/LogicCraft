# LogicCraft

LogicCraft is a Fitch-like logical proof checker, written in
Minecraft commands using the Trident command preprocessor.

[Trident Language](https://github.com/Energyxxer/Trident-Language/releases)  
[Trident IDE](https://github.com/Energyxxer/Trident-UI/releases)  
[Trident Development Discord](https://discord.gg/VpfA3c6)

## Setup

The source files can be compiled with Trident, which will produce
a data pack and a resource pack. These may be placed in a save
file. Alternatively, you can find the precompiled packs, and a world
with them preinstalled, on the [releases](https://github.com/AjaxGb/LogicCraft/releases)
page.
LogicCraft assumes:
* You are playing in Minecraft Java Edition 1.14 or later.
Snapshot versions should be fine.
* There is only one player in the world at a time, or at least
only one interacting with LogicCraft at a time.
* The player is in Creative. Not a *strict* requirement, but
without fly mode and infinite items it will be very difficult
to write on the screen.

Other than that, it should work in most worlds, but it works
best in worlds that do not have high, screen-blocking terrain.

Once you have added the datapack and resource pack to the world,
enter the console command `/function logiccraft:clear_screen` to
set up the screen and some clickable utility signs.

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

Subproofs are required for some of the Fitch rules. While the
existing code is designed to allow easy addition of subproofs, they
haven't actually been added yet.

## Rules

All rules that do not require subproofs have been implemented.

### AND Intro
Cite: Two sentences of any kind.  
Produces: The conjunction of the two expressions.
### AND Elim
Cite: A conjunction.  
Produces: Either of the two conjuncts.
### OR Intro
Cite: A sentence of any kind.  
Produces: The disjunction of that sentence with any sentence.
### ~~OR Elim~~
**Requires subproofs**  
Cite: A disjunction and a subproof for each side of the disjunction.
Each subproof should start with its respective side, and both should
have the same conclusion.  
Produces: The shared conclusion of both subproofs.
### ~~NOT Intro~~
**Requires subproofs**  
Cite: A subproof that concludes in a contradiction.  
Produces: The negation of the subproof's premise.
### NOT Elim
Cite: A negation of a negation.  
Produces: The sentence with the two negations removed.
### CONTRADICTION Intro
Cite: A sentence and its negation.  
Produces: A contradiction.
### CONTRADICTION Elim
Cite: A contradiction.  
Produces: Any sentence.
### ~~CONDITIONAL Intro~~
**Requires subproofs**  
Cite: A subproof of any kind.  
Produces: A conditional that connects the subproof's premise to its
conclusion.
### CONDITIONAL Elim
Cite: A conditional and a sentence that is the antecedent of that
conditional.  
Produces: The consequent of the conditional.
### ~~BICONDITIONAL Intro~~
**Requires subproofs**  
Cite: Two subproofs, where one's premise is the other's conclusion
and vice versa.  
Produces: A biconditional that connects the two sentences.
### BICONDITIONAL Elim
Cite: A biconditional and a sentence that appears on either side of
that biconditional.  
Produces: The other side of the biconditional.
