import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="modified-ai-economist",
    version="1.1.0",
    author="Aslan Satary Dizaji",
    author_email="asataryd@umich.edu",
    description="Modified AI-Economist: Multi-agent Reinforcement Learning for Economics and Neuroscience",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aslansd/modified-ai-economist",
    packages=setuptools.find_packages(),
    package_data={
        "modified_ai_economist": [
            "foundation/scenarios/simple_wood_and_stone_iron/map_txt/*.txt",
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)