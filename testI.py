import asyncio
import os

import pytest
from dotenv import load_dotenv

from langchain_anthropic import ChatAnthropic
from ragas import SingleTurnSample
from ragas.llms import LangchainLLMWrapper
from ragas.metrics._context_precision import LLMContextPrecisionWithoutReference

load_dotenv()

@pytest.mark.asyncio
async def test_context_precision():
    if not os.getenv("ANTHROPIC_API_KEY"):
        pytest.skip("ANTHROPIC_API_KEY is not set")

    model_name = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
    print(f"Using Anthropic model: {model_name}", flush=True)

    llm_model = ChatAnthropic(temperature=0, model_name=model_name)
    langchain_llm = LangchainLLMWrapper(llm_model)
    context_precision = LLMContextPrecisionWithoutReference(llm = langchain_llm)

    # feed data
    sample = SingleTurnSample(
        user_input = "How many articles are present in the Selenium WebDriver course?",
        response = "There are **63 articles** included in the Selenium Webdriver course.",
        retrieved_contexts= [
            "Wish you all the Best! See you all in the course with above topics :)\n\nWho this course is for:\nAutomation Engineers\nSoftware Engineers\nManual testers\nSoftware developers",
            "What you'll learn\n*****By the end of this course,You will be Mastered on Selenium Webdriver with strong Core JAVA basics\n****You will gain the ability to design PAGEOBJECT, DATADRIVEN&HYBRID Automation FRAMEWORKS from scratch\n*** InDepth understanding of real time Selenium CHALLENGES with 100 + examples\n*Complete knowledge on TestNG, MAVEN,ANT, JENKINS,LOG4J, CUCUMBER, HTML REPORTS,EXCEL API, GRID PARALLEL TESTING",
            "This course includes:\n55 hours on-demand video\n2 coding exercises\nAssignments\n63 articles\n138 downloadable resources\nAccess on mobile and TV\nCertificate of completion",
            "Course includes real time projects with practical Solutions for the Robust Selenium Framework building\nTheoretical Material,Code dump and Interview Guide are available for download\nNew : JOB ASSISTANCE after completion of course to make your Profile reach to Hundreds of Recruiters in my network.******\nJoin in our Selenium Training community with (350 + lectures, 5 Million Students) Learning Together which you will not see in any other Selenium online course on Udemy."
        ]
    )

    print("Computing context precision score...", flush=True)
    try:
        score = await asyncio.wait_for(
            context_precision.single_turn_ascore(sample),
            timeout=30,
        )
    except asyncio.TimeoutError as exc:
        pytest.fail("Timed out waiting for context precision score (30s)")

    print(f"The score is: {score}")
    assert score is not None
    assert 0 <= score <= 1