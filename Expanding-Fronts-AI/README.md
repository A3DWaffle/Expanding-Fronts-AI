# Expanding Fronts AI

Prototype RTS AI scripting work for *Star Wars: Galactic Battlegrounds* and the *Expanding Fronts* mod.

This repository contains `.per` AI script files used for rule-based computer player behavior. The project focuses on scripting organization, faction behavior, military population logic, research handling, resource gathering, naval behavior, difficulty support, and other systems used by the game's AI.

## Project Purpose

The goal of this project is to improve and organize AI behavior for *Expanding Fronts* while keeping the script files easier to read, test, and maintain. The AI is built around rule-based logic, which means behavior is controlled through scripted conditions, goals, constants, and strategic rules.

## Featured Areas

- Rule-based RTS AI scripting
- Military population and unit composition logic
- Faction-specific behavior support
- Research and technology handling
- Resource gathering logic
- Naval and island map behavior
- Difficulty-specific AI behavior
- Script organization and documentation

## File Format

Most files in this repository use the `.per` extension. These are AI script files used by the *Star Wars: Galactic Battlegrounds* AI system.

Examples include:

- `constants.per` — shared constants and AI identifiers
- `combat-arm.per` — military branch and combat behavior logic
- `military-population.per` — standard military population logic
- `military-population-hard.per` — hard difficulty military population logic
- `research.per` — research and technology rules
- `sn-gather.per` — strategic number and resource gathering behavior
- `warboat.per` — naval behavior logic

## Status

This is prototype AI work. Some files may contain experimental logic, unfinished behavior, or code that is still being tested and reorganized. This repository is intended as a portfolio and development reference rather than a final release package.

## Related Tool

I also created a Visual Studio Code extension for *Star Wars: Galactic Battlegrounds* and *Expanding Fronts* AI scripting:

https://marketplace.visualstudio.com/items?itemName=A3DWaffle.ef-ai-tools

The extension adds editor support for `.per` and `.bin` AI script files, including syntax highlighting, completions, hover documentation, signature help, rule folding, outline support, and basic diagnostics.

## Suggested Use

These scripts are intended for inspection, experimentation, and development reference. They may need to be integrated into the correct *Expanding Fronts* AI folder structure before use in-game.

## Disclaimer

This is a fan-made AI scripting project for *Star Wars: Galactic Battlegrounds* and *Expanding Fronts*. Star Wars and related properties belong to their respective owners. This repository does not include game assets, executables, or official copyrighted media.
