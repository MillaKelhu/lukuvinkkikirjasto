from invoke import task

@task
def start(ctx):
	ctx.run("python3 app.py")

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html")

@task
def lint(ctx):
	ctx.run("pylint src")
