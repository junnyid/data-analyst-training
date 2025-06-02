# A Class to Test: Testing a class is similar to testing a function
class AnonymousSurvey:
    """Collect anounymous answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question."""
        print(self.question)
    
    def store_response(self, new_responses):
        """Store a single response to survey."""
        self.responses.append(new_responses)
    
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")