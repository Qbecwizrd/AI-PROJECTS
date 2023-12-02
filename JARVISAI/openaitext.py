# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI

api_key = "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"
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "generate a resignation letter for me very short\n"
    },
    {
      "role": "user",
      "content": ""
    },
    {
      "role": "assistant",
      "content": "[Your Name]\n[Your Address]\n[City, State ZIP Code]\n[Email Address]\n[Phone Number]\n[Date]\n\n[Recipient's Name]\n[Recipient's Job Title]\n[Company Name]\n[Company Address]\n[City, State ZIP Code]\n\nDear [Recipient's Name],\n\nI hope this letter finds you well. I am writing to officially resign from my position as [Your Job Title] at [Company Name], effective [Last Working Day - typically two weeks from the date of the letter, unless otherwise specified].\n\nIt is with mixed emotions that I submit my resignation. Over the past [X years/months], I have genuinely enjoyed working at [Company Name]. The experiences, challenges, and knowledge gained during this time have been invaluable to my personal and professional growth. I am grateful for the opportunities I have received and the collaborative work environment that has fostered my career development.\n\nAfter much consideration, I have decided to pursue a new opportunity that aligns more closely with my long-term career aspirations. While it was a difficult decision to make, I firmly believe it is the right path for my professional growth and development.\n\nI am committed to making a smooth transition during the notice period. I will do my best to ensure that all pending projects and tasks are either completed"
    },
    {
      "role": "assistant",
      "content": "or handed over to a designated team member before my departure. Please let me know if there is anything specific I can do to facilitate a seamless transition.\n\nI am grateful for the invaluable experience and support I have received from you and the entire team at [Company Name]. I will always cherish the relationships I have built here and the knowledge I have gained. I am confident that [Company Name] will continue to thrive and achieve great success in the future.\n\nThank you once again for the opportunity to be part of the [Company Name] family. I wish you and the entire team nothing but the best for the future.\n\nSincerely,\n[Your Name]"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
'''
ChatCompletion(id='chatcmpl-8N0F9x0XMQrtb5HJhgZr0ssywg5AS', choices=[Choice(finish_reason='stop', index=0, message=ChatCompletionMessage(content="[Your Name]\n[Your Address]\n[City, State ZIP Code]\n[Email Address]\n[Phone Number]\n[Date]\n\n[Recipient's Name]\n[Recipient's Job Title]\n[Company Name]\n[Company Address]\n[City, State ZIP Code]\n\nDear [Recipient's Name],\n\nI am writing to inform you of my decision to resign from my position at [Company Name]. Please accept this letter as my formal resignation, effective [Last Working Day - typically two weeks from the date of the letter, unless otherwise specified].\n\nI have enjoyed my time at [Company Name] and have valued the opportunities and experiences I have gained during my tenure. However, after careful consideration, I have decided to pursue new opportunities that will further enhance my professional growth.\n\nI will ensure a smooth transition of my responsibilities and duties before my departure. Please let me know how I can assist in this process.\n\nI appreciate the support and guidance provided by [Recipient's Name] and the entire team. I am confident that [Company Name] will continue to thrive and achieve great success in the future.\n\nThank you for the understanding and for making this transition as smooth as possible.\n\nSincerely,\n[Your Name]", role='assistant', function_call=None, tool_calls=None))], created=1700493171, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=238, prompt_tokens=414, total_tokens=652))

'''