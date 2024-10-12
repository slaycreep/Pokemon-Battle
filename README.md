# Pokemon-Battle
Imagine on one morning you woke up in the world of Pokémon as Ash Ketchum. Professor Oak then asked you to choose one from the following 6 starter Pokémon. After you chose your Pokémon, your arch nemesis Gary Oak chose one from the remaining Pokémon.

Now Gary being the bully that he is, challenges you to a battle. However, you are a CSE student in real life and therefore, decided to design a Pokémon battle simulator to determine your winning chances.

- Charmander and Cyndaquil are fire type, Squirtle and Totodile are water type, and Bulbasaur and Chikorita are grass type.
- Fire types are strong against grass type and do double damage, water types are strong against fire type and do double damage, and grass types are strong against water types and do double damage. In these cases, type affinity = 2
- Fire types are weak against water type and do half damage, water types are weak against grass types and do half damage, grass types are weak against fire types and do half damage. In these cases, type affinity = 0.5
- For same types (fire-fire/water-water/grass-grass), type affinity = 1
- Assume all 6 Pokémon have 50 hp and 20 attack power.
- The battle goes on until one of the Pokémon’s hp goes down to zero (or negative). Equation used to calculate remaining hp after each turn: Remaining hp = previous hp – attack power * type affinity
- When the battle is over, declare who is the winner.
- 
Your task is to create a Pokémon battle simulator that determines who wins between you and your rival.

```
Sample Input #1
You Choose: Charmander
Gary Chooses: Totodile
Output:
=== Turn 1 ===
Charmander has 10 hp left
Totodile has 40 hp left
=== Turn 2 ===
Charmander has 0 hp left
Totodile has 30 hp left
Totodile and Gary wins!


Sample Input #2
You Choose: Squirtle
Gary Chooses: Cyndaquil
Output:
=== Turn 1 ===
Squirtle has 40 hp left
Cyndaquil has 10 hp left
=== Turn 2 ===
Squirtle has 30 hp left
Cyndaquil has 0 hp left
Squirtle and Ash wins!


Sample Input #3
You Choose: Chikorita
Gary Chooses: Bulbasaur
Output:
=== Turn 1 ===
Chikorita has 30 hp left
Bulbasaur has 30 hp left
=== Turn 2 ===
Chikorita has 10 hp left
Bulbasaur has 10 hp left
=== Turn 3 ===
Chikorita has 0 hp left
Bulbasaur has 0 hp left
It’s a tie!

```
