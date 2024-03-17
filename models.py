from pydantic import BaseModel, field_serializer, HttpUrl


class ShortenURL(BaseModel):
    url: HttpUrl

    @field_serializer('url')
    def url2str(self, val) -> str:
        return str(val)