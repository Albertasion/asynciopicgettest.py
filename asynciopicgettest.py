import asyncio
import httpx


async def download (query, current_page):
    header = {'Authorization' : '563492ad6f91700001000001953e522b3b7f422fa4d3ca05b715bf90'}
    params = {'query' : query, 'per_page' : 1 , 'page' : current_page}
    url = f'https://api.pexels.com/v1/search'

    async with httpx.AsyncClient() as client:
        r =await client.get(url, headers = header, params = params)
        if r.status_code == 200:
            r = r.json()
            for item in r.get('photos'):
                print(item.get('src').get('original'))

        else:
            print(r.status_code)


async def main():
    query = input('input yor search')
    page_count = int(input('page quntity'))
    current_page = 0
    task_list =[]
    while current_page < page_count:
        current_page+=1
        task = asyncio.create_task(download(query, current_page))
        task_list.append(task)
    await asyncio.gather(*task_list)



loop = asyncio.get_event_loop()
loop.run_until_complete(main())


