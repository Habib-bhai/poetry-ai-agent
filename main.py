# Types of Poetry
# - Lyric poetry is when poets write about their own feelings and thoughts, like songs or poems about being sad or happy.

# - Narrative poetry tells a story with characters and events, just like a regular story but written in poem form with rhymes or special rhythm.

# - Dramatic poetry is meant to be performed out loud, where someone acts like a character and speaks their thoughts and feelings to an audience (acting in a theatre).

# 1. Make a poet agent. Alternatively you could pass a poetry (2 stanza) as an input.
# 2. Make three analyst agent. 
# 3. Make a triage/Orchestrator/Parent agent.

# Exercise: Make a Triage/Parent agent that gives takes a poetry as an input and Triage/Poetry agent analyze the poetry and handoffs to the appropriate agent. The appropriate analyze agent should give description (tashree) of the poetry.

from config import config 
from agents import Agent,Runner, handoff, RunContextWrapper
from poet_agents.dramatic_poet import dramatic_poet
from poet_agents.lyric_poet import lyric_poet
from poet_agents.narrative_poet import narrrative_poet


def handoff_handler(ctx: RunContextWrapper[None]):
    pass

triage_agent = Agent(
    name="Triage Agent",
    instructions="You are a Poet now. you will be getting different types of poetries from user like lyric, dramatic, narrative etc. analyzing the poetary, handoff that poetry (user input) to the appropriate expert poet to get its detailed description/tashree.",
    
    handoffs=[handoff(dramatic_poet, on_handoff=handoff_handler),
              handoff(lyric_poet, on_handoff=handoff_handler),
              handoff(narrrative_poet, on_handoff=handoff_handler)
              ],    
)



