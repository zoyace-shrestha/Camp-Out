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

    agents = 'config/agents.yaml'
    tasks = 'config/tasks.yaml'

    @agent
    def friend_1(self) -> Agent:
        """Friend 1 agent"""
        return Agent(
            config=self.agents['friend_1'],
            verbose=True,
        )
    
    @agent
    def friend_2(self) -> Agent:
        """Friend 2 agent"""
        return Agent(
            config=self.agents['friend_2'],
            verbose=True,
        )
    
    @agent
    def friend_3(self) -> Agent:
        """Friend 3 agent"""
        return Agent(
            config=self.agents['friend_3'],
            verbose=True,
        )
    
    @agent
    def orchestrator(self) -> Agent:
        """Orchestrator agent"""
        return Agent(
            config=self.agents['orchestrator'],
            verbose=True,
        )
    
    @task
    def participate_in_conversation(self) -> Task:
        """Participate in conversation"""
        return Task(
            config=self.tasks['participate_in_conversation'],
            verbose=True,
        )
    
    @task
    def steer_discussion(self) -> Task:
        """Steer discussion"""
        return Task(
            config=self.tasks['steer_discussion'],
            verbose=True,
        )
    
    @task
    def wrap_up_thought(self) -> Task:
        """Wrap up thought"""
        return Task( 
            config=self.tasks['wrap_up_thought'],
            verbose=True,
        )
    
    @task
    def orchestrate_conversation(self) -> Task:
        """Orchestrate conversation"""
        return Task(
            config=self.tasks['orchestrate_conversation'],
            verbose=True,
        )
    

    @crew
    def crew(self):
        """Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
            max_concurrency=10,
            process=Process.sequential,
        )

