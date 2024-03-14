# Generated using abnf-to-regex 1.1.2

scheme = '(?P<scheme>[a-zA-Z][a-zA-Z0-9+\\-.]*)'
unreserved = '[a-zA-Z0-9\\-._~]'
pct_encoded = '%[0-9A-Fa-f][0-9A-Fa-f]'
sub_delims = "[!$&'()*+,;=]"
userinfo = f'(?P<userinfo>({unreserved}|{pct_encoded}|{sub_delims}|:)*)'
h16 = '[0-9A-Fa-f]{1,4}'
dec_octet = '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
ipv4address = f'(?P<IPv4address>{dec_octet}\\.{dec_octet}\\.{dec_octet}\\.{dec_octet})'
ls32 = f'({h16}:{h16}|{ipv4address})'
ipv6address = ('(?P<IPv6address>'
    f'({h16}:){{6}}{ls32}|::({h16}:){{5}}{ls32}|({h16})?::({h16}:){{4}}'
    f'{ls32}|(({h16}:)?{h16})?::({h16}:){{3}}{ls32}|(({h16}:){{2}}{h16})?::'
    f'({h16}:){{2}}{ls32}|(({h16}:){{3}}{h16})?::{h16}:{ls32}|(({h16}:){{4}}'
    f'{h16})?::{ls32}|(({h16}:){{5}}{h16})?::{h16}|(({h16}:){{6}}{h16})?::'
')')
ipvfuture = f'(?P<IPvFuture>[vV][0-9A-Fa-f]+\\.({unreserved}|{sub_delims}|:)+)'
ip_literal = f'(?P<IP_literal>\\[({ipv6address}|{ipvfuture})\\])'
reg_name = f'(?P<reg_name>({unreserved}|{pct_encoded}|{sub_delims})*)'
host = f'(?P<host>{ip_literal}|{ipv4address}|{reg_name})'
port = '(?P<port>[0-9]*)'
authority = f'(?P<authority>({userinfo}@)?{host}(:{port})?)'
pchar = f'({unreserved}|{pct_encoded}|{sub_delims}|[:@])'
segment = f'(?P<path_segment>(?P<segment>({pchar})*))'
path_abempty = f'(?P<path_abempty>(/{segment})*)'
segment_nz = f'(?P<path_segment>(?P<segment_nz>({pchar})+))'
path_absolute = f'(?P<path_absolute>/({segment_nz}(/{segment})*)?)'
path_rootless = f'(?P<path_rootless>{segment_nz}(/{segment})*)'
path_empty = f'(?P<path_empty>({pchar}){{0}})'
hier_part = (
    f'(?P<hier_part>//{authority}{path_abempty}|{path_absolute}|{path_rootless}|'
    f'{path_empty})'
)
query = f'(?P<query>({pchar}|[/?])*)'
absolute_uri = f'(?P<absolute_URI>{scheme}:{hier_part}(\\?{query})?)'
fragment = f'(?P<fragment>({pchar}|[/?])*)'
gen_delims = '[:/?#\\[\\]@]'
segment_nz_nc = f'(?P<segment_nz_nc>({unreserved}|{pct_encoded}|{sub_delims}|@)+)'
path_noscheme = f'(?P<path_noscheme>{segment_nz_nc}(/{segment})*)'
path = (
    f'(?P<path>{path_abempty}|{path_absolute}|{path_noscheme}|{path_rootless}|'
    f'{path_empty})'
)
relative_part = ('(?P<relative_part>'
    f'(//{authority}{path_abempty}|{path_absolute}|'
    f'{path_noscheme}|{path_empty})'
')')
relative_ref = f'(?P<relative_ref>{relative_part}(\\?{query})?(\\#{fragment})?)'
reserved = f'({gen_delims}|{sub_delims})'
uri = f'(?P<URI>{scheme}:{hier_part}(\\?{query})?(\\#{fragment})?)'
uri_reference = f'(?P<URI_reference>{uri}|{relative_ref})'
