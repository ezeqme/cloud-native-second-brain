---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Christine Kim", "Nick Young", "Isovalent at Cisco", "Mattia Lavacca", "Kong", "Guilherme Cassolato", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1hoxF/gateway-api-whats-new-whats-next-christine-kim-nick-young-isovalent-at-cisco-mattia-lavacca-kong-guilherme-cassolato-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Gateway+API%3A+What%27s+New%2C+What%27s+Next%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Gateway API: What's New, What's Next? - Christine Kim & Nick Young, Isovalent at Cisco; Mattia Lavacca, Kong; Guilherme Cassolato, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Christine Kim, Nick Young, Isovalent at Cisco, Mattia Lavacca, Kong, Guilherme Cassolato, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1hoxF/gateway-api-whats-new-whats-next-christine-kim-nick-young-isovalent-at-cisco-mattia-lavacca-kong-guilherme-cassolato-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Gateway+API%3A+What%27s+New%2C+What%27s+Next%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Gateway API: What's New, What's Next?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxF/gateway-api-whats-new-whats-next-christine-kim-nick-young-isovalent-at-cisco-mattia-lavacca-kong-guilherme-cassolato-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Gateway+API%3A+What%27s+New%2C+What%27s+Next%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=reGxuaM7XBs
- YouTube title: Gateway API: What's New, What's Next? - C. Kim, N. Young, M. Lavacca, G. Cassolato
- Match score: 0.72
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/gateway-api-whats-new-whats-next/reGxuaM7XBs.txt
- Transcript chars: 23643
- Keywords: policies, gateway, experimental, standard, features, policy, release, implementations, channel, target, changes, resources, backend, basically, cluster, already, probably, review

### Resumo baseado na transcript

okay folks let's get started um welcome to Gateway API what's new what's next this is the maintainer track Gateway API update uh and uh we're all here to give you uh some updates uh most importantly uh who are we uh my name is Nicky young uh I'm a senior software engineer at ient at Cisco and I'm one of the four gway API maintainers and I'm G I'm a sof engineer at Red Hat and I'm also part of the G API team I'm Christine Kim I also

### Excerpt da transcript

okay folks let's get started um welcome to Gateway API what's new what's next this is the maintainer track Gateway API update uh and uh we're all here to give you uh some updates uh most importantly uh who are we uh my name is Nicky young uh I'm a senior software engineer at ient at Cisco and I'm one of the four gway API maintainers and I'm G I'm a sof engineer at Red Hat and I'm also part of the G API team I'm Christine Kim I also work at I surveillance at Cisco um I focus primarily around open source Dev experience so I care about your pain and I'm laaka I a software engineer working at Kong and I'm a gway maintainer thanks very much everyone so as you can see there's four of us up here so our agenda for today is uh I'm going to run everyone through what's new uh ge will run us through some stuff about policies uh Christine will hit uh user experience improvements and then Mata is going to hit what's up next so in the interest of time I'll uh keep us moving okay um so yeah what's new uh so probably the biggest change in Gateway API uh version 1.2 is the new release cycle uh so we have uh committed to an official release cycle we designated time periods um with four phases scoping iteration and review API refinement and documentation and then uh API review and release candidates so I want to walk through a couple of those because for those of you who are using Gateway pii this is if you want to contribute this is really going to matter so um scoping phase is where we figure out what's going to be in the release uh and uh make sure that uh we're choosing things that have we have people to do and that the community is is actually interested in by we do that with a voting process and a couple of other things um one important thing is that uh we graduate features uh we call features experimental when they're still experimental and then once they are stable we graduate them to standard um we are currently full in the experimental uh channel uh and so we uh need to graduate some things to standard uh to be able to uh add more experimental features so that's probably the thing that's most relevant for you using it is until we get people willing to grad stuff to standard then we can't put new features in um so the output of this is a list of gaps and a Target status for of the lips for the G for the release uh then we once we pick the gaps uh we work on them actually I just realized I did not Define Gap I should do that for those of you who don't know uh uh Gap s
