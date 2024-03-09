# Generated using abnf-to-regex 1.1.2

scheme = '[a-zA-Z][a-zA-Z0-9+\\-.]*'
unreserved = '[a-zA-Z0-9\\-._~]'
pct_encoded = '%[0-9A-Fa-f][0-9A-Fa-f]'
sub_delims = "[!$&'()*+,;=]"
userinfo = f'({unreserved}|{pct_encoded}|{sub_delims}|:)*'
h16 = '[0-9A-Fa-f]{1,4}'
dec_octet = '([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
ipv4address = f'{dec_octet}\\.{dec_octet}\\.{dec_octet}\\.{dec_octet}'
ls32 = f'({h16}:{h16}|{ipv4address})'
ipv6address = (
    f'(({h16}:){{6}}{ls32}|::({h16}:){{5}}{ls32}|({h16})?::({h16}:){{4}}'
    f'{ls32}|(({h16}:)?{h16})?::({h16}:){{3}}{ls32}|(({h16}:){{2}}{h16})?::'
    f'({h16}:){{2}}{ls32}|(({h16}:){{3}}{h16})?::{h16}:{ls32}|(({h16}:){{4}}'
    f'{h16})?::{ls32}|(({h16}:){{5}}{h16})?::{h16}|(({h16}:){{6}}{h16})?::)'
)
ipvfuture = f'[vV][0-9A-Fa-f]+\\.({unreserved}|{sub_delims}|:)+'
ip_literal = f'\\[({ipv6address}|{ipvfuture})\\]'
reg_name = f'({unreserved}|{pct_encoded}|{sub_delims})*'
host = f'({ip_literal}|{ipv4address}|{reg_name})'
port = '[0-9]*'
authority = f'({userinfo}@)?{host}(:{port})?'
pchar = f'({unreserved}|{pct_encoded}|{sub_delims}|[:@])'
segment = f'({pchar})*'
path_abempty = f'(/{segment})*'
segment_nz = f'({pchar})+'
path_absolute = f'/({segment_nz}(/{segment})*)?'
path_rootless = f'{segment_nz}(/{segment})*'
path_empty = f'({pchar}){{0}}'
hier_part = (
    f'(//{authority}{path_abempty}|{path_absolute}|{path_rootless}|'
    f'{path_empty})'
)
query = f'({pchar}|[/?])*'
absolute_uri = f'{scheme}:{hier_part}(\\?{query})?'
fragment = f'({pchar}|[/?])*'
gen_delims = '[:/?#\\[\\]@]'
segment_nz_nc = f'({unreserved}|{pct_encoded}|{sub_delims}|@)+'
path_noscheme = f'{segment_nz_nc}(/{segment})*'
path = (
    f'({path_abempty}|{path_absolute}|{path_noscheme}|{path_rootless}|'
    f'{path_empty})'
)
relative_part = (
    f'(//{authority}{path_abempty}|{path_absolute}|'
    f'{path_noscheme}|{path_empty})'
)
relative_ref = f'{relative_part}(\\?{query})?(\\#{fragment})?'
reserved = f'({gen_delims}|{sub_delims})'
uri = f'{scheme}:{hier_part}(\\?{query})?(\\#{fragment})?'
uri_reference = f'({uri}|{relative_ref})'
