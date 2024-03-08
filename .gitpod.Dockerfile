FROM gitpod/workspace-full

# Python Dependencies
ARG PYTHON_VERSION=3.9

RUN sudo add-apt-repository ppa:deadsnakes/ppa -y
RUN sudo apt install python${PYTHON_VERSION} -y
RUN sudo apt install python${PYTHON_VERSION}-venv -y
RUN sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 2
RUN sudo pip install --upgrade pip

RUN sudo pip install build
RUN sudo pip install tox
RUN sudo pip install sphinx
RUN sudo pip install pipdeptree



