from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from datetime import datetime
from langchain_community.llms import OpenAI
from langchain.output_parsers import DatetimeOutputParser
from langchain_community.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI
api_key = "YOUR_API_KEY"
class Quiz():

    def create_quiz_question(self, topic):

        # PART ONE: SYSTEM
        system_template = "You write single quiz questions about {topic}. You only return the quiz question."
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
        # PART TWO: HUMAN REQUEST
        human_template = "{question_request}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        # PART THREE: COMPILE TO CHAT
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        # PART FOUR: INSERT VARIABLES
        request = chat_prompt.format_prompt(topic=topic,
                                            question_request="Give me a quiz question where the correct answer is a specific date.").to_messages()
        # PART FIVE: CHAT REQUEST
        chat = ChatOpenAI(openai_api_key=api_key)
        result = chat(request)

        return result.content

    def get_openAI_answer(self, question):

        # Datetime Parser
        output_parser = DatetimeOutputParser()

        # SYSTEM Template
        system_template = "You answer quiz questions with just a date."
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)


        # HUMAN Template
        human_template = """Answer the user's question:
        
        {question}
        
        {format_instructions}"""
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        # Compile ChatTemplate
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])

        # Insert question and format instructions

        request = chat_prompt.format_prompt(question=question,
                                            format_instructions=output_parser.get_format_instructions()).to_messages()
        # Chat Bot
        chat = ChatOpenAI(openai_api_key=api_key)
        result = chat(request)
        # Format Request to datetime
        correct_datetime = output_parser.parse(result.content)
        return correct_datetime


    def get_human_answer(self, question):

        print(question)


        # Get the year, month, and day from the user
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        day = int(input("Enter the day (1-31): "))

        # Create a datetime object
        user_datetime = datetime(year, month, day)


        return user_datetime

    def check_user_guess(self, user_answer, ai_answer):


        # Calculate the difference between the dates
        difference = user_answer - ai_answer

        # Format the difference into a string
        formatted_difference = str(difference)

        # Return the string reporting the difference
        print("The difference between the dates is:", formatted_difference)