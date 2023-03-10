class ASGIApplication:
    def __init__(self, scope):
        assert scope["type"] == "http"
        self.scope = scope

    async def __call__(self, receive, send):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ],
        })

        await send({
            'type': 'http.response.body',
            'body': b'Hello, world!',
        })


