from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CampOut():
    """CampOut crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def friend_1(self) -> Agent:
        """Friend 1 agent"""
        return Agent(
            config=self.agents_config['friend_1'],
            verbose=True,
        )
    
    @agent
    def friend_2(self) -> Agent:
        """Friend 2 agent"""
        return Agent(
            config=self.agents_config['friend_2'],
            verbose=True,
        )
    
    @agent
    def friend_3(self) -> Agent:
        """Friend 3 agent"""
        return Agent(
            config=self.agents_config['friend_3'],
            verbose=True,
        )
    
    @agent
    def orchestrator(self) -> Agent:
        """Orchestrator agent"""
        return Agent(
            config=self.agents_config['orchestrator'],
            verbose=False,  # Match YAML config
        )
    
    @task
    def zeak_conversation(self) -> Task:
        """Zeak's conversation contribution"""
        return Task(
            config=self.tasks_config['zeak_conversation'],
            verbose=True,
        )
    
    @task
    def rhea_conversation(self) -> Task:
        """Rhea's conversation contribution"""
        return Task(
            config=self.tasks_config['rhea_conversation'],
            verbose=True,
        )
    
    @task
    def kai_conversation(self) -> Task:
        """Kai's conversation contribution"""
        return Task(
            config=self.tasks_config['kai_conversation'],
            verbose=True,
        )
    

    @crew
    def crew(self):
        """Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            max_concurrency=1,  # Sequential with delegation for conversation flow
            process=Process.sequential,
            memory=True,  # Enable memory to track conversation flow
        )

