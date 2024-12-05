
from setuptools import Extension, setup

setup(
	name="foreign",
	version="1.0.0",
	description="Matrix exponentiation module",
	author="Wokzy",
	author_email="yegor1552@yandex.ru",
	ext_modules=[
		Extension(
			name="foreign",
			sources=["13.c"],
		),
	]
)
