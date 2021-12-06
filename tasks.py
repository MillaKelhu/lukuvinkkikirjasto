from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/app.py")

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html")

@task
def lint(ctx):
	ctx.run("pylint src")

@task
def robot(ctx):
	ctx.run("robot src/tests")

@task
def test(ctx):
	ctx.run("pytest src")
