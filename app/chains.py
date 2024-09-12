import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
                   """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Shashank, a final-year Computer Science student at VIT with strong expertise in Java, Python, JavaScript, and Django. You have internship experience at IRCTC, where you developed a payroll system, and a wide range of project experience in fields like web development, machine learning, and simulation modeling.
        Your task is to write a cold email to the hiring manager, showcasing your technical proficiency while addressing their specific requirements. Mention your projects selectively, but only if they align with the job's required skills. Do not list or stick all projects everywhere.
        
        Available projects and skills to mention:
        
        - Java (75CodeStrong: [75CodeStrong](https://github.com/shashank651156/75CodeStrong))
        - JavaScript (AutoPlayPauseYouTubeVideo-Extension: [AutoPlayPauseYouTubeVideo-Extension](https://github.com/shashank651156/AutoPlayPauseYouTubeVideo-Extension))
        - Python, scikit-learn (Miniature-engine-Spam-Mail-Detection: [Miniature-engine-Spam-Mail-Detection](https://github.com/shashank651156/miniature-engine-Spam-Mail-Detection-))
        - Python (MonteCarloSimulation-usingManufacturingVars: [MonteCarloSimulation-usingManufacturingVars](https://github.com/shashank651156/MonteCarloSimulation-usingManufacturingVars))
        - Django, HTML, CSS, JavaScript (RoomTalk: [RoomTalk](https://github.com/shashank651156/RoomTalk-aDiscordLikeWebApplication))
        
        Use these projects only when they directly fit the skills required in the job description. Focus on how your experience and skills can meet the company's needs while offering concrete examples of your past work when relevant.
        make it like human written.
        ### EMAIL (NO PREAMBLE):
        
        """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content