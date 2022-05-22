
# STN(A) - Studencki Transporter Napojów (A)

Source code of a group project developed as part of the Projekt Zespołowy P lead by Dr. Jarosław Glapiński in the semester 2021/2022.

## Required modules
 - `inputs`
 - `future`
 - `RPi.GPIO`


You can install required libraries by using pip. Make sure you setup a [virtual environment](https://docs.python.org/3/library/venv.html) beforehand, i.e. like this:
```python
  python -m venv <path_to_your_venv>
```

## Installation

For now, clone it from git and launch from command line.

```bash
  git clone https://github.com/jestem-andrew/STN.git
```

## Run the scrypt

In order to run the line follower scrypt, use
```bash
  python line_follower.py <flag>
```
Currently supported flags:
 - `use_gamepad`(in order to control the line follower with an Xbox 360 gamepad)

## Authors

- Andrzej Małolepszy [@jestem-andrew](https://www.github.com/jestem-andrew)
- Paulina Poręba
- Julia Kurzawa

## Supervisor

 - Damian Kociołek

