# tmp-serverless-python

Install Serverless plugin: serverless-python-requirements

```sh
$ npm install
```

### Usage

Install a Python dependency (for example, [Requests](http://docs.python-requests.org/en/master/))

```sh
$ pip install requests
```

Store a reference to your dependencies

```sh
$ pip freeze > requirements.txt
```

Re-install your dependencies from your requirements

```sh
$ pip install -r requirements.txt
```

Invoke a function locally

```
$ serverless invoke local -f hello
```

Run your tests
```
$ python -m unittest discover -s tests
```

Deactivate your virtual environment

```sh
$ deactivate
```

### Deploying

Deploy your project

```sh
$ serverless deploy
```

Deploy a single function

```sh
$ serverless deploy function --function hello
```

To compile non-pure Python modules, install [Docker](https://docs.docker.com/engine/installation/) and the [Lambda Docker Image](https://github.com/lambci/docker-lambda). Enable **dockerizePip** in **serverless.yml** and `serverless deploy` again.

```yml
# enable dockerize Pip
custom:
  pythonRequirements:
    dockerizePip: true
```

**Note**, if you are deploying using [SEED](https://seed.run), you don't need to enable **dockerizePip** or install Docker. [SEED](https://seed.run) does it automatically.

