# Install python3 and create a new project.

python3 --version
mkdir my_agent
cd my_agent
python3 -m venv .venv
source .venv/bin/activate
which python
# install langgraph and langchain

pip install --pre langgraph langchain langchain-openai
pip install "langgraph-cli[inmem]"

# run the agent
langgraph dev# LangGraph
