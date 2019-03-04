from rasa_core.agent import Agent
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy

def train_core(domain_path, stories_path, model_dir):
  fallback = FallbackPolicy(fallback_action_name="action_default_fallback", core_threshold=0.3, nlu_threshold=0.3)
  agent = Agent(domain_path, policies=[MemoizationPolicy(), KerasPolicy(), fallback])
  data = agent.load_data(stories_path)
  agent.train(data)
  agent.persist(model_dir)

train_core('../domain.yml', '../data/stories.md', '../models/core')