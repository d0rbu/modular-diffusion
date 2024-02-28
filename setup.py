from setuptools import setup, find_packages

setup(
    name="modular-diffusion",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "einops",
        "pyyaml",
        "tqdm",
        "torchvision",
        "lightning",
        "pillow",
        "numpy",
    ],
)