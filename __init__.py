from .main import ArabaFenice

def autoload():
    return ArabaFenice()

config = [{
    'name': 'arabafenice',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'ArabaFenice',
            'description': '<a href="http://www.arabafenice.me" target="_blank">ArabaFenice</a>',
            'wizard': True,
            'icon': 'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMJkBf/zyX3/++/Z//vv2P/yx3v/vlwA/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv18A////////////vF0A/7pYAP+8XgD//v79////////////yGsO/wAAAAAAAAAAAAAAAAAAAAAAAAAAvFwA//////+9XwL/vF4A/7xfA//Bahb/vV8A/71gAv+8XgD///////////++YQL/AAAAAAAAAAAAAAAAw2YI/f////+9XwD/9eXX///+/f++Ywn/vV8A/8NtHP/uwXb/vV8A/9iia//AZhT//////7tWAfQAAAAAAAAAAP//////////zYdC/82CRv+9YAb/vWAE//HHfP+9XgD/0YlK/7xeAP+9XwD/vV4A////////////AAAAAMJhAv3/////+/bx/8l5M//nxaL/88l9//LIff/amVb/yHcv/8yAQv/Lfz//w2wb/8JrG/+8XgD//////8NiBfrxxnn//////75kEf//////zoNE//PJff/MgEL/zIFC/7xfAv/gpV//88l9/82BQ/+9XwD/vF8A///////wxXn//fbo/////v//////vV8A//LIfP/zyX3//////82BQ////v7/u1sB//PJff/zyX7/vV8A/7xdAP+7WwD/+eXB//326v+7WwD/vF0A/71fAf/fo17////////////XlVT/vV8D////////////vWAE/71fAP+8XgD/8d3K//jju//yx3r//vz8/+XAnP+8XgH/y309///////58er/y39B////////////////////////////vV8B/7xeAP/wxXn/wmEC/f////+8XQD/3a1+//7+/v///////////////////////////////////////////8h3MP++Ygb/w2IF+gAAAAD+/v7//////8FqIP/+/Pz///////////////////////////////////////////++Ygv//v7//wAAAAAAAAAAw2YI/f////+3VAL/vWEH/////////////////////////////////////////////////8dpDfsAAAAAAAAAAAAAAAC8XAD/yHw0///////CbBf//////////////////////////////////////75hAv8AAAAAAAAAAAAAAAAAAAAAAAAAAL5dAP///////////////////////////////////////////7ZRAPYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMJkBf/yyH3/++/Z//vv2f/yx3v/vlwA/AAAAAAAAAAAAAAAAAAAAAAAAAAA+B8AAOAHAADAAwAAgAEAAIABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAQAAgAEAAMADAADgBwAA+B8AAA==',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 3,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]