# Paper Trading Application

[![Made with Pthon](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


![application screenshot](https://i.imgur.com/Uu9lNeB.png)

## About

> A paper trading application. Users are credited with an initial balance and then they can search for a stock ticker and then buy or sell given stock.




## Getting Started

### Prerequisites

* Python; [pyenv](https://github.com/pyenv/pyenv) recommended
* Pip

### Installation


1. Create a personal [Fork](https://github.com/edgars61/stock-trader-app) of this repository.

2. **Clone** the fork with HTTPS, using your local terminal to a preferred location, and **cd** into the project.

```bash
git clone https://github.com/edgars61/stock-trader-app.git

Cloning into 'stock-trader-app'...
remote: Enumerating objects: 337, done.
remote: Counting objects: 100% (337/337), done.
remote: Compressing objects: 100% (201/201), done.
remote: Total 337 (delta 184), reused 260 (delta 113), pack-reused 0
Receiving objects: 100% (337/337), 568.77 KiB | 2.96 MiB/s, done.
Resolving deltas: 100% (184/184), done.


cd stock-trader-app/
```

3. Create your virtual environment, and activate it.

```bash
python -m venv env

source env/bin/activate  # Linux/Mac
env/Scripts/activate  # Windows
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run local server, and **DONE**!

```bash
python manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).
March 18, 2021 - 14:48:05
Django version 3.1.5, using settings 'stocktraderapp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```




## Built With

* [Django](https://www.djangoproject.com/) Django is a high-level Web framework that encourages rapid development and clean, pragmatic design.
* [Matplotlib](https://matplotlib.org) Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
* [Bootstrap](https://getbootstrap.com/)


## License

[@MIT](https://github.com/BrianRuizy/covid19-dashboard/blob/master/LICENSE.md)
