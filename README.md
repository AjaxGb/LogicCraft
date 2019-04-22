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
run `/function logiccraft:clear_screen` to setup the screen and
`/function logiccraft:give_me_symbols` to get all the symbols you
need.

## Usage

TODO

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
