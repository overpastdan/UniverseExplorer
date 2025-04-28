# Galaxy Explorer

An interactive space simulation game built with Python, Pygame, and Pymunk.

## Features

- Multiple galaxy systems with unique characteristics
- Binary star systems
- Planetary orbits with realistic physics
- Interactive solar system exploration
- Planet information display

## Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the game:
```bash
python main.py
```

## Controls

- Click on galaxies to explore their solar systems
- Click right click to return to galaxy view

## Project Structure

```
Gravity/
├── effects/
│   ├── particle_system.py
├── models/
│   ├── __init__.py
│   ├── galaxy.py
│   ├── galaxy_explorer.py
│   ├── planet.py
│   └── star.py
├── utils/
│   ├── __init__.py
│   ├── constants.py
│   └── physics.py
├── main.py
├── README.md
└── requirements.txt
```
