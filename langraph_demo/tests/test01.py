from langgraph_sdk import get_client, get_sync_client
import asyncio

async_client = get_client(url='http://localhost:2024')


async def async_main():
    async for chunk in async_client.runs.stream(
            None,
            'agent',
            input={
                'messages': [
                    {
                        'role': 'human',
                        'content': '3000 和 220 的和是多少'
                    }
                ]
            }
    ):
        print(f'receiving new event of type:{chunk.event}')
        print(chunk.data)
        print('\n\n')


sync_client = get_sync_client(url='http://localhost:2024')


def sync_main():
    for chunk in sync_client.runs.stream(
            None,
            'agent',
            input={
                'messages': [
                    {
                        'role': 'human',
                        'content': '北京天气怎么样? 哪里值得游玩 给出25个景点和2个游览计划'
                    }
                ]
            },
            stream_mode='messages-tuple',
            # stream_mode='messages',
            config={'configurable': {'user_name': 'user001'}}
    ):
        # print(f'receiving new event of type:{chunk.event}')
        # print(chunk.data)
        # print('\n\n')
        if isinstance(chunk.data, list) and 'type' in chunk.data[0] and chunk.data[0]['type']=='AIMessageChunk':
            print(chunk.data[0]['content'], end=' ')


if __name__ == '__main__':
    # asyncio.run(async_main())
    sync_main()
