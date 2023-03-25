import openai
import os


class Chat:
    def __init__(self, temperature: float = 0.7, verbose: bool = True):
        """
        Initializes the Chat object with the given temperature and verbose settings.

        Args:
            temperature (float, optional): The temperature to use for the chatbot. Defaults to 0.7.
            verbose (bool, optional): Whether to print the chat history. Defaults to True.
        """

        self.temperature = temperature
        self.verbose = verbose
        self.gpt_chat_history = []

    def add_to_history(self, content: str, role: str = "user") -> None:
        """
        Adds the given content to the chat history.

        Args:
            content (str): The content to add to the chat history.
            role (str, optional): The role of the content. Defaults to "user".
        """

        self.gpt_chat_history.append(
            {
                "role": role,
                "content": content,
            }
        )

        if self.verbose:
            print(self.gpt_chat_history[-1])

    def message(self, content: str, role: str = "user") -> None:
        """
        Sends a message to the chatbot.

        Args:
            content (str): The content of the message.
            role (str, optional): The role of the message. Defaults to "user".
        """

        self.add_to_history(content, role)

        gm_res = openai.ChatCompletion.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4-0314"),
            messages=self.gpt_chat_history,
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        answer = gm_res["choices"][0]["message"]["content"].strip()
        self.add_to_history(answer, "assistant")
        return answer