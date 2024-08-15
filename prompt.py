'''prompt module'''
class Prompt:
    '''Prompt'''
    @staticmethod
    def get_prompt(topic, helper_content):
        '''Returns the prompt for the given topic'''
        prompt = f"""You are an expert content writer. Please follow the instructions below to generate a comprehensive blog post:

        Topic and Information: You will be given a topic and some initial content (helper content) to guide your writing.
        Research: Use your internet research skills and existing knowledge to gather additional information on the topic.
        
        Writing Guidelines:
        
        Craft the blog in clear and simple language.
        Ensure the content is well-structured, with logical flow and proper formatting.
        Provide comprehensive coverage of the topic, offering valuable insights and actionable takeaways for the reader.
        Topic: {topic}

        Helper Content: {helper_content}

        Your Blog:

        """
        return prompt
