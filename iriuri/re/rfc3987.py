# Generated using abnf-to-regex 1.1.2, using their sample RFC 3987 grammar.

scheme = '[a-zA-Z][a-zA-Z0-9+\\-.]*'
ucschar = (
    '[\\xa0-\\ud7ff\\uf900-\\ufdcf\\ufdf0-\\uffef'
    '\\U00010000-\\U0001fffd\\U00020000-\\U0002fffd'
    '\\U00030000-\\U0003fffd\\U00040000-\\U0004fffd'
    '\\U00050000-\\U0005fffd\\U00060000-\\U0006fffd'
    '\\U00070000-\\U0007fffd\\U00080000-\\U0008fffd'
    '\\U00090000-\\U0009fffd\\U000a0000-\\U000afffd'
    '\\U000b0000-\\U000bfffd\\U000c0000-\\U000cfffd'
    '\\U000d0000-\\U000dfffd\\U000e1000-\\U000efffd]'
)
iunreserved = f'([a-zA-Z0-9\\-._~]|{ucschar})'
pct_encoded = '%[0-9A-Fa-f][0-9A-Fa-f]'
sub_delims = "[!$&'()*+,;=]"
iuserinfo = f'({iunreserved}|{pct_encoded}|{sub_delims}|:)*'
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
unreserved = '[a-zA-Z0-9\\-._~]'
ipvfuture = f'[vV][0-9A-Fa-f]+\\.({unreserved}|{sub_delims}|:)+'
ip_literal = f'\\[({ipv6address}|{ipvfuture})\\]'
ireg_name = f'({iunreserved}|{pct_encoded}|{sub_delims})*'
ihost = f'({ip_literal}|{ipv4address}|{ireg_name})'
port = '[0-9]*'
iauthority = f'({iuserinfo}@)?{ihost}(:{port})?'
ipchar = f'({iunreserved}|{pct_encoded}|{sub_delims}|[:@])'
isegment = f'({ipchar})*'
ipath_abempty = f'(/{isegment})*'
isegment_nz = f'({ipchar})+'
ipath_absolute = f'/({isegment_nz}(/{isegment})*)?'
ipath_rootless = f'{isegment_nz}(/{isegment})*'
ipath_empty = f'({ipchar}){{0}}'
ihier_part = (
    f'(//{iauthority}{ipath_abempty}|{ipath_absolute}|'
    f'{ipath_rootless}|{ipath_empty})'
)
iprivate = '[\\ue000-\\uf8ff\\U000f0000-\\U000ffffd\\U00100000-\\U0010fffd]'
iquery = f'({ipchar}|{iprivate}|[/?])*'
absolute_iri = f'{scheme}:{ihier_part}(\\?{iquery})?'
gen_delims = '[:/?#\\[\\]@]'
ifragment = f'({ipchar}|[/?])*'
isegment_nz_nc = f'({iunreserved}|{pct_encoded}|{sub_delims}|@)+'
ipath_noscheme = f'{isegment_nz_nc}(/{isegment})*'
ipath = (
    f'({ipath_abempty}|{ipath_absolute}|{ipath_noscheme}|'
    f'{ipath_rootless}|{ipath_empty})'
)
irelative_part = (
    f'(//{iauthority}{ipath_abempty}|{ipath_absolute}|'
    f'{ipath_noscheme}|{ipath_empty})'
)
irelative_ref = f'{irelative_part}(\\?{iquery})?(\\#{ifragment})?'
iri = f'{scheme}:{ihier_part}(\\?{iquery})?(\\#{ifragment})?'
iri_reference = f'({iri}|{irelative_ref})'
reserved = f'({gen_delims}|{sub_delims})'