from invoke import task, run


REQUIREMENTS_DIR = './requirements'
APPS_DIR = './apps'


"""
Starts a new Django App, placing it in the apps dir.
"""
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


"""
Installs a package using PIP, and adds the dependency to the specified
requirements file.
"""
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
            env = envs['prod']

    if env not in envs.values():
        return 'Please add an environment to add the package to.' \
               'Valid environments are {}'.format(envs.values())

    # If this fails then the function exits.
    run('pip install {}'.format(package))

    # Check if the requirement is already listed in the file.
    is_listed = run(
        'grep {0} requirements/{1}.txt'.format(package, env), warn=True)
    if len(is_listed.stdout) == 0:
        # Add to requirements file.
        requirements_cmd = 'echo `pip freeze | grep {0}` >> {1}/{2}.txt' \
            .format(package, REQUIREMENTS_DIR, env)
        run(requirements_cmd)
        print('Requirement \'{0}\' installed and added '
              'to \'{1}\' requirements!'.format(package, env))
    else:
        print('Requirement is already listed in {0}.txt.'.format(env))

    print('Install complete!')
