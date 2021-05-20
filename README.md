# Project #2 Group 210 - Youtube

<img src="youtube/static/img/logo.png" alt="overview" width="120"/>

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

## About The Project

Small Youtube allows you to watch videos !
You can also create our own channel and upload videos.

### Built With

* [Python 3.7](https://www.python.org/)
* [Django 3.1.5](https://www.djangoproject.com/download/)
* [Bootstrap 4.5.2](https://www.bootstrapcdn.com/)
* [Axios 0.21.1](https://github.com/axios/axios)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites  
For **DEBIAN distributions**  
* Python 3.7
```sh
sudo apt install python3.7
```
* Pip3
```sh
sudo apt install python3-pip
```
* Django 3.1.5
```sh
pip3 install Django==3.1.5
```
* Pillow 8.1.2
```sh
pip3 install Pillow==8.1.2
```
> This library provides extensive file format support (requierement for the Django ImageField)

* django-crispy-forms 1.11.2
```sh
pip3 install django-crispy-forms==1.11.2
```
> Bootstrap form builder

### Installation

1. Clone the repo
```sh
git clone https://gitlab.computing.dcu.ie/conceia2/2021-ca229-project02.git
```
For **DCU containers**

2. Create a file named *user.txt* in *youtube/* that contains your DCU username
```sh
echo -n "<username>" > youtube/user.txt
```
## Usage

From *youtube/*
```
$ python3 manage.py runserver
```
For **DCU containers**  
```
$ python3 manage.py runserver 0.0.0.0:8080
```

## Roadmap

See the [open issues](https://gitlab.computing.dcu.ie/conceia2/2021-ca229-project02/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Axel Conceicao - axel.conceicao2@mail.dcu.ie - https://gitlab.computing.dcu.ie/conceia2  
Leonardo Shehu - Leonardo.shehu2@mail.dcu.ie - https://gitlab.computing.dcu.ie/shehul2 

Project Link: https://gitlab.computing.dcu.ie/conceia2/2021-ca229-project02

## Acknowledgements

* [Bootstrap Documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/)