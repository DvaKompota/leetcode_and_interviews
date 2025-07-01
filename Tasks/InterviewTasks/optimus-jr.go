// # Optimus Jr Coding Challenge
// ## Background (fictional)
// Optimus Jr is a fictional, pre-prototype robot wandering the factory floor attempting to deliver its cargo. It has only basic sensors and basic abilities to move from its starting location to its destination. Your task, given an input map for each run, is to analyze and plan, if possible, the path that Optimus Jr will take to safely reach its destination. These run results will be key to the evolution of Optimus Jr.
// Read the following carefully in order to understand how to interpret the input maps and how to publish your output. We have provided a few sample inputs (maps) and expected outputs. Create additional maps as needed to fully test your logic. Your submission will be tested further against additional maps we have created.
// ---
// ## Rules
// 1. **Start:** Optimus Jr starts from the `@` symbol on the map and is always initially heading **SOUTH**.
// 2. **Finish:** Optimus Jr finishes its journey and delivers its cargo when it reaches the location marked `$`.
// 3. **Obstacles:**  
//    - `#` = unbreakable  
//    - `X` = breakable
// 4. **Obstacle Handling:**  
//    When Optimus Jr encounters an obstacle, regardless of its current direction, it changes direction using the following priorities:  
//    **SOUTH, EAST, NORTH, WEST** (in that order).  
//    If it cannot go SOUTH, it tries EAST, then NORTH, then WEST.
// 5. **Path Modifiers:**  
//    If Optimus Jr steps on a path modifier, it will cause Optimus Jr to change direction:  
//    - `S` → SOUTH  
//    - `E` → EAST  
//    - `N` → NORTH  
//    - `W` → WEST
// 6. **Circuit Inverters:**  
//    - `I` reverses the direction priorities to: **WEST, NORTH, EAST, SOUTH**.  
//    - The next inverter encountered will invert the priorities again, resetting to the original order, and so on.
// 7. **Breaker-mode:**  
//    - `B` toggles Breaker-mode on/off.  
//    - In Breaker-mode, Optimus Jr can destroy and immediately pass through breakable obstacles (`X`).  
//    - Destroyed obstacles remain destroyed.  
//    - Stepping on `B` again toggles Breaker-mode off.
// 8. **Teleporters:**  
//    - Digits `1` through `9` may be present.  
//    - Stepping on a teleporter instantly moves Optimus Jr to the matching teleporter (same digit), retaining direction and mode.  
//    - Teleporters always exist in pairs.
// 9. **No Traps:**  
//    Optimus Jr will never start in or be teleported into a single square totally enclosed with unbreakable walls.
// 10. **Blank Spaces:**  
//     Space characters are blank areas with no special effects.
// ---
// ## Input
// - The only input is text consumed from STDIN containing a 2-dimensional grid of characters (the map).
// - The edges of the map are always unbreakable `#` obstacles.
// - The map always has a starting point `@` and a destination `$`.
// - Digits, if present, always exist in pairs.
// - **Line 1:** Two integers, the height `H` and width `W` of the map, separated by a space.
// - **Next H lines:** Each line is a string of `W` characters representing a horizontal line of the map.
// **Possible characters:** `#`, `X`, `@`, `$`, `S`, `E`, `N`, `W`, `B`, `I`, `1`-`9`, and space.
// ---
// ## Output
// - Output the sequence of moves (`NORTH`, `SOUTH`, `EAST`, or `WEST`, one per line) taken by Optimus Jr as it travels from its starting point to the destination.
// - If Optimus Jr cannot reach its destination due to an indefinite loop, output only `LOOP`.
// ---
// ## Examples:
//
// ### Example 1
// Input:
// 5 6
// ###### 
// #@E $#
// # N  #
// #X   #
// ######
// Expected Output:
// SOUTH
// EAST
// NORTH
// EAST
// EAST
//
// ### Example 2
// Input:
// 10 10
// ##########
// #        #
// #  S  W  #
// #        #
// #  $     #
// #        #
// #@       #
// #        #
// #E     N #
// ##########
// Expected Output:
// SOUTH
// SOUTH
// EAST
// EAST
// EAST
// EAST
// EAST
// EAST
// NORTH
// NORTH
// NORTH
// NORTH
// NORTH
// NORTH
// WEST
// WEST
// WEST
// WEST
// SOUTH
// SOUTH
//
// ### Example 3
// Input:
// 10 10
// ##########
// # @      #
// # B      #
// #XXX     #
// # B      #
// #    BXX$#
// #XXXXXXXX#
// #        #
// #        #
// ##########
// Expected Output:
// SOUTH
// SOUTH
// SOUTH
// SOUTH
// EAST
// EAST
// EAST
// EAST
// EAST
// EAST
//
// ### Example 4
// Input:
// 10 10
// ##########
// #    I   #
// #        #
// #       $#
// #       @#
// #        #
// #       I#
// #        #
// #        #
// ##########
// Expected Output:
// SOUTH
// SOUTH
// SOUTH
// SOUTH
// WEST
// WEST
// WEST
// WEST
// WEST
// WEST
// WEST
// NORTH
// NORTH
// NORTH
// NORTH
// NORTH
// NORTH
// NORTH
// EAST
// EAST
// EAST
// EAST
// EAST
// EAST
// EAST
// SOUTH
// SOUTH
//
// ### Example 5
// Input:
// 10 10
// ##########
// #    1   #
// #        #
// #        #
// #        #
// #@       #
// #        #
// #        #
// #    1  $#
// ##########
// Expected Output:
// SOUTH
// SOUTH
// SOUTH
// EAST
// EAST
// EAST
// EAST
// EAST
// EAST
// EAST
// SOUTH
// SOUTH
// SOUTH
// SOUTH
// SOUTH
// SOUTH
// SOUTH
//
// ### Example 6
// Input:
// 5 5
// #####
// #   #
// # $ #
// # @ #
// #####
// Expected Output:
// LOOP

package main
