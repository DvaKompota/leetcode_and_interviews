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
// #  S   W #
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

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Tile string

const (
	TileWall      Tile = "#"
	TileBreakable Tile = "X"
	TileStart     Tile = "@"
	TileGoal      Tile = "$"
	TileSouth     Tile = "S"
	TileEast      Tile = "E"
	TileNorth     Tile = "N"
	TileWest      Tile = "W"
	TileBreaker   Tile = "B"
	TileInverter  Tile = "I"
	TileEmpty     Tile = " "
	// Teleporters: "1"..."9" can be handled as needed
)

type Direction string

const (
	South Direction = "S"
	East  Direction = "E"
	North Direction = "N"
	West  Direction = "W"
)

var dirToString = map[Direction]string{
	South: "SOUTH",
	East:  "EAST",
	North: "NORTH",
	West:  "WEST",
}

var normalPriority = []Direction{South, East, North, West}
var invertedPriority = []Direction{West, North, East, South}

type State struct {
	X, Y     int
	Dir      Direction
	Breaker  bool
	Inverted bool
}

type Grid [][]rune

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var inputLines []string

	for {
		fmt.Println("Please provide the instructions for Optimus Jr (end input with an empty line):")
		inputLines = inputLines[:0] // reset for each map
		// Read until an empty line or EOF
		for scanner.Scan() {
			line := scanner.Text()
			if strings.TrimSpace(line) == "" {
				break
			}
			inputLines = append(inputLines, line)
		}
		if len(inputLines) == 0 {
			break // No more input
		}
		instructions := getInstructionsForInput(inputLines)
		fmt.Println(instructions)
	}
}

func getInstructionsForInput(i []string) string {
	grid := mapInput(i)
	x, y := getOptimusCoordinates(grid)
	state := State{
		X:        x,
		Y:        y,
		Dir:      South, // initial direction is always SOUTH
		Breaker:  false, // initial breaker mode is off
		Inverted: false, // initial inverter mode is off
	}
	return getInstructions(grid, &state)
}

func mapInput(inputLines []string) Grid {
	if len(inputLines) < 2 {
		log.Fatal("Invalid input: must contain at least two lines")
	}
	dimensions := strings.Split(inputLines[0], " ")
	height, _ := strconv.Atoi(dimensions[0])
	width, _ := strconv.Atoi(dimensions[1])

	grid := make(Grid, height)
	for y := range height {
		grid[y] = []rune(inputLines[y+1])
		if len(grid[y]) != width {
			log.Fatalf("Invalid input: line %d does not match specified width %d", y+1, width)
		}
	}
	return grid
}

func getOptimusCoordinates(grid Grid) (int, int) {
	for y := range grid {
		for x := range grid[y] {
			if grid[y][x] == '@' {
				return x, y
			}
		}
	}
	log.Fatalf("Invalid map for Optimus Jr — character '@' not found")
	return -1, -1
}

func getDirectionCoordinates(state *State, direction Direction) (x int, y int) {
	switch direction {
	case North:
		return state.X, state.Y - 1
	case East:
		return state.X + 1, state.Y
	case South:
		return state.X, state.Y + 1
	case West:
		return state.X - 1, state.Y
	}
	return
}

func getInstructions(g Grid, s *State) string {
	instructions := ""
	visited := make(map[State]bool)
	visited[*s] = true

	for Tile(g[s.Y][s.X]) != TileGoal {
		// Try current direction
		targetX, targetY := getDirectionCoordinates(s, s.Dir)
		if canGo(s, Tile(g[targetY][targetX])) {
			instructions += dirToString[s.Dir] + "\n"
			modifyState(s, g, targetX, targetY)
		} else {
			// Try each direction in priority order
			priority := normalPriority
			if s.Inverted {
				priority = invertedPriority
			}
			for _, direction := range priority {
				targetX, targetY := getDirectionCoordinates(s, direction)
				if canGo(s, Tile(g[targetY][targetX])) {
					instructions += dirToString[direction] + "\n"
					s.Dir = direction
					modifyState(s, g, targetX, targetY)
					break
				}
			}
		}

		if visited[*s] {
			return "LOOP\n"
		} else {
			visited[*s] = true
		}
	}

	return instructions
}

func canGo(s *State, t Tile) bool {
	if t == TileWall {
		return false
	}
	if t == TileEmpty || t == TileNorth || t == TileEast || t == TileSouth || t == TileWest || t == TileInverter || t == TileStart || t == TileGoal || t == TileBreaker {
		return true
	}
	if t == TileBreakable && s.Breaker {
		return true
	}
	if isTeleport(t) {
		return true
	}
	return false
}

func isTeleport(t Tile) bool {
	return len(t) == 1 && t[0] >= '1' && t[0] <= '9'
}

func findTeleportExit(g Grid, x int, y int) (int, int) {
	t := Tile(g[y][x])
	for exitY := range g {
		for exitX := range g[y] {
			if Tile(g[exitY][exitX]) == t && (exitX != x || exitY != y) {
				return exitX, exitY
			}
		}
	}
	return -1, -1
}

func modifyState(s *State, g Grid, x int, y int) {
	t := Tile(g[y][x])
	s.X = x
	s.Y = y
	if t == TileNorth {
		s.Dir = North
	}
	if t == TileEast {
		s.Dir = East
	}
	if t == TileSouth {
		s.Dir = South
	}
	if t == TileWest {
		s.Dir = West
	}
	if t == TileInverter {
		s.Inverted = !s.Inverted
	}
	if t == TileBreaker {
		s.Breaker = !s.Breaker
	}
	if t == TileBreakable {
		g[y][x] = ' '
	}
	if isTeleport(t) {
		exitX, exitY := findTeleportExit(g, x, y)
		s.X = exitX
		s.Y = exitY
	}
}
