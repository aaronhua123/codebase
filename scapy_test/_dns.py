import requests


class HostHeaderSSLAdapter(requests.adapters.HTTPAdapter):

    def __init__(self, resolutions):
        super().__init__()
        self.resolutions = resolutions
    def resolve(self, hostname):
        # a dummy DNS resolver
        return self.resolutions.get(hostname)

    def send(self, request, **kwargs):
        from urllib.parse import urlparse

        connection_pool_kwargs = self.poolmanager.connection_pool_kw

        result = urlparse(request.url)
        resolved_ip = self.resolve(result.hostname)

        if result.scheme == 'https' and resolved_ip:
            request.url = request.url.replace(
                'https://' + result.hostname,
                'https://' + resolved_ip,
            )
            connection_pool_kwargs['server_hostname'] = result.hostname  # SNI
            connection_pool_kwargs['assert_hostname'] = result.hostname

            # overwrite the host header
            request.headers['Host'] = result.hostname
        else:
            # theses headers from a previous request may have been left
            connection_pool_kwargs.pop('server_hostname', None)
            connection_pool_kwargs.pop('assert_hostname', None)

        return super(HostHeaderSSLAdapter, self).send(request, **kwargs)


url = 'https://www.baidu.com'

session = requests.Session()
session.mount('https://', HostHeaderSSLAdapter({
            'www.baidu.com': '183.2.172.42',
        }))

r = session.get(url, verify=False)
print(r.text)

r = session.get(url, verify=False)
print(r.text)