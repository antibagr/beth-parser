# bethowen.ru Parser

![CI Workflow](https://github.com/antibagr/Any-Python-Template/actions/workflows/makefile.yml/badge.svg?event=push)![coverage badge](./coverage.svg)

## Table of Contents
- [bethowen.ru Parser](#bethowenru-parser)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Usage](#usage)
    - [Installation](#installation)
    - [Environment Variables](#environment-variables)
  - [Contributing](#contributing)
    - [Poetry](#poetry)
    - [Dependencies](#dependencies)
  - [Run](#run)
    - [Development](#development)



## Description

Library orchestrates the pull of processes to parse products from [bethowen](https://www.bethowen.ru).
1. First it requests the sitemap, then it parses the categories, sub categories, sections and products.
- 1.1 The anti captcha service is not yet implemented, so you have to solve the captcha manually.
2. With all the product urls known, it spawns a pool of processes to parse the products using [aiomultiprocess](https://github.com/omnilib/aiomultiprocess) library.
3. The parsed products are stored in MongoDB after the `BATCH_SIZE` is reached.


## Usage

> **Note for Windows Users:**
>
> If you are using Windows, it's important to ensure that you have Windows Subsystem for Linux (WSL) 2 installed and configured correctly before running the provided commands under a WSL terminal. WSL 2 provides a Linux-compatible environment that can be used for development tasks.
>
> To install and set up WSL 2 on your Windows machine, please follow the official Microsoft documentation: [Install Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).
>
> Once WSL 2 is set up, make sure to use the WSL terminal for running the commands specified in this documentation for a seamless development experience.
>
> If you encounter any issues related to WSL or need further assistance, please refer to the Microsoft WSL documentation or seek support from the WSL community.


### Installation

### Environment Variables

The following environment variables are required to run the application:

| Variable Name           | Description                               |
| ----------------------- | ----------------------------------------- |
| `ENVIRONMENT`           | Environment name (either `dev` or `prod`) |
| `DEBUG`                 | Debug mode (either `true` or `false`)     |
| `SITEMAP_URL`           | Sitemap URL                               |
| `ANTI_CAPTCHA_API_KEY`  | Anti Captcha API key                      |
| `ANTI_CAPTCHA_SITE_KEY` | Anti Captcha site key                     |
| `BATCH_SIZE`            | How many products to insert at once       |
| `MONGO_DB_URI`          | MongoDB URI                               |
| `MONGO_DB_NAME`         | MongoDB database name                     |


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Poetry

Install poetry using your package manager or [official guide](https://python-poetry.org/docs/#installation).

### Dependencies

The easiest way to install required and dev dependencies is as follows:

```bash
make install
```


## Run

Now you can run the following command to start the application:

```bash
make run
```

### Development

This will install all the dependencies and create a virtual environment for you.

Now you can format the code using:

```bash
make format
```

To run linters:

```bash
make lint
```

To run tests:

```bash
make test
```
