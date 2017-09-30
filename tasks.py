from invoke import task, run


@task
def startapp(ctx, name):
    if not name:
        print('Please give an app name.')
        return
    app_dir = './apps/{}'.format(name)
    make_dir = 'mkdir {0}'.format(app_dir)
    make_app = 'django-admin startapp {0} {1}'.format(name, app_dir)
    run(make_dir)
    run(make_app)
    print('App \'{0}\' created!'.format(name))
