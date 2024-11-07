import g4f
import asyncio


_providers = [
    g4f.Provider.Ai4Chat,
    #g4f.Provider.Aura,
    #g4f.Provider.AIUncensored,
    g4f.Provider.DDG,
    #g4f.Provider.ChatGot,
    #g4f.Provider.ChatBase,
    #g4f.Provider.Bing,
    #g4f.Provider.GptGo,
    #g4f.Provider.DeepInfra,
    #g4f.Provider.You,
    #g4f.Provider.Editee,
    g4f.Provider.Free2GPT,
    #g4f.Provider.Pi,
    #g4f.Provider.Gemini,
    #g4f.Provider.Yqcloud,
    #g4f.Provider.MetaAI,
    g4f.Provider.NexraQwen,
    #g4f.Provider.HuggingChat,
]


async def run_provider(provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Что такое пиу-пиу?"}],
            provider=provider,
        )
        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [run_provider(provider) for provider in _providers]
    await asyncio.gather(*calls)


asyncio.run(run_all())