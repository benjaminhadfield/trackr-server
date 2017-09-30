from invoke import task, run


REQUIREMENTS_DIR = './requirements'
APPS_DIR = './apps'

@task
def startapp(ctx, name):
    if not name:
        return 'Please give an app name.'

    app_dir = '{0}/{1}'.format(APPS_DIR, name)
    make_dir = 'mkdir {0}'.format(app_dir)
    make_app = 'django-admin startapp {0} {1}'.format(name, app_dir)
    run(make_dir)
    run(make_app)
    print('App \'{0}\' created!'.format(name))


@task
def install(ctx, package, env):
    envs = {
        'common': 'common',
        'local': 'local',
        'production': 'production'
    }

    # Expand single letter args to full env value.
    if len(env) == 1:
        if env == 'c':
            env = envs['common']
        if env == 'l':
            env = envs['local']
        if env == 'p':
            env = envs['production']

    if env not in envs.values():
        return 'Please add an environment to add the package to.' \
               'Valid environments are {}'.format(envs.values())


    install_cmd = 'pip install {}'.format(package)
    requirements_cmd = 'echo `pip freeze | grep {0}` >> {1}/{2}.txt' \
        .format(package, REQUIREMENTS_DIR, env)

    run(install_cmd)
    run(requirements_cmd)

    print('Requirement \'{0}\' installed and added to \'{1}\' requirements!'
          .format(package, env))
