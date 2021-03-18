# Paper Trading Application

[![Made with Pthon](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


![application screenshot](https://i.imgur.com/Uu9lNeB.png)

## About

> Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.
> At this time, there are no specific vaccines or treatments for COVID-19. The best way to prevent and slow down transmission is be **well informed** about the COVID-19 virus. [who.int](https://www.who.int/health-topics/coronavirus#tab=tab_1)

The goal of this project is not to build *just another dashboard*. But, to focus on collaborative plot ideas, and a mobile friendly UI/UX. Feel free to open an issue requesting a type of plot, table, or any feature for that matter. Join the repo's [Gitter chat](https://gitter.im/ncov-dashboard/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link).

## Contributors

[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/images/0)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/links/0)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/images/1)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/links/1)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/images/2)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/links/2)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/images/3)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/links/3)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/images/4)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/links/4)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/images/5)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/links/5)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/images/6)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/links/6)[![](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/images/7)](https://sourcerer.io/fame/BrianRuizy/BrianRuizy/covid-19-dashboard/links/7)

## Getting Started

### Prerequisites

* Python; [pyenv](https://github.com/pyenv/pyenv) recommended
* Pip

### Installing

Get the project up and running locally in just 5 easy steps.

1. Create a personal [Fork](https://github.com/login?return_to=%2FBrianRuizy%2Fcovid19-dashboard) of this repository.

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

May 06, 2020 - 11:22:23
Django version 3.0.6, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Deployment

Heroku app is already configured to this repository for *automatic deploys* from any push to the **master** branch. Create a pull request containing your respective changes and wait for merge.

## Reading data locally
You can go through all the available datasets by going into the `/processdata` directory, launching a interactive python shell, importing `getdata` file, and calling any function. See below...

```bash
cd ~/repos/covid19-dashboard/processdata
```

```bash
$ python

Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32 
...

>>> import getdata
>>> getdata.realtime_growth()

         Confirmed  Deaths  Recovered
Date
1/22/20        555      17         28
1/23/20        654      18         30
...            ...     ...        ...
8/2/20    18079723  689362   10690555
8/3/20    18282208  693694   10913000

[195 rows x 3 columns]
```


## Built With

* [Django](https://www.djangoproject.com/) Django is a high-level Web framework that encourages rapid development and clean, pragmatic design.
* [Plotly](https://plotly.com/) The leading front-end for ML & data science models in Python, R, and Julia.
* [Appseed](https://appseed.us/)
* [Bootstrap](https://getbootstrap.com/)

## Data Sources

* Johns Hopkins University: [CSSE](https://systems.jhu.edu/) 2019-ncov data repository, found [here](https://github.com/CSSEGISandData/COVID-19).
* Our World in Data: [OWID](https://ourworldindata.org/) GitHub Data repository, found [here](https://github.com/owid/covid-19-data/tree/master/public/data).
* New York Times' COVID GitHub data repository, found [here](https://github.com/nytimes/covid-19-data)

## License

[@MIT](https://github.com/BrianRuizy/covid19-dashboard/blob/master/LICENSE.md)
